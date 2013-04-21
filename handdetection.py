import cv
import time
import Image

cv.NamedWindow("camera", 1)
capture = cv.CreateCameraCapture(0)

width = None
height = None

if width is None:
  width = int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_WIDTH))
else:
  cv.SetCaptureProperty(capture,cv.CV_CAP_PROP_FRAME_WIDTH,width)    
if height is None:
  height = int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_HEIGHT))
else:
  cv.SetCaptureProperty(capture,cv.CV_CAP_PROP_FRAME_HEIGHT,height) 

result = cv.CreateImage((width,height),cv.IPL_DEPTH_8U,3) 



avg = 0 #inizializzazione media
def scrollImage(rect):
  global avg
  range = 2 #definizione margine di errore
  count = 0
  for r in rect:
    count = count + int(r[0][0])
  temp_avg=count/len(rect)
  #print "{0} {1}".format(avg,temp_avg)
  if avg +range < temp_avg  or avg == 0: #la prima volta imposto la media
    avg = temp_avg
    return 1
  elif avg - range > temp_avg:	
    avg = temp_avg
    return -1
  else:
    return 0


def DetectHand(image, handCascade):
	min_size = (20,20)
	image_scale = 2
	haar_scale = 1.2
	min_neighbors = 2
	haar_flags = 0

	# Allocate the temporary images
	gray = cv.CreateImage((image.width, image.height), 8, 1)
	smallImage = cv.CreateImage((cv.Round(image.width / image_scale),cv.Round (image.height / image_scale)), 8 ,1)

	# Convert color input image to grayscale
	cv.CvtColor(image, gray, cv.CV_BGR2GRAY)

	# Scale input image for faster processing
	cv.Resize(gray, smallImage, cv.CV_INTER_LINEAR)

	# Equalize the histogram
	cv.EqualizeHist(smallImage, smallImage)

	# Detect the hand
	hand = cv.HaarDetectObjects(smallImage, handCascade, cv.CreateMemStorage(0),haar_scale, min_neighbors, haar_flags, min_size)
	# If hand are found
	if hand:
		print scrollImage(hand)
		#check the color
		#create rectangle
		for ((x, y, w, h), n) in hand:
                  	#print n
		# the input to cv.HaarDetectObjects was resized, so scale the
			pt1 = (int(x * image_scale), int(y * image_scale))
			pt2 = (int((x + w) * image_scale), int((y + h) * image_scale))
			cv.Rectangle(image, pt1, pt2, cv.RGB(255, 0, 0), 3, 8, 0)
    		cv.SetImageROI(image, (pt1[0],pt1[1],pt2[0] - pt1[0],int((pt2[1] - pt1[1]) * 0.7)))	
	cv.ResetImageROI(image)
	return image



handCascade = cv.Load("aGest.xml")

while True:
	img = cv.QueryFrame(capture)
	image = DetectHand(img, handCascade)
	cv.ShowImage("camera", image)
	k = cv.WaitKey(10);
	if k == 102:
		break


