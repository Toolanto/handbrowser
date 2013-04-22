from pygame import *

class ImageDisplay:

  def __init__(self,width,height):
    self.width = width
    self.height = height
    display.init()	
    self.screen = display.set_mode([width,height])

  # load image es. 0.jpg; 1.jpg ...
  def load_image(self,path,ext):
    imgs = []
    for i in [0,1,2]:
      temp = "{0}.".format(i)
      imgs.append(image.load(path+temp+ext)) 
    return imgs

  def display_image(self,path,ext):
    running = True
    while running:
      imgs = self.load_image(path,ext)
      #center the image
      x = (self.width-imgs[0].get_width())/2
      y = (self.height-imgs[0].get_height())/2
      self.screen.blit(imgs[0],(x,y))
      display.flip()
      if len(event.get(QUIT))>0:
          running = False
    



if __name__=='__main__':
  obj = ImageDisplay(800,600)
  obj.display_image("image/","jpg")




