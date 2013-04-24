from pygame import *
import handdetection

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
  def display_image(self,path,ext,index=0,xi=0,xy=0):
    imgs = self.load_images(path,ext)
    #check if image is bigger than window
    img_w, img_h = imgs[index].get_size()
    if img_w > self.width or img_h > self.height:
      imgs[index] = transform.scale(imgs[index],(800,600))
    #center image	
    x = (self.width-imgs[index].get_width())/2+xi
    y = (self.height-imgs[index].get_height())/2
    self.screen.blit(imgs[index],(x,y))
    display.flip()
      
    



if __name__=='__main__':
  obj = ImageDisplay(800,600)
  running = True
  while running:
    obj.display_image("image/","jpg",1,i,0)
    if len(event.get(QUIT))>0:
          running = False




