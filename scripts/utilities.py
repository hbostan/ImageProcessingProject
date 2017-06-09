import numpy as np
import skimage.morphology as shapes

def butter2d_lp(shape,f,n,pxd=1):
    pxd = float(pxd)
    rows,cols = shape
    x = np.linspace(-0.5, 0.5,cols) * cols /pxd
    y = np.linspace(-0.5, 0.5,rows) * rows /pxd
    radius = np.sqrt((x**2)[np.newaxis]+(y**2)[:, np.newaxis])
    filt = 1 / (1.0 + (radius / f)**(2*n))
    return filt

def generateBandpassFilter(type, start, size, shape, n = 1, pxd = 1):
    if type == 'ideal':
        height, width = shape
        smallMask = mrp.disk(start)
        bigMask = mrp.disk(size)
        bigH,bigW = np.shape(bigMask)
        smallH, smallW = np.shape(smallMask)
        for i in range(smallH):
            for j in range(smallW):
                bigMask[(bigH-1)/2-start+i][(bigH-1)/2-start+j] -= smallMask[i][j]       
        filterMask = np.zeros(shape)
        filterMask[np.round(height-1)/2-size:np.round(height-1)/2+size+1,np.round(width-1)/2-size:np.round(width-1)/2+size+1]=bigMask
        return filterMask

    elif type == 'butter':
        rows, cols = shape
        smallMask = butter2d_lp(shape,start,n,pxd)
        bigMask = butter2d_lp(shape, size,n,pxd)
        for i in range(rows):
            for j in range(cols):
                bigMask[i][j]-=smallMask[i][j]
        return bigMask
    return None

def diceScore(image,original):
    xSize,ySize = np.shape(image)
    difference = np.zeros((xSize,ySize),dtype=bool)
    
    truePositives=0
    falsePositives=0
    falseNegatives=0
    positives=0
    
    for i in range(xSize):
        for j in range(ySize):
            if (image[i][j] and original[i][j]):
                truePositives+=1.0
            if (image[i][j] ^ original[i][j] and (not original[i][j])):
                falsePositives+=1.0
            if (image[i][j] ^ original[i][j] and original[i][j]):
                falseNegatives+=1.0
            if (original[i][j]):
                positives+=1.0
            difference[i][j] = image[i][j] ^ original[i][j]
    
    return (2*truePositives) / (2*truePositives+falseNegatives+falsePositives)

def make2d(image):
    if check2d(image):
        return image
    else:
        try:
            y, x, z = np.shape(image)
        except:
            print "Error handling image"
        else:
            grayscaleImage = np.zeros((y,x))
            for i in range(y):
                for j in range(x):
                    r, g, b = image[i][j]
                    grayscaleImage[i][j] = 0.21*r + 0.72*g + 0.07*b
            return grayscaleImage
            
def check2d(image):
    try:
        y, x = np.shape(image);
    except:
        return False
    else:
        return True

def makeBin(image, thresh=100):
    return (image<thresh).astype(float)