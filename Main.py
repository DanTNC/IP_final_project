import Process as P
import UI
import ImageIO as IIO
import os
import numpy as np
from PIL import Image

class Main(object):
	def __init__(self):
		self.iio = IIO.ImageIO("test.png", "test_o.png")
		self.image = None
		self.result = None
		self.cwd = os.getcwd()
		self.ui = UI.UI(self)

	def run(self):
		self.ui.main_menu()

	def import_image(self, name):
		self.image = self.iio.get_input_image(name, "L")
		self.result = None
		return self.image

	def process(self, borders):
		self.result = P.run(self.image, *borders)
		return self.result

	def save_image(self, name):
		self.iio.save_output_image(name, self.overlap())

	def overlap(self):
		if self.image is not None and self.result is None:
			return self.image
		elif self.image is not None and self.result is not None:
			RGBimage = np.array(Image.fromarray(self.image).convert("RGB"))
			RGBimage[self.result > 0] = np.array([255, 0, 0])
			return RGBimage
		else:
			return np.zeros((512, 512), dtype=int)

if __name__ == '__main__':
	Main().run()