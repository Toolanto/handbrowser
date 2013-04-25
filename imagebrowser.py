from pygame import *
import handdetection
import sys

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
    return imgs #return Surface list of images

  #show image
  #path where are the images
  #index select an image
  #xi translate on x
  #translate on y
  def display_image(self,path,ext,index=0,xi=0,yi=0):
    imgs = self.load_images(path,ext)
    #check if image is bigger than window
    img_w, img_h = imgs[index].get_size()
    if img_w > self.width or img_h > self.height:
      imgs[index] = transform.scale(imgs[index],(800,600))
    #center image	
    x = (self.width-imgs[index].get_width())/2+xi
    y = (self.height-imgs[index].get_height())/2
    self.screen.fill(000)
    self.screen.blit(imgs[index],(x,y))
    display.flip()
      
    



if __name__=='__main__':
  path = sys.argv[1]
  obj = ImageDisplay(800,600)
  running = True
  start = 0
  offsset = 0
  move_x = 0
  image_i= 0
  hd = handdetection.HandDetection("detection")
  handcascade = hd.loadHaarcascade("aGest.xml")
  while running:
    result = hd.detectHand(handcascade)
    if (result[1] == 0):
      start = result[2]
      offsset = result[2]
    elif (result[1]!=0 and result[1]!=None):
      offsset = result[2] - start
      move_x = offsset 
    print result[0:]
    obj.display_image(path,"jpg",image_i,move_x,0)
    if len(event.get(QUIT))>0:
          running = False




