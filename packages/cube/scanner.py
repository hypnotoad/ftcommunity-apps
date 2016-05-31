#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#

# quick'n dirty scanner or the rubiks cube solver. This uses opencv to access
# the camera.

# import the necessary packages
import time, os
import numpy as np
import cv2

# default is non interactive mode
interactive = False

SCAN_ITERATIONS=10
FRAME_SKIP=5

Y = 6
X = 26
S = 110

SMIN =  70   # this is the boundary between white and the colors
SMAX = 255

VMIN =  50
VMAX = 255

# RGB
BE = 10
GE = 70
YE = 110     # critial boundary between yellow and orange
OE = 120     # critical boundary between orange and red
RE = 145 

RANGES = [
# list of hsv boundaries
# list of "mixed" hsv boundaries from RGB with B/R swapped
    ("blue",   0x0000FF, [RE+1, SMIN, VMIN],  [ BE, SMAX, VMAX]),
    ("green",  0x00FF00, [BE+1, SMIN, VMIN],  [ GE, SMAX, VMAX]),
    ("yellow", 0xFFFF00, [GE+1, SMIN, VMIN],  [ YE, SMAX, VMAX]),
    ("orange", 0xFF8000, [YE+1, SMIN, VMIN],  [ OE, SMAX, VMAX]),
    ("red",    0xFF0000, [OE+1, SMIN, VMIN],  [ RE, SMAX, VMAX]),
    ("white",  0xFFFFFF, [   0,    0,   10],  [180, SMIN, VMAX]) 
]

image_files = None
video_device = None

#
WIDTH = 160
HEIGHT = 120
FPS = 5

S_F = S/3          # size of one square
S_B = S_F/4        # border to be ignored
S_I = S_F - 2*S_B  # used part

def analyze_range(image, lower, upper):
    # find the colors within the specified boundaries and apply
    # the mask. if upper[0] is lower than lower[0], then "wrap"
    if upper[0] > lower[0]:
        return cv2.inRange(image, lower, upper)

    mask0 = cv2.inRange(image, lower, np.array( [180, upper[1], upper[2]], dtype = "uint8" ))
    mask1 = cv2.inRange(image, np.array( [0, lower[1], lower[2]], dtype = "uint8" ), upper)
    return cv2.bitwise_or(mask0, mask1)
        
def get_weights(mask):        
    # get all nine mask weights
    m = [[0 for x in range(3)] for y in range(3)] 
    for y in range(3):
        ym = int(y*S_F+S_B)
        yn = int(y*S_F+S_B+S_I-1)
        for x in range(3):
            xm = int(x*S_F+S_B)
            xn = int(x*S_F+S_B+S_I)
            m[y][x] = cv2.mean(mask[ym:yn,xm:xn])[0]/255

    return m
            
def analyze(full_image, adjust = 0):    
    # cut cube
    gimage = full_image[Y:Y+S,X:X+S]
    if interactive:
        images = [ gimage ]

    # ------------ step 1: blur the image ------------------
    gimage = cv2.blur(gimage,(5,5))
    if interactive:
        images.append(gimage)

    # ------------ step 2: mask colored squares ------------------
    image = np.zeros((S,S,3), np.uint8)
    for y in range(3):
        ym = int(y*S_F+S_B)
        yn = int(y*S_F+S_B+S_I-1)
        for x in range(3):
            xm = int(x*S_F+S_B)
            xn = int(x*S_F+S_B+S_I)
            image[ym:yn,xm:xn] = gimage[ym:yn,xm:xn]

    # convert to hsv space
    image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

    if interactive:
        image_dsp = cv2.cvtColor(image, cv2.COLOR_HSV2RGB)
        images.append(image_dsp)
    
    # ------------ step 3: loop over the color filters ----------
    weights = {}
    for (name, value, lower, upper) in RANGES:
        # apply color adjustment value
        mask = analyze_range(image,
               np.array((lower[0]+adjust, lower[1], lower[2]), dtype = "uint8"),
               np.array((upper[0]+adjust, upper[1], upper[2]), dtype = "uint8"))

        # get colour weights
        weights[name] = get_weights(mask)

        # paint mask in color that was meant to be detected
        if interactive:
            bg = np.zeros((S,S,3), np.uint8)
            c = int(value)
            bg[0:S,0:S] = ((c >> 0)& 0xff, (c >> 8)& 0xff, (c>>16) & 0xff)
            images.append(cv2.bitwise_and(bg, bg, mask = mask))

    # ------------ step 4: analyse color weightings --------------
    if interactive:
        image = np.zeros((S,S,3), np.uint8)

    result = [[0 for x in range(3)] for y in range(3)] 
    for y in range(3):
        ym = int(y*S_F+2)
        yn = int(y*S_F+S_F-4)
        for x in range(3):
            xm = int(x*S_F+2)
            xn = int(x*S_F+S_F-4)
            max_weighted = ("unknown", 0x000000, 0)
            for i in RANGES:
                # check for max
                val = weights[i[0]][y][x]
                if val > max_weighted[2]:
                    max_weighted = (i[0], i[1], val)

            result[y][x] = max_weighted

            if interactive:
                # create image
                c = int(max_weighted[1])
                image[ym:yn,xm:xn] = ((c >> 0)& 0xff, (c >> 8)& 0xff, (c>>16) & 0xff)

    # ------------ step 5: determine quality --------------
    # consider the image to be as good as it's worst detected value
    quality = 1.0
    for y in range(3):
        for x in range(3):
            if result[y][x][2] < quality:
                quality = result[y][x][2]

    if interactive:
        images.append(image)
        # make a hstack of all images and display it
        cv2.imshow("images", np.hstack(images))

    return quality, result

def scan(image):
    step = 0
    # adjust_steps = ( 0, 1,-1,2,-2,3,-3,4,-4,5,-5,6,-6 )
    adjust_steps = ( 0, 1,2,3,4,5,6 )

    quality = 0
    best = (0,0)

    while quality < 0.99 and step < len(adjust_steps):
        (quality, result) = analyze(image, adjust_steps[step])
        if quality > best[0]: best = (quality, step)
        step += 1

    # if we didn't reach a 0.99 score check which step had the best quality
    if quality < 0.99:
        (quality, result) = analyze(image, adjust_steps[best[1]])
        step = best[1]+1

    #print("Accepted quality is", quality, "in step", step, "with adjust", adjust_steps[step-1])

    # extract color information from result
    colors = [[0 for x in range(3)] for y in range(3)] 
    for y in range(3):
        for x in range(3):
            colors[y][x] = result[y][x][0]
                
    return quality, colors

def do(video_device):
    # drop a few frames to get "fresh" images and to
    # let white balance etc kick in
    for i in range(FRAME_SKIP):
        video_device.read()

    results = []
    for i in range(SCAN_ITERATIONS):
        image = video_device.read()[1]
        (quality, colors) = scan(image)

        # check if such a result already exists in the list
        if not colors in (item[1] for item in results):
            # append the new result as a tuple with the quality
            results.append( (quality, colors) )
        else:
            # color set already exists as a result. Just
            # increase the quality value
            quality += results[ ([y[1] for y in results].index(colors)) ][0]
            results[ ([y[1] for y in results].index(colors)) ] = (quality, colors)

    # now sort the results by quality
    # print("Number of different results: ", len(results))
    return sorted(results, key=lambda x: x[0], reverse=True)

def init():
    CAM_DEV = os.environ.get('FTC_CAM')
    if CAM_DEV == None: CAM_DEV = 0
    else:               CAM_DEV = int(CAM_DEV)

    video_device = cv2.VideoCapture(CAM_DEV)
    if video_device.isOpened():
        video_device.set(3,WIDTH)
        video_device.set(4,HEIGHT)
        video_device.set(5,FPS)
        print("Video device started")
        return video_device

    print("Unable to open video device")
    return None

def close(video_device):
    video_device.release()

if __name__ == "__main__":
    #    global interactive
    interactive = True

    # test usage
    video_device = init()

    if video_device:
        time.sleep(1)   # wait 5 seconds for camera auto adjust
        while True:
            results = do(video_device)
            print("Number of results: ", len(results))
            for i in results:
                print("{:5.2f}".format(i[0]), i[1])

            if cv2.waitKey(100) == 27:
                exit(0)