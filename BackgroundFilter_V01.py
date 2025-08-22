#   Original Author: Kevin Telfer
#   Date Modified: 08/21/25
#   Copyright 2025
#   Version 1.0

# To run .py file in Huygens python shell insert path of script into following example: source("C:/user/myScript.py")
## USER ENTRY REQUIRED for following 4 lines 
myPath = "D:/user/folder/myImageFile.czi"                     # paste file path (forward slash required)
destinationPath = "D:/user/folder/project/filteredImages"     # paste the file path of destination folder
Tiles = 9                                                     # enter the number of tiles in the image
ImageRoot = "myImageFile" + ":M"                              # enter file name. Defines subImage root for Zeiss file
                                                              
huOpt.report("Starting filtering of selected images")
for i in range(Tiles):                                        # loop through integers up to the number of tiles
    InputImage = ImageRoot + f"{i}"                           # define the name of each subImage every loop 
    gaussFiltered = image("gaussFiltered")                    ## create empty image for filtered products
    gaussMinFiltered = image("gaussMinFiltered")
    subtractedImage = image("subtractedImage")
    
    # load in the individual subImage from the image file provided in myPath
    rawImg = image (path = myPath, query = False, foreignTo = "int", cmode = "clip", keepA = False, notMapped = False,
    logEnable = False, subImage = InputImage, subIndex = -1, tileIndex = -1, angleIndex = -1, series = "query")
    
    rawImg.convert(type = "int", chanspec = "stacked")   # convert data type to integer for filter compatibility

    # apply a small gaussian filter to original image and create a new image with the product
    rawImg.qgauss(gaussFiltered, sigma = [3, 3, 3, 1], units = "mus", edge = "trunc", maxWidth = 25, acc = 0.1)

    # apply a minimum filter to the gaussian filter product
    gaussFiltered.minFilter(gaussMinFiltered, width = [9, 9, 21], edge = "trunc")

    # subtract the background found using the combined gaussian minimum filter from the original image
    subtractedImage = rawImg - gaussMinFiltered

    ## name filtered images numerically to be compatible with Huygens stitcher module
    if i<10:                                                    
        filename = destinationPath + f"/filteredImage00{i}"
    elif 100>i>=10:
        filename = destinationPath + f"/filteredImage0{i}"
    elif i>=100:
        filename = destinationPath + f"/filteredImage{i}"

    # Saves the individual filtered tiles to desired destination
    subtractedImage.save(filename, type = "ics2", compr = False, comprlevel = 4, tiffMultiDir = False,
    omeTiffMultiDir = "z,t,ch", cmode = "stretch", q = 90, tclReturn = False)
huOpt.report("finished saving all filtered images") # Message in Huygens Task reports window