import cv
import Image
import pygame

class ImageDisplay:

  def __init__(self, namew):
    self._namew = namew
    cv.NamedWindow(namew,0)
    cv.ResizeWindow(namew,800,600)

  # load image es. 0.jpg; 1.jpg ...
  def load_image(self,path,ext):
    imgs = []
    for i in [0,1,2]:
      temp = "{0}.".format(i)
      imgs.append(cv.LoadImage(path+temp+ext))
    return imgs

  def display_image(self, index, path, ext):
    imgs = obj.load_image(path,ext)
    while True:
      cv.ShowImage(self._namew,imgs[index])
      k = cv.WaitKey(10)
      if k == 102:
        break

obj = ImageDisplay("browser")
obj.display_image(0,"image/","jpg")




