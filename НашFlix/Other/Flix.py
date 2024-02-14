

import tkinter as tk
from tkinter import PhotoImage
import os
from PIL import Image, ImageTk
import pyautogui
import json

Page = 0

ButtonList = []

w = 1100
h = 600

SourcePath = "C:/Users/Bogdan/Desktop/мультимедiя"
MovieInfo = f"{SourcePath}/DataBase/MovieInfo.json"
photopath = f"{SourcePath}/foto"
firstline = f"{photopath}/firstline"
secondline = f"{photopath}/secondline"

fileNames = os.listdir(f"{SourcePath}/foto/firstline")

class app():
    def Init():
        global root
        root = tk.Tk()
        root.title("НашFlix")
        root.geometry(f"{w}x{h}")

        root.minsize(w, h)
        root.maxsize(w, h)

def show_popup(name, rate):
    global MovieInfo
    print(name)

    posX, posY = pyautogui.position()
    x, y = 300, 600
    popup = tk.Toplevel(root)
    popup.title("Grade")
    popup.geometry(f"{x}x{y}+{posX}+{posY}")
    popup.minsize(x ,y)
    popup.maxsize(x ,y)
    tk.Label(popup, text = str("Name: " + name)).place(x= 10, y= 10)
    tk.Label(popup, text = str("Rate: " + rate)).place(x= 10, y= 35)

    MOVIE_DESCRIPTION = ""

    with open(MovieInfo, "rb") as file:
        json_data = json.load(file)
    
    MOVIE_DESCRIPTION = json_data[name]

    EDIT_MOVIE_DESCRIPTION = ""
    CONTROLLER = 0 
    words = MOVIE_DESCRIPTION.split(" ")
    for el in words:
        CONTROLLER += 1
        if CONTROLLER > 3:
            EDIT_MOVIE_DESCRIPTION += "\n"
            CONTROLLER = 0
        if len(el) > 8:
            CONTROLLER += 2
        EDIT_MOVIE_DESCRIPTION += el + " "


    tk.Label(popup, text = str(EDIT_MOVIE_DESCRIPTION), justify="left").place(x= 10, y= 110)
    
    XPOS_STAR = 10
    YPOS_STAR = 55
    for el in range(0, int(rate.split(",")[0])):
        StarImagePath = "C:/Users/Bogdan/Desktop/мультимедiя/foto/More/Star.png"
        OIIMAGE = Image.open(StarImagePath)
        Rimage = OIIMAGE.resize((22, 20))
        Rimage.save(StarImagePath)
        IMG = ImageTk.PhotoImage(file= StarImagePath)
        label = tk.Label(popup, image = IMG)
        label.image = IMG
        label.place(x= XPOS_STAR, y= YPOS_STAR)
        XPOS_STAR += 22

        if XPOS_STAR > 136:
            XPOS_STAR = 10
            YPOS_STAR += 20

def PageController(value):
    global Page, fileNames
    print(len(fileNames))
    if Page + value > -1 and Page + value < len(fileNames):
       Page += value
       for el in ButtonList:
          el.destroy()
       firstline()

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

    bt1 = tk.Button(root, text = "Top level")
    bt2 = tk.Button(root, text = "Cartoon")
    bt3 = tk.Button(root, text = "Series")

    r = tk.Button(root, text = ">>>>>>>", command= lambda: PageController(6))
    l = tk.Button(root, text = "<<<<<<<", command= lambda: PageController(-6))

    bt1.place(x= 10, y =20)
    bt2.place(x= 10, y =50)
    bt3.place(x= 10, y =80)

    r.place(x = 700, y = 560)
    l.place(x = 400, y = 560)

def firstline():
    global SourcePath, photopath, ButtonList, fileNames
    Widht = 320
    controller = False
    Start_X = 150
    X_controller = 150
    Y_controller = 60
    
    for el in range(Page, len(fileNames)):
        path = f"{SourcePath}/foto/firstline/{fileNames[el]}"
        savedpath = f"{SourcePath}/foto/Fsaved/{fileNames[el][:4]}-saved.png"
        Oimage = Image.open(path)
        Rimage = Oimage.resize((120, 230))
        Rimage.save(savedpath)
        photo = ImageTk.PhotoImage(file=savedpath)

        
        ButtonPhoto1 = tk.Button(root, image = photo, width=120, height = 230, command= lambda el= el: show_popup(fileNames[el].split(".")[0].split("#")[1], fileNames[el].split(".")[0].split("#")[0]))
        ButtonPhoto1.image = photo
        ButtonPhoto1.place(x = X_controller, y = Y_controller)
        
        ButtonList.append(ButtonPhoto1)

        IMG = f"{photopath}/More/Shadow.png"

        X_controller += Widht

        if X_controller > 900 and controller == False:
            controller = True
            Y_controller = 300
            X_controller = Start_X
            

app.Init()

canvas = tk.Canvas(root, width = w, height = h)
canvas.pack()
StR()
MenuButtons()
firstline()


Loop()