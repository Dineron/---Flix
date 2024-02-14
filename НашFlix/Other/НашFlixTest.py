import tkinter as tk
from tkinter import PhotoImage
import os
from PIL import Image, ImageTk


w =1100
h = 600
photopath = "C:/Users/roma_/OneDrive/Рабочий стол/НашFlix/мультимедія/foto"
firstline = "C:/Users/roma_/OneDrive/Рабочий стол/НашFlix/мультимедія/foto/firstline"
secondline = "C:/Users/roma_/OneDrive/Рабочий стол/НашFlix/мультимедія/foto/secondline"

class MyGui(Frame):
	def __init__(self, parent=None):
		Frame.__init__(self, parent)
		page = page

		root = page1()

	def switchUp():
		app = page2()

class appl():
	def Init():
		global root
		root = tk.Tk()
		root.title("НашFlixTest")
		root.geometry(f"{w}x{h}")

		root.minsize(w, h)
		root.maxsize(w, h)

def Loop():
	root.mainloop()

def StR():
	global canvas
	canvas.create_rectangle(1100, 600, 0, 0, fill = "#8B0000", outline = "blue", width = 0)
	canvas.create_rectangle(100, 600, 0, 0, fill = "red", outline = "blue", width = 0)

def MenuButtons():
	global canvas

	canvas.create_rectangle(550, 560, 600, 585, fill = "#FFFFFF", outline = "blue", width = 0)
	lable = tk.Label(root, text = "page 3")
	lable.place(x =555, y = 562)

	bt1 = tk.Button(root, text = "Films")
	bt2 = tk.Button(root, text = "Cartoon")
	bt3 = tk.Button(root, text = "Series")

	r = tk.Button(root, text = ">>>>>>>", commands = MyGui.switchUp())
	#r['command'] = switchUp()
	l = tk.Button(root, text = "<<<<<<<")

	bt1.place(x= 10, y =20)
	bt2.place(x= 10, y =50)
	bt3.place(x= 10, y =80)

	r.place(x = 700, y = 560)
	l.place(x = 400, y = 560)

def firstline(xx, yy):
	cont = False
	Xx = xx
	for el in os.listdir("C:/Users/roma_/OneDrive/Рабочий стол/НашFlix/мультимедiя/foto/firstline"):
		print(el)
		path = f"C:/Users/roma_/OneDrive/Рабочий стол/НашFlix/мультимедiя/foto/firstline/{el}"
		savedpath = f"C:/Users/roma_/OneDrive/Рабочий стол/НашFlix/мультимедiя/foto/Fsaved/{el[:4]}-saved.png"
		Oimage = Image.open(path)
		Rimage = Oimage.resize((350, 300))
		Rimage.save(savedpath)
		photo = ImageTk.PhotoImage(file=savedpath)
		ButtonPhoto1 = tk.Button(root, image = photo, width=350, height = 300)
		ButtonPhoto1.image = photo
		ButtonPhoto1.place(x = xx, y = yy)
		xx += 450


appl.Init()

canvas = tk.Canvas(root, width = w, height = h)
canvas.pack()
StR()
MenuButtons()
firstline(150, 120)
#secondline(150)


Loop()