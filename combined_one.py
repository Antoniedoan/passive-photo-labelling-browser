# coding=utf-8
import os
import tkFileDialog
import Tkinter as Tk
import ttk
from PIL import Image, ImageTk


class MainApplication(Tk.Tk):
	image = photo = []
	
	def __init__(self):
		Tk.Tk.__init__(self)
		self.path = Tk.StringVar()
		
		self.title("Photo Labelling Software")
		# self.geometry("1000x800")
		# self.master.attributes('-zoom', True)
		self.attributes('-fullscreen', True)
		self.grid_rowconfigure(1, weight = 1)
		self.grid_columnconfigure(0, weight = 1)
		
		# image_frame holds the images and is within left_frame
		self.left_frame = Tk.Frame(self.master)
		self.image_frame = Tk.Frame(self.master)
		self.left_frame.grid(row = 0, sticky = "ew")
		self.image_frame.grid(row = 1, sticky = "nsew")
		
		self.canvas = Tk.Canvas(self.image_frame)
		self.frame_in2 = Tk.Frame(self.canvas)
		self.my_scrollbar = Tk.Scrollbar(self.image_frame, orient = "vertical", command = self.canvas.yview)
		self.canvas.configure(yscrollcommand = self.my_scrollbar.set)
		self.my_scrollbar.pack(side = "right", fill = "y")
		self.canvas.pack(side = "left")
		
		self.canvas.create_window((0, 0), window = self.frame_in2, anchor = 'nw')
		
		self.frame_in2.bind("<Configure>", self.my_canvas)
		
		self.path_label = Tk.Label(self.left_frame, text = "  Path  :   ").grid(row = 0, column = 0)
		self.entry = Tk.Entry(self.left_frame, textvariable = self.path, width = 50).grid(row = 0, column = 1)
		self.b = Tk.Button(self.left_frame, text = "Select", command = self.open_photo).grid(row = 0, column = 2)
		
		# right_frame is the frame that displays the tags
		self.right_frame = Tk.Frame(self.master)
		self.right_frame.grid(sticky= "ne", row = 1, column = 1)
		self.tag_labels = ttk.Notebook(self.right_frame)
		self.tag_labels.grid(sticky = "n")
		self.gen_tag_labels()
		
	def gen_tag_labels(self):
		general_tab = ttk.Frame(self.tag_labels)
		location_tab = ttk.Frame(self.tag_labels)
		activity_tab = ttk.Frame(self.tag_labels)
		thing_tab = ttk.Frame(self.tag_labels)
		
		self.tag_labels.add(general_tab, text = "General")
		self.tag_labels.add(location_tab, text = "Location")
		self.tag_labels.add(activity_tab, text = "Activity")
		self.tag_labels.add(thing_tab, text = "Things")
			
		cb_list = []
		# General Tab
		person = Tk.Checkbutton(general_tab, text = "Person")
		cb_list.append(person)
		useless = Tk.Checkbutton(general_tab, text = "Not Useful")
		cb_list.append(useless)
		
		# Location Tab
		home = Tk.Checkbutton(location_tab, text = "Home")
		cb_list.append(home)
		park = Tk.Checkbutton(location_tab, text = "Park")
		cb_list.append(park)
		market = Tk.Checkbutton(location_tab, text = "Supermarket / Wet Market")
		cb_list.append(market)
		hawker = Tk.Checkbutton(location_tab, text = "Food Court / Coffee Shop")
		cb_list.append(hawker)
		hospital = Tk.Checkbutton(location_tab, text = "Hospital")
		cb_list.append(hospital)
		common = Tk.Checkbutton(location_tab, text = "Playground / Void Deck")
		cb_list.append(common)
		religion = Tk.Checkbutton(location_tab, text = "Place of Worship")
		cb_list.append(religion)
		road = Tk.Checkbutton(location_tab, text = "On the Street")
		cb_list.append(road)
		bus_stop = Tk.Checkbutton(location_tab, text = "Bus Stop")
		cb_list.append(bus_stop)
		train_station = Tk.Checkbutton(location_tab, text = "MRT station")
		cb_list.append(train_station)
		
		# Activity Tab
		walk = Tk.Checkbutton(activity_tab, text = "Walking")
		cb_list.append(walk)
		cycle = Tk.Checkbutton(activity_tab, text = "Cycling")
		cb_list.append(cycle)
		sit = Tk.Checkbutton(activity_tab, text = "Sitting")
		cb_list.append(sit)
		talk = Tk.Checkbutton(activity_tab, text = "Chatting")
		cb_list.append(talk)
		eat = Tk.Checkbutton(activity_tab, text = "Eating")
		cb_list.append(eat)
		shop = Tk.Checkbutton(activity_tab, text = "Shopping")
		cb_list.append(shop)
		rest = Tk.Checkbutton(activity_tab, text = "Resting")
		cb_list.append(rest)
		others = Tk.Checkbutton(activity_tab, text = "Others")
		cb_list.append(others)
		
		for cb in cb_list:
			cb.grid(sticky = "w")

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
					c1 = Tk.Checkbutton(self.frame_in2, text = file_name, image = self.photo[0], compound = 'top',
					                    onvalue = 1, offvalue = 0)
					c1.grid(row = row, column = 0, sticky = Tk.W)
					# c1.pack()
					col += 1
				elif col == 2:
					c2 = Tk.Checkbutton(self.frame_in2, text = file_name, image = self.photo[0], compound = 'top',
					                    onvalue = 1, offvalue = 0)
					c2.grid(row = row, column = 1, sticky = Tk.W)
					# c2.pack()
					col += 1
				else:
					c2 = Tk.Checkbutton(self.frame_in2, text = file_name, image = self.photo[0], compound = 'top',
					                    onvalue = 1, offvalue = 0)
					c2.grid(row = row, column = 2, sticky = Tk.W)
					# c2.pack()
					col -= 2
					row += 1


root = MainApplication()
root.mainloop()

# remove images from the interface once already labelled
# one more tab for useless images
