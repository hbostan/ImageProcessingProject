import utilities
import scipy.ndimage.filters as filters

def gaussianBlur(image, value = 3):
    return filters.gaussian_filter(image, value)