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
  percLessRed = percLessRed/100.0
  if percLessRed == 0:
    pic = get_pic()
    return
  # save data passed from function
  pic = get_pic()
  pixels = getPixels(pic)
  # for each pixel, save red value. Then reduce the value of red by user inputted percentage
  for eachPix in pixels:
    pixRedCt = getRed(eachPix)
    setRed(eachPix, pixRedCt*(1.0 - percLessRed))
  # output the edited picture to the screen
  repaint(pic)
  
def halfRed():
  # modifty picture
  lessRed(50)


# Problem 2
def moreRed():
  pic = get_pic()
  pixels = getPixels(pic)
  percentage = input("From 0-100, what percentage do you wish to increase the red pixel value: ")
  p = 1+(percentage/100)
  for x in pixels:
    r = getRed(x)
    newRed = r*p
    if newRed > 255:
      setRed(x, 255)
    else:
      setRed(x, newRed)
  repaint(pic)
    
# Problem 3
def roseColoredGlasses():
  pic = get_pic()
  pixels = getPixels(pic)
  for x in pixels:
    r = getRed(x)
    b = getBlue(x)
    g = getGreen(x)
    setRed(x, r*1.1)
    setBlue(x, b*0.8)
    setGreen(x, g*0.5)
  repaint(pic)
  
# Problem 4

def lightenUp():
  # get picture and save pixel data
  pic = get_pic()
  pixels = getPixels(pic)
  #lighten each pixel
  for x in pixels:
    oldColor = getColor(x)
    newColor = makeLighter(oldColor)
    setColor(x, newColor)
  # output
  repaint(pic)
  
# Problem 5
def makeNegative():
  # get picture and save pixel data
  pic = get_pic()
  pixels = getPixels(pic)
  # invert each pixel
  for x in pixels:
    oppositeRed = 255 - getRed(x)
    oppositeBlue = 255 - getBlue(x)
    oppositeGreen = 255 - getGreen(x)
    setRed(x, oppositeRed)
    setBlue(x, oppositeBlue)
    setGreen(x, oppositeGreen)
  # output
  repaint(pic)
    
# Problem 6
def BnW():
  pic = get_pic()
  pixels = getPixels(pic)
  
  for x in pixels:
    redColor = getRed(x)
    blueColor = getBlue(x)
    greenColor = getGreen(x)
    luminance = (redColor+blueColor+greenColor)/3
    setRed(x, luminance)
    setBlue(x, luminance)
    setGreen(x, luminance)
  
  repaint(pic)
  
def betterBnW():
  pic = get_pic()
  pixels = getPixels(pic)
  
  for x in pixels:
    redColor = getRed(x)
    redColor = redColor*0.299
    blueColor = getBlue(x)
    blueColor = blueColor*0.587
    greenColor = getGreen(x)
    greenColor = greenColor*0.114
    luminance = (redColor+blueColor+greenColor)/3
    setRed(x, luminance)
    setBlue(x, luminance)
    setGreen(x, luminance)
  
  repaint(pic)
  
