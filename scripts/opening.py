from scipy.ndimage import morphology as mrp
import skimage.morphology as shapes
import numpy as np
import utilities

def opening(image, value=100, shape = shapes.disk(10)):
    image = utilities.makeBin(image, value)
    result = mrp.binary_erosion(image,structure=shape)
    result = mrp.binary_dilation(result,structure=shape)
    return result.astype(float)