import Tkinter as TK
import tkFileDialog as TKFD
from PIL import Image, ImageTk
import re

class UI(object):
	def __init__(self, main):
		self.main = main
		self.window = TK.Tk()
		self.x = self.window.winfo_screenwidth()
		self.y = self.window.winfo_screenheight()
		self.place(self.window)
		self.cwdregex = re.compile("^{}/".format(self.main.cwd))
		self.lines = {}
		self.imagename = "img/empty.png"

	def place(self, window):
		window.geometry("+{}+{}".format(int(self.x/3), int(self.y/3)))

	def main_menu(self):
		self.window.title("heart image processer")

		lf = TK.Frame(self.window)

		TK.Button(lf,
					width=20, height=2,
					text="import image",
					command=self.import_image).pack(padx=10, pady=10)
		TK.Button(lf,
					width=20, height=2,
					text="process",
					command=self.process).pack(padx=10, pady=10)
		TK.Button(lf,
					width=20, height=2,
					text="save image",
					command=self.save).pack(padx=10, pady=10)
		self.x1 = TK.StringVar(lf)
		self.x1.trace("w", lambda name, index, mode, ele=self.x1: self.move_border("x1", ele))
		TK.Label(lf, text="x1").pack()
		TK.Spinbox(lf, from_=0, to=511, increment=1, textvariable=self.x1).pack()
		self.x2 = TK.StringVar(lf)
		self.x2.trace("w", lambda name, index, mode, ele=self.x2: self.move_border("x2", ele))
		self.x2.set("511")
		TK.Label(lf, text="x2").pack()
		TK.Spinbox(lf, from_=0, to=511, increment=1, textvariable=self.x2).pack()
		self.y1 = TK.StringVar(lf)
		self.y1.trace("w", lambda name, index, mode, ele=self.y1: self.move_border("y1", ele))
		TK.Label(lf, text="y1").pack()
		TK.Spinbox(lf, from_=0, to=511, increment=1, textvariable=self.y1).pack()
		self.y2 = TK.StringVar(lf)
		self.y2.trace("w", lambda name, index, mode, ele=self.y2: self.move_border("y2", ele))
		self.y2.set("511")
		TK.Label(lf, text="y2").pack()
		TK.Spinbox(lf, from_=0, to=511, increment=1, textvariable=self.y2).pack()

		lf.pack(side="left")

		self.canvas = TK.Canvas(self.window, width=512, height=512, bg="black")
		self.canvas.pack(padx=10, pady=10, side="left")
		self.draw_lines()

		self.window.mainloop()

	def imshow(self, arr):
		self.image = ImageTk.PhotoImage(Image.fromarray(arr)) # prevent image to be recycled so use an attribute to store it
		self.canvas.create_image(0, 0, anchor="nw", image=self.image)
		self.draw_lines()

	def import_image(self):
		img = TKFD.askopenfilenames(initialdir="img/",
										filetypes=[("images",".jpg .png")],
										title="Please choose images to import",
										parent=self.window)
		self.imagename = re.sub(self.cwdregex, "", img[0])
		self.imshow(self.main.import_image(self.imagename))

	def process(self):
		self.main.process(self.borders())
		self.imshow(self.main.overlap())

	def save(self):
		fn, ext = self.imagename.split(".")
		self.main.save_image("{}_o.{}".format(fn, ext))

	def draw_lines(self):
		for v in self.lines.itervalues():
			self.canvas.delete(v)
		self.lines["x1"] = self.canvas.create_line(int(self.x1.get()), 0, int(self.x1.get()), 512, fill="yellow")
		self.lines["x2"] = self.canvas.create_line(int(self.x2.get()), 0, int(self.x2.get()), 512, fill="yellow")
		self.lines["y1"] = self.canvas.create_line(0, int(self.y1.get()), 512, int(self.y1.get()), fill="yellow")
		self.lines["y2"] = self.canvas.create_line(0, int(self.y2.get()), 512, int(self.y2.get()), fill="yellow")

	def move_border(self, varname, var):
		if not hasattr(self, "canvas") or var.get() == "": return
		var = int(var.get())
		if varname == "x1" or varname == "x2":
			if self.lines.has_key(varname):
				self.canvas.delete(self.lines[varname])
			self.lines[varname] = self.canvas.create_line(var, 0, var, 512, fill="yellow")
		if varname == "y1" or varname == "y2":
			if self.lines.has_key(varname):
				self.canvas.delete(self.lines[varname])
			self.lines[varname] = self.canvas.create_line(0, var, 512, var, fill="yellow")

	def borders(self):
		x1, x2, y1, y2 = int(self.x1.get()), int(self.x2.get()), int(self.y1.get()), int(self.y2.get())
		if x1 > x2:
			x1, x2 = x2, x1
		if y1 > y2:
			y1, y2 = y2, y1
		return [x1, x2, y1, y2]