# coding=utf-8
import os
import tkFileDialog
import tkinter as tk
from PIL import Image, ImageTk


class MainApplication(tk.Tk):
	image = photo = []
	
	def __init__(self):
		tk.Tk.__init__(self)
		self.var_photo = tk.IntVar()
		self.path = tk.StringVar()
		
		self.title("Photo Labelling Software")
		self.geometry("1000x800")
		# self.master.attributes('-zoom', True)
		# self.attributes('-fullscreen', True)
		self.grid_rowconfigure(1, weight = 1)
		self.grid_columnconfigure(0, weight = 1)
		
		self.frame1 = tk.Frame(self.master)
		self.frame2 = tk.Frame(self.master)
		self.frame1.grid(row = 0, sticky = "ew")
		self.frame2.grid(row = 1, sticky = "nsew")
		
		self.canvas = tk.Canvas(self.frame2)
		self.frame_in2 = tk.Frame(self.canvas)
		self.my_scrollbar = tk.Scrollbar(self.frame2, orient = "vertical", command = self.canvas.yview)
		self.canvas.configure(yscrollcommand = self.my_scrollbar.set)
		self.my_scrollbar.pack(side = "right", fill = "y")
		self.canvas.pack(side = "left")
		
		self.canvas.create_window((0, 0), window = self.frame_in2, anchor = 'nw')
		
		self.frame_in2.bind("<Configure>", self.my_canvas)
		
		self.path_label = tk.Label(self.frame1, text = "  Path  :   ").grid(row = 0, column = 0)
		self.entry = tk.Entry(self.frame1, textvariable = self.path, width = 50).grid(row = 0, column = 1)
		self.b = tk.Button(self.frame1, text = "Select", command = self.open_photo).grid(row = 0, column = 2)
	
	def my_canvas(self, event):
		self.canvas.configure(scrollregion = self.canvas.bbox("all"), width = 1000, height = 700)
	
	def open_photo(self):
		path_ = tkFileDialog.askdirectory()
		self.path.set(path_)
		col = 1
		row = 1
		
		for file_name in os.listdir(self.path.get()):
			global image, photo
			
			if file_name.endswith(".jpg"):
				self.image.insert(0, Image.open(os.path.join(self.path.get(), file_name)).resize((300, 200),
				                                                                                 Image.ANTIALIAS))
				self.photo.insert(0, ImageTk.PhotoImage(self.image[0]))
				if col == 1:
					c1 = tk.Checkbutton(self.frame_in2, text = file_name, image = self.photo[0], compound = 'top',
					                    onvalue = 1, offvalue = 0, variable = self.var_photo)
					c1.grid(row = row, column = 0, sticky = tk.W)
					c1.pack()
					col += 1
				elif col == 2:
					c2 = tk.Checkbutton(self.frame_in2, text = file_name, image = self.photo[0], compound = 'top',
					                    onvalue = 1, offvalue = 0, variable = self.var_photo)
					c2.grid(row = row, column = 1, sticky = tk.W)
					c2.pack()
					col += 1
				else:
					c2 = tk.Checkbutton(self.frame_in2, text = file_name, image = self.photo[0], compound = 'top',
					                    onvalue = 1, offvalue = 0, variable = self.var_photo)
					c2.grid(row = row, column = 2, sticky = tk.W)
					c2.pack()
					col -= 2
					row += 1


root = MainApplication()
root.mainloop()
