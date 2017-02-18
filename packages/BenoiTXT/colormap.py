#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#

def listColorMaps():
    return ["default","rainbow","forest","planet","beach","fire","dreamy","autumn","oeco telecom","icy","r-g-b","y-c-m","kill bill","amstrad","zuse","boole","roentgen","3d glasses","soylent green","douglas adams","matrix","from hell", "night flash"]

def setColorMap(name:str="default"):
    colormap=[1,1,1]*16
    if name=="rainbow":        
        colormap[ 0]=[255,   0,   0]
        colormap[ 1]=[255,  80,   0]
        colormap[ 2]=[255, 180,   0]
        colormap[ 3]=[255, 255,   0]
        colormap[ 4]=[192, 255,   0] 
        colormap[ 5]=[128, 255,   0] 
        colormap[ 6]=[ 64, 255,   0] 
        colormap[ 7]=[  0, 255,   0] 
        colormap[ 8]=[  0, 192,  64] 
        colormap[ 9]=[  0, 128, 128] 
        colormap[10]=[  0,  64, 192] 
        colormap[11]=[  0,   0, 255] 
        colormap[12]=[ 64,   0, 255] 
        colormap[13]=[128,   0, 255] 
        colormap[14]=[192,   0, 255] 
        colormap[15]=[255,   0, 255] 
    elif name=="forest":        
        colormap[ 0]=[142,  94,   5] # d.braun
        colormap[ 1]=[180, 120,   7]
        colormap[ 2]=[210, 150,  12]
        colormap[ 3]=[240, 165,  32] # h.braun
        colormap[ 4]=[180, 165,  14] 
        colormap[ 5]=[150, 130,  10] 
        colormap[ 6]=[100,  80,   7] 
        colormap[ 7]=[ 50,  60,   4] 
        colormap[ 8]=[  0,  42,   0] # d.grün 
        colormap[ 9]=[ 20,  92,  20] 
        colormap[10]=[ 40, 142,  40] 
        colormap[11]=[ 60, 192,  60] 
        colormap[12]=[ 80, 225,  80] 
        colormap[13]=[ 96, 255,  96] # h.grün
        colormap[14]=[132, 180,  45] 
        colormap[15]=[160, 105,   6] 
    elif name=="planet":        
        colormap[ 0]=[255, 255, 255] # weiß
        colormap[ 1]=[227, 227, 255]
        colormap[ 2]=[200, 200, 255] # h.blau
        colormap[ 3]=[150, 150, 200]
        colormap[ 4]=[100, 100, 120] 
        colormap[ 5]=[ 50,  50,  80] 
        colormap[ 6]=[  0,   0,  42] # d.blau 
        colormap[ 7]=[  2,  16,  32] 
        colormap[ 8]=[  4,  32,  24] 
        colormap[ 9]=[  7,  48,  16] 
        colormap[10]=[ 10,  64,  10] # d.gn 
        colormap[11]=[ 80, 150,  85] 
        colormap[12]=[170, 255, 180] # h.gn
        colormap[13]=[130, 200, 120] 
        colormap[14]=[ 90, 120,  60] 
        colormap[15]=[ 42,  42,   0] # d.bn
    elif name=="fire":        
        colormap[ 0]=[ 32,   0,   0] # bk
        colormap[ 1]=[ 32,  32,   5]
        colormap[ 2]=[ 64,  32,   8] # d.red
        colormap[ 3]=[128,  64,   8]
        colormap[ 4]=[192,   0,   0] 
        colormap[ 5]=[210,   0,   0] 
        colormap[ 6]=[255,   0,   0] 
        colormap[ 7]=[255,  30,  30] #red! 
        colormap[ 8]=[255,  60,  23] 
        colormap[ 9]=[255, 120,  14] 
        colormap[10]=[255, 200,   7] 
        colormap[11]=[255, 255, 0] 
        colormap[12]=[250, 250, 0] 
        colormap[13]=[245, 245, 0] 
        colormap[14]=[240, 240, 255] 
        colormap[15]=[255, 255, 255]
    elif name=="dreamy":        
        colormap[ 0]=[255, 255, 255]
        colormap[ 1]=[228, 228, 255]
        colormap[ 2]=[204, 204, 255]
        colormap[ 3]=[184, 184, 255]
        colormap[ 4]=[160, 160, 255] 
        colormap[ 5]=[192, 192, 255] 
        colormap[ 6]=[224, 224, 255] 
        colormap[ 7]=[255, 255, 255] 
        colormap[ 8]=[255, 224, 224] 
        colormap[ 9]=[255, 192, 192] 
        colormap[10]=[255, 160, 160] 
        colormap[11]=[255, 192, 160] 
        colormap[12]=[255, 224, 160] 
        colormap[13]=[255, 255, 160] 
        colormap[14]=[255, 255, 202] 
        colormap[15]=[255, 255, 255]
    elif name=="autumn":        
        colormap[ 0]=[  0, 120,   0]
        colormap[ 1]=[ 40, 108,   3]
        colormap[ 2]=[ 80,  95,   6]
        colormap[ 3]=[120,  80,   9]
        colormap[ 4]=[160,  65,  12] 
        colormap[ 5]=[200,  50,  15] 
        colormap[ 6]=[225,  35,  18] 
        colormap[ 7]=[255,  20,  20] 
        colormap[ 8]=[255,  60,  28] 
        colormap[ 9]=[255, 100,  36] 
        colormap[10]=[255, 140,  42] 
        colormap[11]=[255, 180,  50] 
        colormap[12]=[255, 220,  57] 
        colormap[13]=[255, 255,  64] 
        colormap[14]=[170, 210,  42] 
        colormap[15]=[100, 170,  20]
    elif name=="icy":        
        colormap[ 0]=[ 64, 128, 255]
        colormap[ 1]=[ 95, 145, 255]
        colormap[ 2]=[125, 170, 255]
        colormap[ 3]=[155, 195, 255]
        colormap[ 4]=[190, 215, 255] 
        colormap[ 5]=[220, 235, 255] 
        colormap[ 6]=[255, 255, 255] 
        colormap[ 7]=[210, 210, 255] 
        colormap[ 8]=[172, 172, 255] 
        colormap[ 9]=[136, 136, 255] 
        colormap[10]=[100, 100, 255] 
        colormap[11]=[ 64,  64, 255] 
        colormap[12]=[ 64,  74, 255] 
        colormap[13]=[ 64,  85, 255] 
        colormap[14]=[ 64,  96, 255] 
        colormap[15]=[ 64, 107, 255]
    elif name=="r-g-b":        
        colormap[ 0]=[  0,   0,   0]
        colormap[ 1]=[ 64,   0,   0]
        colormap[ 2]=[128,   0,   0]
        colormap[ 3]=[196,   0,   0]
        colormap[ 4]=[255,   0,   0] 
        colormap[ 5]=[196,  64,   0] 
        colormap[ 6]=[128, 128,   0] 
        colormap[ 7]=[ 64, 196,   0] 
        colormap[ 8]=[  0, 255,   0] 
        colormap[ 9]=[  0, 192,  64] 
        colormap[10]=[  0, 128, 128] 
        colormap[11]=[  0,  64, 196] 
        colormap[12]=[  0,   0, 255] 
        colormap[13]=[  0,   0, 196] 
        colormap[14]=[  0,   0, 128] 
        colormap[15]=[  0,   0,  64]
    elif name=="y-c-m":        
        colormap[ 0]=[255, 255, 255]
        colormap[ 1]=[255, 255, 196]
        colormap[ 2]=[255, 255, 128]
        colormap[ 3]=[255, 255,  64]
        colormap[ 4]=[255, 255,   0] 
        colormap[ 5]=[192, 255,  64] 
        colormap[ 6]=[128, 255, 128] 
        colormap[ 7]=[ 64, 255, 192] 
        colormap[ 8]=[  0, 255, 255] 
        colormap[ 9]=[ 64, 196, 255] 
        colormap[10]=[128, 128, 255] 
        colormap[11]=[196,  64, 255] 
        colormap[12]=[255,   0, 255] 
        colormap[13]=[255,  96, 255] 
        colormap[14]=[255, 192, 255] 
        colormap[15]=[255, 255, 255]
    elif name=="amstrad":        
        colormap[ 0]=[  0,  32,   0]
        colormap[ 1]=[  6,  48,   2]
        colormap[ 2]=[ 12,  64,   4]
        colormap[ 3]=[ 18,  80,   6]
        colormap[ 4]=[ 26,  96,   8] 
        colormap[ 5]=[ 36, 112,  10] 
        colormap[ 6]=[ 48, 128,  12] 
        colormap[ 7]=[ 62, 144,  14] 
        colormap[ 8]=[ 78, 160,  16] 
        colormap[ 9]=[ 94, 176,  18] 
        colormap[10]=[110, 192,  20] 
        colormap[11]=[126, 208,  22] 
        colormap[12]=[126, 224,  24] 
        colormap[13]=[126, 240,  26] 
        colormap[14]=[126, 255,  29] 
        colormap[15]=[126, 255,  32]
    elif name=="zuse":        
        colormap[ 0]=[255, 128,   0]
        colormap[ 1]=[32,   16,   0]
        colormap[ 2]=[255, 128,   0]
        colormap[ 3]=[32,   16,   0]
        colormap[ 4]=[255, 128,   0] 
        colormap[ 5]=[32,   16,   0] 
        colormap[ 6]=[255, 128,   0] 
        colormap[ 7]=[32,   16,   0] 
        colormap[ 8]=[255, 128,   0] 
        colormap[ 9]=[32,   16,   0] 
        colormap[10]=[255, 128,   0] 
        colormap[11]=[32,   16,   0] 
        colormap[12]=[255, 128,   0] 
        colormap[13]=[32,   16,   0] 
        colormap[14]=[255, 128,   0] 
        colormap[15]=[32,   16,   0]    
    elif name=="roentgen":        
        colormap[ 0]=[  0,   0,   0]
        colormap[ 1]=[ 16,  16,  16]
        colormap[ 2]=[ 32,  32,  32]
        colormap[ 3]=[ 48,  48,  48]
        colormap[ 4]=[ 64,  64,  64] 
        colormap[ 5]=[ 80,  80,  80] 
        colormap[ 6]=[ 96,  96,  96] 
        colormap[ 7]=[112, 112, 112] 
        colormap[ 8]=[128, 128, 128] 
        colormap[ 9]=[144, 144, 144] 
        colormap[10]=[160, 160, 160] 
        colormap[11]=[176, 176, 176] 
        colormap[12]=[192, 192, 192] 
        colormap[13]=[208, 208, 208] 
        colormap[14]=[224, 224, 224] 
        colormap[15]=[240, 240, 240]
    elif name=="boole":        
        colormap[ 0]=[255, 255, 255]
        colormap[ 1]=[255, 255, 255]
        colormap[ 2]=[255, 255, 255]
        colormap[ 3]=[255, 255, 255]
        colormap[ 4]=[  0,   0,   0]  
        colormap[ 5]=[  0,   0,   0] 
        colormap[ 6]=[  0,   0,   0] 
        colormap[ 7]=[  0,   0,   0]  
        colormap[ 8]=[255, 255, 255] 
        colormap[ 9]=[255, 255, 255] 
        colormap[10]=[255, 255, 255] 
        colormap[11]=[255, 255, 255] 
        colormap[12]=[  0,   0,   0] 
        colormap[13]=[  0,   0,   0] 
        colormap[14]=[  0,   0,   0] 
        colormap[15]=[  0,   0,   0]
    elif name=="beach":        
        colormap[ 0]=[128, 128, 255] # light blue sky
        colormap[ 1]=[ 64,  64, 255]
        colormap[ 2]=[  0,   0, 255]
        colormap[ 3]=[  0,   0, 192] # darker at the horizon
        colormap[ 4]=[218, 165,  32] # sand! 
        colormap[ 5]=[255, 193,  37] 
        colormap[ 6]=[238, 180,  34] 
        colormap[ 7]=[205, 155,  29] # wet sand!
        colormap[ 8]=[185, 155,  49] 
        colormap[ 9]=[165, 155,  69] # shallow water
        colormap[10]=[100,  80,  80] 
        colormap[11]=[30,   20, 128] 
        colormap[12]=[  0,   0,  64] # deep sea
        colormap[13]=[  0,   0, 128] 
        colormap[14]=[  0,   0, 192] 
        colormap[15]=[192, 192, 255] # white crest waves
    elif name=="3d glasses":        
        colormap[ 0]=[255,   0,   0]
        colormap[ 1]=[224,  32,  32]
        colormap[ 2]=[192,  64,  64]
        colormap[ 3]=[160,  96,  96]
        colormap[ 4]=[128, 128, 128] 
        colormap[ 5]=[ 96, 160, 160] 
        colormap[ 6]=[ 64, 192, 192] 
        colormap[ 7]=[ 32, 224, 224] 
        colormap[ 8]=[  0, 255, 255] 
        colormap[ 9]=[ 32, 224, 224] 
        colormap[10]=[ 64, 192, 192] 
        colormap[11]=[ 96, 160, 160] 
        colormap[12]=[128, 128, 128] 
        colormap[13]=[160,  96,  96] 
        colormap[14]=[192,  64,  64] 
        colormap[15]=[224,  32,  32]
    elif name=="soylent green":        
        colormap[ 0]=[  0, 255,   0]
        colormap[ 1]=[ 32, 255,   0]
        colormap[ 2]=[ 64, 255,   0]
        colormap[ 3]=[ 96, 255,   0]
        colormap[ 4]=[128, 255,   0] 
        colormap[ 5]=[160, 255,   0] 
        colormap[ 6]=[192, 255,   0] 
        colormap[ 7]=[224, 255,   0] 
        colormap[ 8]=[255, 255,   0] 
        colormap[ 9]=[224, 255,   0] 
        colormap[10]=[192, 255,   0] 
        colormap[11]=[160, 255,   0] 
        colormap[12]=[128, 255,   0] 
        colormap[13]=[ 96, 255,   0] 
        colormap[14]=[ 64, 255,   0] 
        colormap[15]=[ 32, 255,   0]    
    elif name=="douglas adams":        
        colormap[ 0]=[ 42,   0,   0]
        colormap[ 1]=[ 84,  42,   0]
        colormap[ 2]=[126,  84,  42]
        colormap[ 3]=[168, 126,  42]
        colormap[ 4]=[210, 158, 126] 
        colormap[ 5]=[252, 210, 158] 
        colormap[ 6]=[210, 252, 210] 
        colormap[ 7]=[168, 210, 252] 
        colormap[ 8]=[126, 168, 210] 
        colormap[ 9]=[ 84, 126, 168] 
        colormap[10]=[ 42,  84, 126] 
        colormap[11]=[  0,  42,  84] 
        colormap[12]=[ 42,   0,  42] 
        colormap[13]=[ 84,  42,   0] 
        colormap[14]=[126,  84,  42] 
        colormap[15]=[168, 126,  84]
    elif name=="matrix":        
        colormap[ 0]=[  0,   0,   0]
        colormap[ 1]=[  0,   0,   0]
        colormap[ 2]=[  0,  64,   0]
        colormap[ 3]=[  0, 128,   0]
        colormap[ 4]=[  0, 192,   0] 
        colormap[ 5]=[  0, 255,   0] 
        colormap[ 6]=[  0, 192,   0] 
        colormap[ 7]=[  0, 128,   0] 
        colormap[ 8]=[  0,  64,   0] 
        colormap[ 9]=[  0,   0,   0] 
        colormap[10]=[  0,  32,   0] 
        colormap[11]=[  0,  64,   0] 
        colormap[12]=[  0,  96,   0] 
        colormap[13]=[  0,  64,   0] 
        colormap[14]=[  0,  32,   0] 
        colormap[15]=[  0,   0,   0]
    elif name=="from hell":        
        colormap[ 0]=[  0,   0,   0]
        colormap[ 1]=[ 32,   0,   0]
        colormap[ 2]=[ 96,   0,   0]
        colormap[ 3]=[192,   0,   0]
        colormap[ 4]=[255,   0,   0] 
        colormap[ 5]=[255, 160,   0] 
        colormap[ 6]=[255, 255,   0] 
        colormap[ 7]=[255, 160,   0] 
        colormap[ 8]=[255,   0,   0] 
        colormap[ 9]=[192,   0,   0] 
        colormap[10]=[ 96,   0,   0] 
        colormap[11]=[ 32,   0,   0] 
        colormap[12]=[  0,   0,   0] 
        colormap[13]=[  0,   0,   0] 
        colormap[14]=[255,   0,   0] 
        colormap[15]=[  0,   0,   0]    
    elif name=="night flash":        
        colormap[ 0]=[  0,   0,   0]
        colormap[ 1]=[  0,   0,   0]
        colormap[ 2]=[  0,   0,   0]
        colormap[ 3]=[  0,   0,   0]
        colormap[ 4]=[  0,   0,   0] 
        colormap[ 5]=[  0,   0,   0] 
        colormap[ 6]=[  0,   0,   0] 
        colormap[ 7]=[  0,   0,   0] 
        colormap[ 8]=[  0,   0,   0] 
        colormap[ 9]=[  0,   0,   0] 
        colormap[10]=[  0,   0, 192] 
        colormap[11]=[ 64, 255, 255] 
        colormap[12]=[255, 255, 255] 
        colormap[13]=[  0,   0,   0] 
        colormap[14]=[  0,   0,   0] 
        colormap[15]=[  0,   0,   0]
    elif name=="kill bill":        
        colormap[ 0]=[255, 255,   0]
        colormap[ 1]=[255, 255,   0]
        colormap[ 2]=[255, 255,   0]
        colormap[ 3]=[224, 224,   0]
        colormap[ 4]=[208, 208,   0] 
        colormap[ 5]=[192, 192,   0] 
        colormap[ 6]=[176, 176,   0] 
        colormap[ 7]=[  0,   0,   0] 
        colormap[ 8]=[  0,   0,   0] 
        colormap[ 9]=[255, 255,   0] 
        colormap[10]=[  0,   0,   0] 
        colormap[11]=[  0,   0,   0] 
        colormap[12]=[176, 176,   0] 
        colormap[13]=[192, 192,   0] 
        colormap[14]=[208, 208,   0] 
        colormap[15]=[224, 224,   0]
    elif name=="oeco telecom":         
        colormap[ 0]=[255,   0, 255]
        colormap[ 1]=[224,  32, 224]
        colormap[ 2]=[192,  64, 192]
        colormap[ 3]=[160,  96, 160]
        colormap[ 4]=[128, 128, 128] 
        colormap[ 5]=[ 96, 160,  96] 
        colormap[ 6]=[ 64, 192,  64] 
        colormap[ 7]=[ 32, 224,  32] 
        colormap[ 8]=[  0, 255,   0] 
        colormap[ 9]=[ 32, 224,  32] 
        colormap[10]=[ 64, 192,  64] 
        colormap[11]=[ 96, 160,  96] 
        colormap[12]=[128, 128, 128] 
        colormap[13]=[160,  96, 128] 
        colormap[14]=[192,  64, 192] 
        colormap[15]=[224,  32, 224]
    else:  
        colormap[ 0]=[ 66,  30,  15]
        colormap[ 1]=[ 25,   7,  26]
        colormap[ 2]=[  9,   1,  47]
        colormap[ 3]=[  4,   4,  73]
        colormap[ 4]=[  0,   7, 100] # blue 4
        colormap[ 5]=[ 12,  44, 138] # blue 3
        colormap[ 6]=[ 24,  82, 177] # blue 2
        colormap[ 7]=[ 57, 125, 209] # blue 1
        colormap[ 8]=[134, 181, 229] # blue 0
        colormap[ 9]=[211, 236, 248] # lightest blue
        colormap[10]=[241, 233, 191] # lightest yellow
        colormap[11]=[248, 201,  95] # light yellow
        colormap[12]=[255, 170,   0] # dirty yellow
        colormap[13]=[204, 128,   0] # brown 0
        colormap[14]=[153,  87,   0] # brown 1
        colormap[15]=[106,  52,   3] # brown 2 
    return colormap

"""
    elif name=="":        
        colormap[ 0]=[]
        colormap[ 1]=[]
        colormap[ 2]=[]
        colormap[ 3]=[]
        colormap[ 4]=[] 
        colormap[ 5]=[] 
        colormap[ 6]=[] 
        colormap[ 7]=[] 
        colormap[ 8]=[] 
        colormap[ 9]=[] 
        colormap[10]=[] 
        colormap[11]=[] 
        colormap[12]=[] 
        colormap[13]=[] 
        colormap[14]=[] 
        colormap[15]=[]
"""