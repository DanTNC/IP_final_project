import Process as P
import UI
import ImageIO as IIO

class Main(object):
	def __init__():
		self.ui = UI.UI(self)
		self.iio = IIO.ImageIO("test.png", "test_o.png")
		self.image = None
		self.result = None

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
		self.iio.save_output_image(name)

	def overlap(self):
		# overlap image and result
		pass

if __name__ == '__main__':
	Main().run()