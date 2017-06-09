import copy
import numpy as np

def averagingBlur(image, value=3):
    #kernel = np.ones((kernelSize,kernelSize))
    kernelSize = value
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
                    newVal += image[currentLine][currentPixel]
            newVal /= (kernelSize*kernelSize)
            newImage[i][j] = newVal
    return newImage