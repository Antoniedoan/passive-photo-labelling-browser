#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 09:24:55 2018

@author: doanthanh
"""

from Tkinter import *
import Tkinter as tk
import ttk
from PIL import ImageTk, Image
import tkFileDialog
import os


class Application:
    def __init__(self, master):
        
        #create regions for the main frame
        self.leftFrame = Frame(master)
        self.leftFrame.grid(sticky=W+N, row=0, column=0, rowspan=30, columnspan=110)
        self.rightFrame = Frame(master)
        self.rightFrame.grid(sticky=E+N, row=0, column=111, rowspan=30, columnspan=10)
        
        master.grid_columnconfigure(1, weight=1)
        master.grid_rowconfigure(3, weight=1)
        master.minsize(width=700, height=260)
        #master.columnconfigure(3, pad=7)
        #master.rowconfigure(3, pad=7)  
        
        ToolBar = Frame(self.leftFrame, relief=GROOVE, bg="blue")
        
        #Toolbar, #insert your functions in command to for events
        self.openFile = Button(ToolBar, text="Open File", height=2, width=7, command=self.openPhoto) 
        self.openFile.grid(sticky=W+N, row=0, column=0, rowspan=2, columnspan=2)
        
        self.saveImgs = Button(ToolBar, text="Save", height=2, width=7, command=self.doNothing)
        self.saveImgs.grid(sticky=W+N, row=0, column=7, rowspan=2, columnspan=2)
        
        ToolBar.grid(sticky=W+N, row=0, column=0, rowspan=2, columnspan=10, padx=5, pady=5)
        #ImgHolders
        
        #self.var_photo = tk.IntVar()
        self.path = tk.StringVar()
		
        self.canvas = tk.Canvas(self.leftFrame)
        self.frame_in2 = tk.Frame(self.canvas)
        self.my_scrollbar = tk.Scrollbar(self.leftFrame, orient = "vertical", command = self.canvas.yview)
        self.canvas.configure(yscrollcommand = self.my_scrollbar.set)
        self.my_scrollbar.grid(row = 4,rowspan=30, columnspan=110, sticky = "ens")
        self.canvas.grid(row = 4,rowspan=30, columnspan=110, sticky = "nsew")
		
        self.canvas.create_window((0, 0), window = self.frame_in2, anchor = 'nw')
		
        self.frame_in2.bind("<Configure>", self.myCanvas)
		
        self.path_label = tk.Label(self.leftFrame, text = "  Path  :   ").grid(row = 3, column = 0)
        self.entry = tk.Entry(self.leftFrame, textvariable = self.path, width = 50).grid(row = 3, column = 1)
        
        TagLabels = ttk.Notebook(self.rightFrame)
        TagLabels.grid(sticky=N+E+S, row=0, column=11, rowspan=30, columnspan=20)
        #TagLabels
        generalTab = ttk.Frame(TagLabels)
        envTab =  ttk.Frame(TagLabels)
        activityTab =  ttk.Frame(TagLabels)
        thingTab =  ttk.Frame(TagLabels)
        addTab = ttk.Frame(TagLabels)
        
        TagLabels.add(generalTab, text="General")
        TagLabels.add(envTab, text="Location")
        TagLabels.add(activityTab, text="Activity")
        TagLabels.add(thingTab, text="Things")
        
        
        #General Tab
        person = Checkbutton(generalTab, text="Person")
        person.grid(sticky=W)
        useless = Checkbutton(generalTab, text="Not useful")
        useless.grid(sticky=W)
        
        #Locations tab
        home = Checkbutton(envTab, text="House")
        park = Checkbutton(envTab, text="Park")
        market = Checkbutton(envTab, text="Supermarket/Wet market")
        foodstore = Checkbutton(envTab, text="Food center/Coffeeshop")
        hospital = Checkbutton(envTab, text="Hospital")
        common = Checkbutton(envTab, text="Playground/Void Deck")
        religion = Checkbutton(envTab, text="Religious Venue")
        road = Checkbutton(envTab, text="On Road/Street")
        busstop = Checkbutton(envTab, text="Bus Stop")
        mrtstation = Checkbutton(envTab, text="MRT station")
        
        home.grid(sticky=W)
        park.grid(sticky=W)
        market.grid(sticky=W)
        foodstore.grid(sticky=W)
        hospital.grid(sticky=W)
        common.grid(sticky=W)
        religion.grid(sticky=W)
        road.grid(sticky=W)
        busstop.grid(sticky=W)
        mrtstation.grid(sticky=W)
        
        #activity
        
        walk = Checkbutton(activityTab, text="Walking")
        cycle = Checkbutton(activityTab, text="Cycling")
        sit = Checkbutton(activityTab, text="Sitting")
        talk = Checkbutton(activityTab, text="Chatting")
        eat = Checkbutton(activityTab, text="Eating")
        shop = Checkbutton(activityTab, text="Shopping")
        rest = Checkbutton(activityTab, text="Resting")
        others = Checkbutton(activityTab, text="Others")
        
        walk.grid(sticky=W)
        cycle.grid(sticky=W)
        sit.grid(sticky=W)
        talk.grid(sticky=W)
        eat.grid(sticky=W)
        shop.grid(sticky=W)
        rest.grid(sticky=W)
        others.grid(sticky=W)
        
    def doNothing(self):
        print("Huat Ah!")
        
    def myCanvas(event):
        canvas.config(scrollregion=canvas.bbox("all"),width=1100,height=900)
        
    def openPhoto(self):
        path_ = tkFileDialog.askdirectory()
        path.set(path_)
        col = 1
        row = 1
        
        for file in os.listdir(path.get()):
            global image,photo
            if file.endswith(".jpg"):
                image.insert(0,Image.open(path.get()+"/"+file).resize((300, 200), Image.ANTIALIAS))
                photo.insert(0,ImageTk.PhotoImage(image[0]))
                if col == 1:
                    C1=tk.Checkbutton(self.frame_in2, text=file, image = photo[0], \
                        compound='top', onvalue = 1, offvalue = 0)
                    C1.grid(row = row, column = 0, sticky=tk.W)
                    col+=1
                elif col == 2:
                    C2=tk.Checkbutton(self.frame_in2, text=file, image = photo[0], \
                        compound='top', onvalue = 1, offvalue = 0)
                    C2.grid(row = row, column = 1, sticky=tk.W)
                    col+=1
                else:
                    C2=tk.Checkbutton(self.frame_in2, text=file, image = photo[0], \
                        compound='top', onvalue = 1, offvalue = 0)
                    C2.grid(row = row, column = 2, sticky=tk.W)
                    col-=2
                    row+=1

root = tk.Tk()
app = Application(root)
root.title("Image Labeling Software")
root.geometry('1000x800')
root.mainloop()