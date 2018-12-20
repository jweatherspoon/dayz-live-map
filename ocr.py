from PIL import Image
import pytesseract
import argparse 
import cv2
import os 

FILENAME = "screenshot.jpg"

image = cv2.imread(FILENAME)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)