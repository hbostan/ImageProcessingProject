import numpy as np
import scipy
import matplotlib.pyplot as plt
import importlib
import inspect
import scripts
import os
import argparse
import shutil
import skimage.morphology
import sys

desc='''This program takes the 2d images in a directory and processes them after processing results are saved inside the
provided directory in a folder called "output"
'''

epi=''' For user created scripts:
    The script must have a single python function inside with the same name as the file name 
( if the file name is "myscript.py" function name must be "myscript" ). Further said function
    MUST take the image as an numpy ndarray and after all processing result should be returned 
again as numpy ndarray to be handled properly. To pass arguments from commandline to your script
you can use built-in "value", "point", and "shape" parameters. Again if you wish to pass these to
your funtion the names should be same in the function decleration ( e.g. myscript(image,value,point): )
You can check the files under scripts/ for examples
'''
functionList = [item for item in dir(scripts) if not item.startswith("_")]

#TODO! Add subparsers for commands for better argument passing
parser = argparse.ArgumentParser(epilog=epi, description=desc)
parser.add_argument( "-l", "--list", help="List the supported operations", action='store_true')
parser.add_argument( "-p", "--path", help="Path to the folder which contains the images to be processed. Default directory is \"./pictures/\"", default="pictures/")
group = parser.add_mutually_exclusive_group()
group.add_argument( "-o", "--operation", help="Operation to be applied to the images inside the folder. To list the supported operations use --list/-l")
group.add_argument( "-s", "--script", help="Path to the user specified script, for details on how to write a compatible script read further...")
parser.add_argument("--value", nargs="?", help="Integer value to be passed to the script, if not provided default values are used", default=None, type=int)
parser.add_argument("--point", nargs="*", help="Point value to be passed to the script, if not provided default values are used", default=None)
parser.add_argument("--shape", nargs="*", help="Shape value to be passed to the script, if not provided default values are used", default=None)
args = parser.parse_args()

if args.list:
    for item in functionList:
        print item
    exit(0)
elif args.path and os.path.exists(args.path):
    if args.operation and args.operation not in functionList:
        parser.error("Invalid operation.")
    elif args.script:
        if not os.path.exists(args.script):
            parser.error("Invalid script path")
        elif os.path.isdir(args.script):
            parser.error("Script path is a directory")
    elif not (args.operation or args.script):
        parser.error("An operation or a script must be provided.")

arguments = {}
if args.value != None:
    arguments['value'] = args.value
if args.point != None:
    arguments['point'] = (int(args.point[0]),int(args.point[1]))
if args.shape != None:
    if len(args.shape) == 2:
        arguments['shape'] = getattr(skimage.morphology, args.shape[0])(int(args.shape[1]))
    else:
        arguments['shape'] = getattr(skimage.morphology, args.shape[0])(int(args.shape[1]), int(args.shape[2]))

if args.script:
    p = os.path.dirname(os.path.abspath(args.script))
    n = os.path.basename(os.path.abspath(args.script))[:-3]
    sys.path.insert(0, p)
    mod = __import__(n, globals(),locals())
    processFunction = getattr(mod, n)

elif args.operation:
    processFunction = getattr(getattr(scripts,args.operation), args.operation)

picturePath = os.path.abspath(args.path)

filesToProcess = [(os.path.abspath(picturePath+"/"+file), file) for file in os.listdir(os.path.abspath(args.path))]
filesToProcess = [(file,name) for file,name in filesToProcess if os.path.isfile(file)]

outputDirectory = os.path.abspath(args.path) + "/output"
if os.path.exists(outputDirectory):
    shutil.rmtree(outputDirectory)
os.makedirs(outputDirectory)
outputDirectory = os.path.abspath(outputDirectory)

def callProcessFunction(image, arguments):
    keys = arguments.keys()
    # value
    if 'value' in keys and 'point' not in keys and 'shape' not in keys:
        return processFunction(image, value = arguments['value'])
    # shape
    elif 'value' not in keys and 'point' not in keys and 'shape' in keys:
        return processFunction(image, shape = arguments['shape'])
    # point
    elif 'value' not in keys and 'point' in keys and 'shape' not in keys:
        return processFunction(image, point = arguments['point'])
    # value, point
    elif 'value' in keys and 'point' in keys and 'shape' not in keys:
        return processFunction(image, value = arguments['value'], point = arguments['point'])
    # value, shape
    elif 'value' in keys and 'point' not in keys and 'shape' in keys:
        return processFunction(image, value = arguments['value'], shape = arguments['shape'])
    # point, shape
    elif 'value' not in keys and 'point' in keys and 'shape' in keys:
        return processFunction(image, point = arguments['point'], shape = arguments['shape'])
    # value, point, shape
    elif 'value' in keys and 'point' in keys and 'shape' in keys:
        return processFunction(image, value = arguments['value'], point = arguments['point'], shape = arguments['shape'])
    else:
        return processFunction(image)

for file, fileName in filesToProcess:
    image = scipy.misc.imread(file)
    image = scripts.utilities.make2d(image)
    image = callProcessFunction(image, arguments)
    scipy.misc.imsave(outputDirectory + "/" + fileName, image)


        
