import numpy as np

def fft(image):
    return np.fft.fftshift(np.log(1+np.abs(np.fft.fft2(image))))