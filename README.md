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

## Built-in Operations
	These operations can be specified with OPERATION (-o) option. Some of these operations take further arguments.
	
### averagingBlur

### closing

### dialation

### erosion

### fft

### gaussianBlur

### medianFilter

### opening

### regionGrowing

### sharpen

### thresholding

  It divides the image into foreground and background based on the threshold value. The output is a binary image.
Thresholding is done according to the passed in "--value", if no value is passed the default is 128. Following code
performs thresholding with a threshold value of 94

	python main.py -p PATH_TO_FOLDER -o thresholding --value 94
	


### utilities


## Usage examples
python main.py -p C:\Users\hakan\Desktop\pictures -o gaussianBlur --value 5