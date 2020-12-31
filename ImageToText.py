#importing all the requerd libraries 
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pytesseract as pt
import cv2
import numpy as np

#path where google's tesseract module is installed
pt.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

#usinf Tkinter Gui module to choose and open image file
Tk().withdraw()
#It will return filepath
filename = askopenfilename()
print(filename)

#function to show image using opencv
def imshow(*args):
	cv2.imshow('image',*args)
	cv2.waitKey(0)
	cv2.destroyAllWindows()	

#if file is choosen then this program will work else it will exit
if filename:
	#Reading image
	image = cv2.imread(filename)

	#using filter to shrpen the image
	filt = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
	sg = cv2.filter2D(image,-1,filt)

	#converting image into gray image
	sg = cv2.cvtColor(sg, cv2.COLOR_BGR2GRAY)
	#Applying threshold to preprocess the image
	sg = cv2.threshold(sg, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
	#MedianBlur is used to remove noise from the image
	sg = cv2.medianBlur(sg, 3)

	#showing final image
	imshow(sg)

	#finally using google's API Pytesseract to recognize text in image and saving in a veriable as string to print
	st = pt.image_to_string(sg)
	print(type(st), '\n', st)

else:
	exit()