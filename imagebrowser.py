from pygame import *
import handdetection
import sys
import cv

class ImageDisplay:

  def __init__(self,width,height):
    self.width = width
    self.height = height
    display.init()	
    self.screen = display.set_mode([width,height])
    display.set_caption("HandBrowser")

  # load image es. 0.jpg; 1.jpg ...
  def load_images(self,path,ext):
    imgs = []
    for i in [0,1,2]:
      temp = "{0}.".format(i)
      imgs.append(image.load(path+temp+ext)) 
    self.imgs = imgs #return Surface list of images
    return self.imgs

  #show image
  #path where are the images
  #index select an image
  #xi translate on x
  #translate on y
  def display_image(self,path,ext,index,xi=0,yi=0):
    #check if image is bigger than window
    img_w, img_h = self.imgs[index].get_size()
    if img_w > self.width or img_h > self.height:
      self.imgs[index] = transform.scale(self.imgs[index],(800,600))
    #center image	
    x = (self.width-self.imgs[index].get_width())/2+xi
    y = (self.height-self.imgs[index].get_height())/2
    self.screen.fill(000)
    self.screen.blit(self.imgs[index],(x,y))
    display.flip()
      
if __name__=='__main__':
  path = sys.argv[1]
  haarcascade = sys.argv[2]
  obj = ImageDisplay(800,600)
  running = True
  start = 0
  offsset = 0
  move_x = 0
  image_i= 0
  index = 0
  first = True
  imgs = obj.load_images(path,"jpg")
  hd = handdetection.HandDetection("detection",800,600)
  handcascade = hd.loadHaarcascade(haarcascade)
  while running:
    stop = False
    result = hd.detectHand(handcascade)

    if result[1] == 0 and first:
      start = result[2]
      first = False
    elif result[1] != 0 and result[1] != None:
      offsset = result[2] - start
      #start = offsset
      move_x -= offsset 
    elif result[1] == None or result[2] == None:
      first = True
      move_x = 0
      
    if move_x > 20 and image_i < len(imgs) -1 and not(first):
      index = index + 1
      offsset = 0
      move_x = 0
      start = result[2]
      #first = True
    elif move_x < -20 and image_i > 0 and not(first):
      index = index - 1
      offsset = 0
      move_x = 0
      start = result[2]
      #first = True
    
    print start, offsset,move_x,index
    image_i = index
    obj.display_image(path,"jpg",image_i,move_x,0)
    k = hd.showImage("detection", result[0])
    if len(event.get(QUIT))>0 or k == 102:
      running = False




