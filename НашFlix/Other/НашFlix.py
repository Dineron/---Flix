import tkinter as tk
from tkinter import PhotoImage
import os
from PIL import Image, ImageTk
import pyautogui
import webbrowser as web

from MovieInfo import data #MovieInfo.py В мене просто не вийшло прочитати звичайний json. Думаю це через OneDrive, але мені лінь перекидувати його в іншу папку ＜（＾－＾）＞


Page = 0
nP = 1

ButtonList = []

w = 1100
h = 600
SourcePath = "C:/Users/roma_/OneDrive/Рабочий стол/НашFlix/мультимедiя"
photopath = f"{SourcePath}/foto"
firstline = f"{photopath}/firstline"
secondline = f"{photopath}/secondline"

fileNames = os.listdir(f"{SourcePath}/foto/firstline")
MovieInfo = f"{SourcePath}/DataBase/MovieInfo.json"


class appl():
	def Init():
		global root
		root = tk.Tk()
		root.title("НашFlix")
		root.geometry(f"{w}x{h}")

		root.minsize(w, h)
		root.maxsize(w, h)

def URL(Link):
	try:
		web.open(Link)
	except Exception as e:
		print(e)

def show_popup(name):
	global MovieInfo
	print(name)

	posX, posY = pyautogui.position()
	x, y = 450, 600
	popup = tk.Toplevel(root)
	popup.title("Grade")
	popup.geometry(f"{x}x{y}+{posX}+{posY}")
	popup.minsize(x ,y)
	popup.maxsize(x ,y)
	tk.Label(popup, text = str("Name: " + name), font=("Arial", 10, "bold")).place(x= 10, y= 10)
	tk.Label(popup, text = str("Mark: " + str(data[0][f"{name}"]["Mark"])), font=("Arial", 10, "bold")).place(x= 10, y= 35)



	#tk.Text(popup, text = str(data[0][f"{name}"]["Description"]), justify="left", wrap = "word").place(x= 10, y= 110)
	text_widget = tk.Text(popup, wrap="word", background="White", font=("Arial", 11, "bold"))
	text_widget.place(x=10,y=110, width= 430, height = 350)
	text_widget.insert("1.0", str(data[0][f"{name}"]["Description"]))

	path = f"{photopath}/More/Youtube.png"
	Oimage = Image.open(path)
	Rimage = Oimage.resize((150, 70))
	Rimage.save(path)
	photo = ImageTk.PhotoImage(file=path)

	bt1 = tk.Button(popup, text = "Trailer", image = photo, width=410, height= 100, command = lambda: URL(str(data[0][f"{name}"]["Trailer"])), background= "#C0C0C0")
	bt1.image = photo
	bt1.place(x= 20, y =475)

	XPOS_STAR = 10
	YPOS_STAR = 55
	try:
		for el in range(0, int(data[0][f"{name}"]["Mark"])):
			StarImagePath = f"{photopath}/More/Star.png"
			OIIMAGE = Image.open(StarImagePath)
			Rimage = OIIMAGE.resize((22, 20))
			Rimage.save(StarImagePath)
			IMG = ImageTk.PhotoImage(file= StarImagePath)
			label = tk.Label(popup, image = IMG)
			label.image = IMG
			label.place(x= XPOS_STAR, y= YPOS_STAR)
			XPOS_STAR += 22

			if XPOS_STAR > 22*5:
				XPOS_STAR = 10
				YPOS_STAR += 20
	except ValueError:
		text_widget.place(x=10,y=70, width= 430)
		bt1.place(x= 20, y =455)

	text_widget.config(state="disabled")



def PageController(value):
	global Page, fileNames, nP
	print(len(fileNames))
	if Page + value > -1 and Page + value < len(fileNames):
		Page += value
		if value > 0:
			nP += 1
		else :
			nP -= 1


		lable = tk.Label(root, text = f"page {nP}")
		lable.place(x =555, y = 562)

		for el in ButtonList:
			el.destroy()
		firstline()



def Loop():
	root.mainloop()

def StR():
	global canvas, nP
	canvas.create_rectangle(0, 0, 1100, 600, fill = "#8B0000", outline = "blue", width = 0)
	canvas.create_rectangle(0, 0, 100, 600, fill = "red", outline = "blue", width = 0)

def MenuButtons(): #- щоб повернути як було, потрібно видалити табуляцію
	global canvas, nP

	canvas.create_rectangle(550, 560, 600, 585, fill = "#FFFFFF", outline = "blue", width = 0)
	lable = tk.Label(root, text = f"page {nP}")
	lable.place(x =555, y = 562)

	bt1 = tk.Button(root, text = "Films")#, command = lambda: Sort("Film"))
	bt2 = tk.Button(root, text = "Cartoons")#, command = lambda: Sort("Cartoon"))
	bt3 = tk.Button(root, text = "Serials")#, command = lambda: Sort("Serial"))

	r = tk.Button(root, text = ">>>>>>>", command= lambda: PageController(6))
	l = tk.Button(root, text = "<<<<<<<", command= lambda: PageController(-6))

	bt1.place(x= 10, y =20)
	bt2.place(x= 10, y =50)
	bt3.place(x= 10, y =80)

	r.place(x = 700, y = 560)
	l.place(x = 400, y = 560)


#def Sort(category):
	# global SourcePath, photopath, ButtonList, fileNames

	# StR()

	# Widht = 320
	# controller = False
	# X_controller = 200
	# Y_controller = 60
    
	# for el in range(Page, len(fileNames)):
	# 	name = fileNames[el].split(".")[0]
	# 	if str(data[0][f"{name}"]["Category"]) == category:
	# 		path = f"{SourcePath}/foto/firstline/{fileNames[el]}"
	# 		savedpath = f"{SourcePath}/foto/Fsaved/{fileNames[el][:4]}-saved.png"
	# 		Oimage = Image.open(path)
	# 		Rimage = Oimage.resize((150, 200))
	# 		Rimage.save(savedpath)
	# 		photo = ImageTk.PhotoImage(file=savedpath)
			
	# 		ButtonPhoto1 = tk.Button(root, image = photo, width=150, height = 200, command= lambda el= el: show_popup(fileNames[el].split(".")[0]))
	# 		ButtonPhoto1.image = photo
	# 		ButtonPhoto1.place(x = X_controller, y = Y_controller)
	        
	# 		ButtonList.append(ButtonPhoto1)

	# 		IMG = f"{photopath}/More/Shadow.png"

	# 		X_controller += Widht

	# 		if X_controller > 900 and controller == False:
	# 			controller = True
	# 			Y_controller = 300
	# 			X_controller = 200

def firstline():
	global SourcePath, photopath, ButtonList, fileNames

	Widht = 320
	controller = False
	X_controller = 200
	Y_controller = 60
    
	for el in range(Page, len(fileNames)):
		path = f"{SourcePath}/foto/firstline/{fileNames[el]}"
		savedpath = f"{SourcePath}/foto/Fsaved/{fileNames[el][:4]}-saved.png"
		Oimage = Image.open(path)
		Rimage = Oimage.resize((150, 200))
		Rimage.save(savedpath)
		photo = ImageTk.PhotoImage(file=savedpath)
		
		ButtonPhoto1 = tk.Button(root, image = photo, width=150, height = 200, command= lambda el= el: show_popup(fileNames[el].split(".")[0]))
		ButtonPhoto1.image = photo
		ButtonPhoto1.place(x = X_controller, y = Y_controller)
        
		ButtonList.append(ButtonPhoto1)

		IMG = f"{photopath}/More/Shadow.png"

		X_controller += Widht

		if X_controller > 900 and controller == False:
			controller = True
			Y_controller = 300
			X_controller = 200
			

appl.Init()

canvas = tk.Canvas(root, width = w, height = h)
canvas.pack()
StR()
MenuButtons()
firstline()


Loop()