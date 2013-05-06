from pygame import *
import handdetection
import sys
import cv
import os

class ImageDisplay:

  def __init__(self,width,height):
    self.width = width
    self.height = height
    display.init()	
    self.screen = display.set_mode([width,height])
    display.set_caption("HandBrowser")


  def load_images(self,path):
    nameofimgs = os.listdir(path)
    self.imgs = [image.load(path+name) for name in nameofimgs]
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





