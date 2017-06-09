# Image Processing Project


  This program takes the 2d images in a directory and processes them after
processing results are saved inside the provided directory in a folder called
"output"

```
	usage: main.py [-h] [-l] [-p PATH] [-o OPERATION | -s SCRIPT]
			       [--value [VALUE]] [--point [POINT [POINT ...]]]
                   [--shape [SHAPE [SHAPE ...]]]

optional arguments:
  -h, --help            show this help message and exit
  -l, --list            List the supported operations
  -p PATH, --path PATH  Path to the folder which contains the images to be
                        processed. Default directory is "./pictures/"
  -o OPERATION, --operation OPERATION
                        Operation to be applied to the images inside the
                        folder. To list the supported operations use --list/-l
  -s SCRIPT, --script SCRIPT
                        Path to the user specified script, for details on how
                        to write a compatible script read further...
  --value [VALUE]       Integer value to be passed to the script, if not
                        provided default values are used
  --point [POINT [POINT ...]]
                        Point value to be passed to the script, if not
                        provided default values are used
  --shape [SHAPE [SHAPE ...]]
                        Shape value to be passed to the script, if not
                        provided default values are used

For user created scripts: The script must have a single python function inside
with the same name as the file name ( if the file name is "myscript.py"
function name must be "myscript" ). Further said function MUST take the image
as an numpy ndarray and after all processing result should be returned again
as numpy ndarray to be handled properly. To pass arguments from commandline to
your script you can use built-in "value", "point", and "shape" parameters.
Again if you wish to pass these to your funtion the names should be same in
the function decleration ( e.g. myscript(image,value,point): ) You can check
the files under scripts/ for examples.
```

## `--value`, `--point`, `--shape`

These options are used to pass parameters to operations.

`--value` is used for passing a single integer argument.
Example:
	--value 54

`--point` is used for passing a point. Option is followed by two numbers y and x coordinate.
Example:
	--point 40 85
	
`--shape` is used for passing a shape to operations which need a structuring element. Shape names are
used to call functions from skimage.morphology package. Some structures need only one argument and some
need two arguments to create. Correct amount of arguments must be provided. For supported shapes and more info 
see [here](http://scikit-image.org/docs/dev/api/skimage.morphology.html)
Examples:

	--shape rectangle 10 5
	
	--shape star 13
	
	--shape disk 23

## Built-in Operations

These operations can be specified with OPERATION (-o) option. Some of these operations take further arguments.
	
### averagingBlur

Performs blurring using an averagin filter. Size of kernel can be determined with the `--value` option.
Default size of the kernel is 3 ( i.e. 3x3 matrix ). Following command blurs the image with a kernel of 5x5.

	python main.py -p PATH_TO_FOLDER -o averagingBlur --value 5

### closing

Performs closing operation on the image. First it converts image to a binary image, using the value passed in with
`--value` option (default is 128). Then uses the structure passed with `--shape` to create the structuring element
and performs closing on the binary image. Default value of `--shape` is a disk with a 10 unit radius.

Following command converts image to binary using the value 80 and performs closing with a square with a side of 5
units.

	python main.py -p PATH_TO_FOLDER -o closing --value 80 --shaoe square 5

### dialation

Performs dialation operation on the image. First it converts image to a binary image, using the value passed in with
`--value` option (default is 128). Then uses the structure passed with `--shape` to create the structuring element
and performs dialation on the binary image. Default value of `--shape` is a disk with a 10 unit radius.

Following command converts image to binary using the value 80 and performs dialation with a square with a side of 5
units.

	python main.py -p PATH_TO_FOLDER -o dialation --value 80 --shape square 5

### erosion

Performs erosion operation on the image. First it converts image to a binary image, using the value passed in with
`--value` option (default is 128). Then uses the structure passed with `--shape` to create the structuring element
and performs erosion on the binary image. Default value of `--shape` is a disk with a 10 unit radius.

Following command converts image to binary using the value 100 and performs erosion with a disk which has 35 unit 
radius.

	python main.py -p PATH_TO_FOLDER -o erosion --value 100 --shape disk 35

### fft

Performs FFT on the given image. Result is the spectrum of the image. Doesn't take any arguments.

	python main.py -p PATH_TO_FOLDER -o fft

### gaussianBlur

Performs gaussian blur on the image. Sigma value for the operation can be passed in with `--value` option.
Default is 3. Following command performs gaussian blur with the sigma value 5.

	python main.py -p PATH_TO_FOLDER -o gaussianBlur --value 5

### medianFilter

Performs median filtering on the image. Size of the kernel can be determined with `--value`. Default is 3.

	python main.py -p PATH_TO_FOLDER -o medianFilter

### opening

Performs opening operation on the image. First it converts image to a binary image, using the value passed in with
`--value` option (default is 128). Then uses the structure passed with `--shape` to create the structuring element
and performs opening on the binary image. Default value of `--shape` is a disk with a 10 unit radius.

Following command converts image to binary using the value 100 and performs opening with a disk which has 35 unit 
radius.

	python main.py -p PATH_TO_FOLDER -o opening --value 100 --shape disk 35

### regionGrowing

Performs region growing algorithm on the image. Seed can be determined with `--point` option. Threshold can be
determined with `--value` option. Default value for seed is the (0,0) point. Default value for threshold is 128.
Following command performs region growing with the seed point of (120,50) and with threshold value of 150.

	python main.py -p PATH_TO_FOLDER -o regionGrowing --point 120 50 --value 150

### sharpen

Sharpens the image using a convolution matrix. Used matrix is given below. Doesn't take any arguments.
```
[0,-1,0]
[-1,5,-1]
[0,-1,0]
```

	python main.py -p PATH_TO_FOLDER -o sharpen

### thresholding

It divides the image into foreground and background based on the threshold value. The output is a binary image.
Thresholding is done according to the passed in "--value", if no value is passed the default is 128. Following code
performs thresholding with a threshold value of 94

	python main.py -p PATH_TO_FOLDER -o thresholding --value 94
	

	
### utilities

This is not a usable operation.

## Using User Created Scripts

User created scripts are also python scripts. These scripts must have only a single python function inside.
Moreover the name of the funtion and the name of the script file must be the same. For example if we have
a script file `myscript.py`, the function inside the file must be named `myscript`. Said function must have at least
one argument, the image to be processed. The main program passes the image to the script in numpy ndarray
format. And to save the image to the output directory, function must again return the image in numpy ndarray format.
You can also use `--value`,`--shape` and `--point` options in your scripts. All that is need to be done is to add these
arguments to your function decleration. For example `myscript(inputImage, value=None, shape=None, point=None)`. Default
values are not mandatory but recommended. To use your script instead of `-o` you should use `-s` and provide the 
path to your script. Or if you want to use your script as an operation you can move your script file inside the `scripts/`
directory and it will be recognised by the program.

	python main.py -p PATH_TO_FOLDER -s PATH_TO_SCRIPT

For example if we have a script named `doSomething.py` in `~/Desktop/` which contains the function:
```
doSomething(inputImg, value=15):
	...
	...
	return ...
```
Can be used in the program with the following command:

	python main.py -p PATH_TO_FOLDER -s ~/Desktop/doSomething.py --value 45

## Usage examples

Imagine we need to perform gaussian blur on all the images inside the `\home\hakan\Desktop\pictures`.

```
hakan@SOVEREIGN:~/Desktop/pictures$ ls
image1.jpg  image2.jpg  image3.jpg  image4.jpg  image5.jpg
```

We have 5 images to be processed. Now from the directory of our script we can use the following command to perform
gaussian blur with a sigma value of 5.

	python main.py -p ~/Desktop/pictures -o gaussianBlur --value 5

After the command

```
hakan@SOVEREIGN:~/Desktop/pictures$ ls
image1.jpg  image2.jpg  image3.jpg  image4.jpg  image5.jpg  output
```
and
```
hakan@SOVEREIGN:~/Desktop/pictures/output$ ls
image1.jpg  image2.jpg  image3.jpg  image4.jpg  image5.jpg
```

Processed output images can be found under `\home\hakan\Desktop\pictures\output`.
















