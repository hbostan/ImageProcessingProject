import numpy as np
import copy

def sharpen(image):
    #kernel = np.ones((kerne\Size,kernelSize))
    kernelSize = 3;
    kernel = [[0,-1,0],[-1,5,-1],[0,-1,0]]
    height, width = np.shape(image)
    newImage = copy.deepcopy(image)
    for i in range(height):
        for j in range(width):
            newVal = 0
            for k in range(-kernelSize/2+1,kernelSize/2+1):
                for l in range(-kernelSize/2+1, kernelSize/2+1):
                    currentLine = i + k
                    currentPixel= j + k
                    if (currentLine < 0 ):
                        currentLine = 0
                    if (currentPixel < 0):
                        currentPixel = 0
                    if (currentLine >= height):
                        currentLine = height-1
                    if (currentPixel >= width):
                        currentPixel = width - 1
                    #print k+kernelSize/2, l+kernelSize/2
                    newVal += image[currentLine][currentPixel]*kernel[k+kernelSize/2][l+kernelSize/2]
            #newVal /= (kernelSize*kernelSize)
            newImage[i][j] = newVal
    return newImage