import copy
import numpy as np

def medianFilter(image, value=5):
    #kernel = np.ones((kernelSize,kernelSize))
    kernelSize=value
    height, width = np.shape(image)
    newImage = copy.deepcopy(image)
    window=  []
    for i in range(height):
        for j in range(width):
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
                    window.append(image[currentLine][currentPixel])
            #newVal /= (kernelSize*kernelSize)
            newImage[i][j] = np.median(np.array(window))
            window = []
    return newImage
