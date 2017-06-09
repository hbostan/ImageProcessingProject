import numpy as np
import copy

def regionGrowing(image, point=(120,50), value=50):
    height, width = np.shape(image)         # Get height and width of image
    resultArr = np.zeros((height,width))     # Create an empty array to show the result
    copyImage = copy.deepcopy(image)        # Also copy the original image to protect it from any changes as python passes lists by reference
                                            
    stack = []                              # Empty stack to keep track of the nodes that are to be visited
    stack.append(point)                      # Start from seed
    
    visitedPixels = {}                      #
                                            # Create a hash table to keep track of the visited pixels so that
    for i in range(height):                 #   we dont visit them again
        visitedPixels[i] = {}               #
    
    seedIntensity = int(copyImage[point[0]][point[1]])     # Initial intensity
    
    while (not(len(stack) == 0)):           # Until there are no pixels to be processed do the following steps
            curY, curX = stack.pop()        # Remove current pixel from stack
            visitedPixels[curY][curX]=1     # Add current pixel to the visited pixels
            if( abs(int(copyImage[curY][curX]) - seedIntensity) < value ): # If the intensity of the current pixel is in the acceptable range
                resultArr[curY][curX] = 255      # Paint pixel white on  the result image
                neighbours = [(curY-1,curX),(curY,curX-1),(curY,curX+1),(curY+1,curX)] # Define which neigbors we want to check
                for y,x in neighbours:      # For every neigbor
                    if( (0 <= x < width) and (0<= y < height) ):    # If they are inside the picture frame
                        if x not in visitedPixels[y].keys():        # And if they haven't already been visited
                            stack.append((y,x))                     # Add them to pixels to be visited list
    return resultArr     # Return the result array