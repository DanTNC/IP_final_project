import Tkinter as TK
import tkFileDialog as TKFD

class UI(object):
	def __init__(self, main):
		self.main = main
		self.window = TK.TK()
		self.x = self.window.winfo_screenwidth()
		self.y = self.window.winfo_screenheight()
		self.place(self.window)

	def place(self, window):
		window.geometry("+{}+{}".format(int(self.x/2.5), int(self.y/2.5)))

	def main_menu(self):
		self.window.title("heart image processer")

		# TK.Button()

	def import_image(self):
		img = self.TKFD.askopenfilenames(initialdir="img/",
										filetypes=[("images",".jpg .png")],
										title="Please choose images to import",
										parent=self.window)
		self.imagename = img
		self.imshow(self.main.import_image(img))

	def process(self):
		self.main.process(self.borders())
		self.imshow(self.main.overlap())

	def save(self):
		fn, ext = self.imagename.split(".")
		self.main.save_image("{}_o.{}".format(fn, ext))

	def move_border(self):
		# get button name
		# modify border textvar
		pass