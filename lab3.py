# CST 205
# Authoes: Ivan Alejandre, Alejandro , Matthew Chan, Randy Son
# Lab 3 Picture Manipulation Functions

# ============================================================

# Start by making a couple functions to reduce code repeats
# Prompt the user to select a file, returns image data
def get_pic():
  return makePicture(pickAFile())
  
# Warm Up
def noBlue():
  pic = get_pic()
  pixels = getPixels(pic)
  for x in pixels:
    setBlue(x, 0)
    
  repaint(pic)
# Problem 1

# function requires a parameter of an percentage integer.
def lessRed(percLessRed):
  # convert integer to decimal version of percentage
  percLessRed = percLessRed / 100.0
  if percLessRed == 0:
    pic = get_pic()
    return
  # save data passed from function
  pic = get_pic()
  pixels = getPixels(pic)
  # for each pixel, save red value. Then reduce the value of red by user inputted percentage
  for eachPix in pixels:
    pixRedCt = getRed(eachPix)
    setRed(eachPix, pixRedCt * (1.0 - percLessRed))
  # output the edited picture to the screen
  repaint(pic)
  
def halfRed():
  # modifty picture
  lessRed(50)


# Problem 2
#Potential issues: if your new red value
# is greater than max red val as dictated
# by pixel depth thats an issue. As such
# this fcn puts a cieling at 255
# assuming 8 bit pixel depth for all
# images
def moreRed(percMore):
  pic = get_pic()
  pixels = getPixels(pic)
  newPercTot = 1 + (percMore / 100.0)
  for eachPix in pixels:
    currPixRed = getRed(eachPix)
    newRedVal = floor(currPixRed * newPercTot)
    if (newRedVal > 255):
      setRed(eachPix, 255)
    else:
      setRed(eachPix, newRedVal)
  repaint(pic)
    
# Problem 3
# This function gives an image a pink hue by manipulating the color ratios of each pixel
def roseColoredGlasses():
  pic = get_pic()
  pixels = getPixels(pic)
  for eachPix in pixels:
    newRed = getRed(eachPix) * 1.1
    newBlue = getBlue(eachPix) * 0.8
    newGreen = getGreen(eachPix) * 0.5
    
    # Since the red value is the only value being multiplied by a value greater than 1,
    # we need to implement a ceiling on that value
    if newRed > 255:
      setRed(eachPix, 255)
    else:
      setRed(eachPix, newRed)
      
    # Change the other two colors 
    setBlue(eachPix, newBlue)
    setGreen(eachPix, newGreen)
  
  # show the user the modified image
  repaint(pic)
  
# Problem 4
# this function lightens an image using a built in function in JES
def lightenUp():
  # get picture and save pixel data
  pic = get_pic()
  pixels = getPixels(pic)
  
  #lighten each pixel
  for eachPix in pixels:
    oldColor = getColor(eachPix)
    newColor = makeLighter(oldColor)
    setColor(eachPix, newColor)
    
  # output
  repaint(pic)
  
# Problem 5
# this function inverts an image to its negative
def makeNegative():
  # get picture and save pixel data
  pic = get_pic()
  pixels = getPixels(pic)
  
  # invert each pixel. Each color has a range of 0-255 and 0 is opposite of 255. So, 1 is opposite to 254, 
  # so on for each value and each pair works both ways.
  for eachPix in pixels:
    oppositeRed = 255 - getRed(eachPix)
    oppositeBlue = 255 - getBlue(eachPix)
    oppositeGreen = 255 - getGreen(eachPix)
    setRed(eachPix, oppositeRed)
    setBlue(eachPix, oppositeBlue)
    setGreen(eachPix, oppositeGreen)
    
  # output
  repaint(pic)
    
# Problem 6
# This function turns an image black and white 
def BnW():
  # request image file and store pixel data
  pic = get_pic()
  pixels = getPixels(pic)
  
  # obtain an average of each pixel and set R, G, and B values to that average
  for eachPix in pixels:
    redColor = getRed(eachPix)
    blueColor = getBlue(eachPix)
    greenColor = getGreen(eachPix)
    luminance = (redColor + blueColor + greenColor) / 3
    setRed(eachPix, luminance)
    setBlue(eachPix, luminance)
    setGreen(eachPix, luminance)
    
  # output the image
  repaint(pic)
  
# this function works similar to BnW(), however before the average line, we modify the
# R, G, and B values to given ratios. Since each ratio is less than 1, we do not have to worry
# about any given value exceeding 255 or going below 0. This produces a grayscale image that 
# the human eye can better perceive
def betterBnW():
  #obtain image and pixel data
  pic = get_pic()
  pixels = getPixels(pic)
  
  # modify pixel values by multiplying each one by their ratio, then find the average and set each pixel
  # to that average
  for eachPix in pixels:
    redColor = getRed(eachPix)
    redColor = redColor * 0.299
    blueColor = getBlue(eachPix)
    blueColor = blueColor * 0.587
    greenColor = getGreen(eachPix)
    greenColor = greenColor * 0.114
    luminance = (redColor + blueColor + greenColor) / 3
    setRed(eachPix, luminance)
    setBlue(eachPix, luminance)
    setGreen(eachPix, luminance)
    
  # show the user the revised image
  repaint(pic)
  
