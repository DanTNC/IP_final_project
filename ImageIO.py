from PIL import Image
import numpy as np
from scipy.misc import imsave

class ImageIO(object):
	def __init__(self, defi="", defo=""):
		self.defi = defi
		self.defo = defo

	# Load the image and convert it into a numpy array
	# @input_name: the filename of the input image
	# @Return: numpy array presentation of the image
	def get_input_image(self, input_name, mode="RGB"):
		image_name = self.defi if input_name is None else input_name
		im = Image.open(image_name).convert(mode)
		arr = np.array(im) # Convert it to a numpy array
		return arr

	# Save the processed image
	# @output_name: the filename of the output image
	# @im: the image array
	def save_output_image(self, output_name, im, mode=None):
		image_name = self.defo if output_name is None else output_name
		imsave(image_name, im, mode) # Save the modified pixels as image