from imagebrowser import *
if __name__=='__main__':
  path = sys.argv[1]
  haarcascade = sys.argv[2]

  running = True
  start = 0
  offsset = 0
  move_x = 0
  image_i= 0
  index = 0
  first = True
  width_display = 800
  height_display = 600
  width_cam = 700
  height_cam = 500

  obj = ImageDisplay(width_display,height_display)
  imgs = obj.load_images(path)
  hd = handdetection.HandDetection("detection",width_cam,height_cam)
  
  handcascade = hd.loadHaarcascade(haarcascade)
  while running:
    stop = False
    result = hd.detectHand(handcascade)
    
    if result[1] == 0 and first:
      start = result[2] * width_display / width_cam #proporzione
      move_x = 0
      first = False
    elif result[1] != 0 and result[1] != None:
      offsset = result[2] - start
      move_x -= offsset
    elif result[1] == None or result[2] == None:
      first = True
      move_x = 0
      
    if move_x > 50 and image_i < len(imgs) -1 and not(first):
      index = index + 1
      offsset = 0
      move_x = 0
      start = result[2]
    elif move_x < -50 and image_i > 0 and not(first):
      index = index - 1
      offsset = 0
      move_x = 0
      start = result[2]
    
    #print start, offsset,move_x,index
    image_i = index
    obj.display_image(path,"jpg",image_i,move_x,0)
    k = hd.showImage("detection", result[0])
    if len(event.get(QUIT))>0 or k == 102:
      running = False
