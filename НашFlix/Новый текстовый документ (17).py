import tkinter as tk
from tkinter import PhotoImage
import os
from PIL import Image, ImageTk
import pyautogui
import webbrowser as web
from MovieInfo import data 
from TitleButtons import ButtonsData as Bd
import imageio

Page = 0
nP = 1

StartMenuEL = []

ActualCategory = []

TitleButtonsTrash = []
ButtonList = []

w = 1100
h = 600
SourcePath = "C:/Users/roma_/OneDrive/Рабочий стол/НашFlix/мультимедiя"
photopath = f"{SourcePath}/foto"
firstline = f"{photopath}/firstline"
secondline = f"{photopath}/secondline"

fileNames = os.listdir(f"{SourcePath}/foto/firstline")
#MovieInfo = f"C:/Users/roma_/OneDrive/Рабочий стол/НашFlix/MovieInfo.py"


fps_interval = 20 



class appl():
    #def Init():
        # global root
        # root = tk.Tk()
        # root.title("НашFlix")
        # root.geometry(f"{w}x{h}")

        # root.minsize(w, h)
        # root.maxsize(w, h)

    def Init(self, root, video_path1):
        global w, h
        self.root = root
        self.root.title("НашFlix")
        self.root.geometry(f"{w}x{h}")

        self.root.minsize(w, h)
        self.root.maxsize(w, h)


        self.video_path1 = video_path1
        self.video1 = imageio.get_reader(video_path1)

        #self.video_path2 = video_path2
        #self.video2 = imageio.get_reader(video_path2)

        print(self.video1.get_meta_data())
        print(self.video1.get_meta_data()['size'])

        self.canvas = tk.Canvas(root, width=w, height=h)
        self.canvas.create_rectangle(100, 600, 0, 0, fill = "black", outline = "blue", width = 0)
        self.canvas.pack()

        self.play_video()

    def play_video(self):
        global w, h
        try:
            frame1 = self.video1.get_next_data()
            #frame2 = self.video2.get_next_data()
            
            resized_frame1 = Image.fromarray(frame1).resize((w, h))
            #resized_frame2 = Image.fromarray(frame2).resize((w, h))
            
            self.photo1 = ImageTk.PhotoImage(image=resized_frame1)
            #self.photo2 = ImageTk.PhotoImage(image=resized_frame2)

            
            #self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo2)
            self.canvas.create_image(100, 0, anchor=tk.NW, image=self.photo1)
            
            self.root.after(fps_interval, self.play_video)

        except StopIteration:
            pass




def open_link(URL):
    try:
        web.open(URL)
    except Exception as e:
        print(e)

def DrowStartMenu():
    global root
    text = tk.Label(root, text = Bd[0]["S"]["Text"], fg= "white", background= "#121212", font=("Arial", 10, "bold"))
    text.place(x= 550, y= 300)
    StartMenuEL.append(text)

def RemoveStartMenu():
    for el in StartMenuEL:
        el.destroy()

def show_popup(name):
    #global MovieInfo
    posX, posY = pyautogui.position()
    if len(data[0][f"{name}"]["Trailer"]) < 5:
        x, y = 450, 500
    else:
        x, y = 450, 600
    popup = tk.Toplevel(root)
    popup.title("Grade")
    popup.geometry(f"{x}x{y}+{posX}+{posY}")
    popup.minsize(x ,y)
    popup.maxsize(x ,y)

    print(name)

    tk.Label(popup, text = str("Name: " + name), font=("Arial", 10, "bold")).place(x= 10, y= 10)
    tk.Label(popup, text = str("Mark: " + str(data[0][f"{name}"]["Mark"])), font=("Arial", 10, "bold")).place(x= 10, y= 35)

    #tk.Text(popup, text = str(data[0][f"{name}"]["Description"]), justify="left", wrap = "word").place(x= 10, y= 110)
    text_widget = tk.Text(popup, wrap="word", background="White", font=("Arial", 11, "bold"))
    text_widget.place(x=10,y=110, width= 430, height= 300)
    text_widget.insert("1.0", str(data[0][f"{name}"]["Description"]))

    text_widget2 = tk.Text(popup, wrap="word", background="White", font=("Arial", 11, "bold"))
    text_widget2.place(x=10 ,y=420, width= 430, height= 70)
    text_widget2.insert("1.0", str(data[0][f"{name}"]["Authors"]))


    path = f"{photopath}/More/Youtube.png"
    Oimage = Image.open(path)
    Rimage = Oimage.resize((130, 50))
    Rimage.save(path)
    photo = ImageTk.PhotoImage(file=path)

    bt1 = tk.Button(popup, text = "Trailer", image = photo, width=410, height= 65, command = lambda: URL(str(data[0][f"{name}"]["Trailer"])), background= "#C0C0C0")
    bt1.image = photo
    bt1.place(x= 20, y =510)

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
    global canvas
    canvas.create_rectangle(1100, 600, 0, 0, fill = "#121212", outline = "blue", width = 0)
    canvas.create_rectangle(100, 600, 0, 0, fill = "black", outline = "blue", width = 0)
    lable = tk.Label(root, width = 35, height= 2, bd=3, relief="solid")
    lable.place(x=100, y=10)

    path = f"{photopath}/More/Search.png"
    Oimage = Image.open(path)
    Rimage = Oimage.resize((22, 20))
    Rimage.save(path)
    photo = ImageTk.PhotoImage(file=path)
    Photo = tk.Label(root, image = photo, width=22, height = 20)
    Photo.image = photo
    Photo.place(x = 105, y = 16)

def MenuButtons():
    global canvas, nP
    lable = tk.Label(root, text = f"page {nP}")
    lable.place(x =555, y = 562)

    TitleButtonInit()

    r = tk.Button(root, text = ">>>>>>>", command= lambda: PageController(6))
    l = tk.Button(root, text = "<<<<<<<", command= lambda: PageController(-6))

    r.place(x = 700, y = 560)
    l.place(x = 400, y = 560)

def MarkButtonSelect(value):
    if Bd[0][str(value)]["Selected"] > 0:
        Bd[0][str(value)]["Selected"] = 0
        ActualCategory.remove(Bd[0][str(value)]["Name"])
    else:
        Bd[0][str(value)]["Selected"] = 1
        ActualCategory.append(Bd[0][str(value)]["Name"])
        print(ActualCategory)

    for el in TitleButtonsTrash:
        el.destroy()
    
    TitleButtonInit()
    DesroyAllMovie()
    firstline()


def TitleButtonInit():
    SelectedPosX, SelectedPosY = 145, 15
      
    X, Y = 10, 20
    for el in range(0, 3):
        if Bd[0][str(el)]["Selected"] > 0:
            b = tk.Button(root, text = Bd[0][str(el)]["Name"], font=("Arial", 10, "bold"), bd = 3, relief = "solid", command= lambda el= el: MarkButtonSelect(el))
            TitleButtonsTrash.append(b)
            b.place(x= SelectedPosX, y = SelectedPosY)
            SelectedPosX += int(Bd[0][str(el)]["CWidth"])
        else:
            b = tk.Button(root, text = Bd[0][str(el)]["Name"], font=("Arial", 10, "bold"), bd = 3, relief = "solid", command= lambda el= el: MarkButtonSelect(el))
            TitleButtonsTrash.append(b)
            b.place(x= X, y = Y)
            Y += 50
    if len(TitleButtonsTrash) == 0:
        DrowStartMenu()
            
def DesroyAllMovie():
    for el in ButtonList:
        el.destroy()


def firstline():
    global SourcePath, photopath, ButtonList, fileNames
    Widht = 320
    controller = False
    X_controller = 200
    Y_controller = 60
    
    for el in range(Page, len(fileNames)):     
        if data[0][fileNames[el].split(".")[0]]["Category"] in ActualCategory:
            RemoveStartMenu()
            path = f"{SourcePath}/foto/firstline/{fileNames[el]}"
            savedpath = f"{SourcePath}/foto/Fsaved/{fileNames[el][:4]}-saved.png"
            Oimage = Image.open(path)
            Rimage = Oimage.resize((150, 200))
            Rimage.save(savedpath)
            photo = ImageTk.PhotoImage(file=savedpath)
            ButtonMovie = tk.Button(root, image = photo, width=150, height = 200, command= lambda el= el: show_popup(fileNames[el].split(".")[0]))
            ButtonMovie.image = photo
            ButtonMovie.place(x = X_controller, y = Y_controller)

            ButtonList.append(ButtonMovie)

            IMG = f"{photopath}/More/Shadow.png"

            X_controller += Widht

            if X_controller > 900 and controller == False:
                controller = True
                Y_controller = 300
                X_controller = 200


V1 = f"{SourcePath}/Rounded Red Lines Background video _ Footage _ Screensaver.mp4" 
V2 = f"{SourcePath}/Rounded Neon Purple Lines Gradient Background video _ Footage _ Screensaver.mp4"
V3 = f"{SourcePath}/Cyberpunk Neon Digital Tunnel Background video _ Footage _ Screensaver.mp4"
V4 = f"{SourcePath}/Gradient Liquid Blue Shapes Animation Background video _ Footage _ Screensaver.mp4"

#preset1 = V1, V2
#preset2 = V2, V1
#preset3 = V2, V3
#preset4 = V3, V3

root = tk.Tk()
my_app = appl()
my_app.Init(root, V4)

canvas = tk.Canvas(root, width = w, height = h)
canvas.pack()
StR()
MenuButtons()

DrowStartMenu()


Loop()