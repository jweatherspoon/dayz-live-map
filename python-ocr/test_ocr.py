import unittest 
from unittest import mock 
from matplotlib import pyplot as plt 
import numpy as np 

import ocr 

class TestOCR(unittest.TestCase):
    def setUp(self):
        self.jpg = 'test_screenshot.jpg' 
        self.png = 'test_cropped.png'

    def test_crop_position(self):
        data = plt.imread(self.jpg)
        cropped = ocr.crop_position(data)

        cropped_correct = plt.imread(self.png)[:,:,0:3]
        self.assertEqual(cropped.shape, cropped_correct.shape)