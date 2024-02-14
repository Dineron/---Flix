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

entry = None

NameTrashContainer = None
HitsContainer = []
TrashMenuButtons = []
TrashPopup = []
StartMenuEL = []
ActualCategory = []
TitleButtonsTrash = []
ButtonList = []

EntryAcualText = ""

w = 1100
h = 600
dirpath = os.getcwd()
SourcePath = f"{dirpath}/мультимедiя"
photopath = f"{SourcePath}/foto"
firstline = f"{photopath}/firstline"
secondline = f"{photopath}/secondline"

fileNames = os.listdir(f"{SourcePath}/foto/firstline")
#MovieInfo = f"C:/Users/roma_/OneDrive/Рабочий стол/НашFlix/MovieInfo.py"


fps_interval = 60



class appl():
    def Init(self, root, video_path1):
        global w, h
        self.root = root
        self.root.title("НашFlix")

        icoPath = f"{photopath}/More/Icon.ico"
        self.root.iconbitmap(f"{icoPath}")

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
    text.place(x= 475, y= 300)
    bt =  tk.Button(root, text = "Показати всі фільми", fg= "white", background= "#121212", font=("Arial", 10, "bold"), command = showall)
    bt.place(x= 475, y= 330)
    StartMenuEL.append(text)
    StartMenuEL.append(bt)

def showall():
    for el in range(0, 3):
        MarkButtonSelect(el)


def RemoveStartMenu():
    for el in StartMenuEL:
        el.destroy()

def show_popup(name):
    global TrashPopup
    posX, posY = pyautogui.position()
    print(posY)
    if len(data[0][f"{name}"]["Trailer"]) < 5:
        x, y = 450, 500
    else:
        x, y = 450, 600
    popup = tk.Toplevel(root)

    for el in TrashPopup:
        el.destroy()
    TrashPopup.append(popup)
    popup.title("Grade")

    if posY > 496:
        posY = 496

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
    Sum = 0

    for el in range(Page, len(fileNames)):     
        if data[0][fileNames[el].split(".")[0]]["Category"] in ActualCategory and Check(EntryAcualText, fileNames[el].split(".")[0]) == True:
            Sum+=1

    print(len(fileNames))
    if Page + value > -1 and Page + value < Sum:
        Page += value
        if value > 0:
            nP += 1
        else :
            nP -= 1

        lable = tk.Label(root, text = f"  page {nP}  ", font=("Arial", 11, "bold"), bd = 3, relief = "solid")
        lable.place(x =555, y = 564)

        for el in ButtonList:
            el.destroy()
        firstline()


def ClearEntry(entry):
    global EntryAcualText
    entry.delete(0, tk.END)
    EntryAcualText = ""
    destroyHints()
    firstline()



def Serch(entry):
    DesroyAllMovie()
    global EntryAcualText
    EntryAcualText = entry.get()
    entry.delete(0, tk.END)
    firstline()
    EntryAcualText = ""
    destroyHints()



def StR():
    global canvas, entry
    canvas.create_rectangle(1100, 600, 0, 0, fill = "#121212", outline = "blue", width = 0)
    canvas.create_rectangle(100, 600, 0, 0, fill = "black", outline = "blue", width = 0)
    # lable = tk.Label(root, width = 35, height= 2, bd=3, relief="solid")
    # lable.place(x=450, y=10)
    
    entry = tk.Entry(root,  font=('Arial', 14), width= 15)
    entry.place(x = 470, y = 16)

    entry.bind("<KeyRelease>", EntryHits)

    path = f"{photopath}/More/Search.png"
    Oimage = Image.open(path)
    Rimage = Oimage.resize((22, 20))
    Rimage.save(path)
    photo = ImageTk.PhotoImage(file=path)
    Photo = tk.Button(root, image = photo, width=22, height = 20, bd =2, command= lambda: Serch(entry))
    Photo.image = photo
    Photo.place(x =639, y = 16)

    tk.Button(root, text= "X", width=2, height = 1, font=("Arial", 10, "bold"), bd= 0, command= lambda: ClearEntry(entry)).place(x = 446, y = 17)

    # entry = tk.Entry(root)
    # entry.place(x = 470, y = 16)


def HitsTap(text):
    global entry, EntryAcualText, ActualCategory
    print(text)

    DesroyAllMovie()
    EntryAcualText = text
    entry.delete(0, tk.END)
    firstline()
    EntryAcualText = ""
    destroyHints()

def EntryHits(event):
    global entry, canvas, fileNames, HitsContainer, EntryAcualText
    print(event.keysym)
    EntryAcualText = entry.get()

    destroyHints()
    y_pos = 40
    for el in range(0, len(fileNames)):
        if Check(EntryAcualText, fileNames[el].split(".")[0]) == True:
            text = fileNames[el].split(".")[0]

            button = tk.Button(root, text = text, width=24, height = 1, anchor= "w", justify= tk.LEFT, borderwidth= 0, highlightthickness= 0, command= lambda el=el: HitsTap(fileNames[el].split(".")[0]))
            print(fileNames[el].split(".")[0])
            button.place(x= 470, y= y_pos)
            HitsContainer.append(button)
            y_pos += 29


def destroyHints():
    global HitsContainer, EntryAcualText
    print(1)
    
    for el in HitsContainer:
        el.destroy()


def MenuButtons(value):
    global canvas, nP, TrashMenuButtons
    lable = tk.Label(root, text = f"  page {nP}  ", font=("Arial", 11, "bold"), bd = 3, relief = "solid")
    lable.place(x =555, y = 564)

    r = tk.Button(root, text = "  >>>>>>>  ", font=("Arial", 11, "bold"), bd = 2, relief = "solid", command= lambda: PageController(8))
    l = tk.Button(root, text = "  <<<<<<<  ", font=("Arial", 11, "bold"), bd = 2, relief = "solid", command= lambda: PageController(-8))

    TrashMenuButtons.append(r)
    TrashMenuButtons.append(l)

    TrashMenuButtons.append(lable)
    r.place(x = 700, y = 560)
    l.place(x = 400, y = 560)

    if value == False:
        for el in TrashMenuButtons:
            el.destroy()


def MarkButtonSelect(value):
    global entry
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
    ClearEntry(entry)


def TitleButtonInit():
    SelectedPosX, SelectedPosY = 145, 15
      
    Sum = 0

    X, Y = 10, 20
    for el in range(0, 3):
        if Bd[0][str(el)]["Selected"] > 0:
            b = tk.Button(root, text = Bd[0][str(el)]["Name"], font=("Arial", 10, "bold"), bd = 3, relief = "solid",   command= lambda el= el: MarkButtonSelect(el))
            TitleButtonsTrash.append(b)
            b.place(x= SelectedPosX, y = SelectedPosY)
            SelectedPosX += int(Bd[0][str(el)]["CWidth"])
            Sum += 1
        else:
            b = tk.Button(root, text = Bd[0][str(el)]["Name"], font=("Arial", 10, "bold"), bd = 3, relief = "solid",  command= lambda el= el: MarkButtonSelect(el))
            TitleButtonsTrash.append(b)
            b.place(x= X, y = Y)

            Y += 50

    if Sum == 0:
        MenuButtons(False)
        DrowStartMenu()
    elif Sum > 0:
        RemoveStartMenu()
        MenuButtons(True)
    if len(TitleButtonsTrash) == 0:
        DrowStartMenu()



def DesroyAllMovie():
    for el in ButtonList:
        el.destroy()

def Check(EntryAcualText, file_name):
    Sum = 0
    for el in range(0, len(EntryAcualText)):
        try:
            if file_name[el].lower() == EntryAcualText[el].lower():
                Sum += 1
        except Exception as e:
            print(e)

    if Sum == len(EntryAcualText):
        return True
    else:
        return False

def NameShow(event, Name):
    global NameTrashContainer

    lable = tk.Label(root, text= f"{Name}", relief="solid",  highlightbackground="blue", highlightcolor="red", highlightthickness=1, background="black", fg ="white", font=("Arial", 10, "bold"))
    lable.place(x=event.x_root - root.winfo_rootx(), y=event.y_root - root.winfo_rooty() - 30)

    if NameTrashContainer != None:
        NameTrashContainer.destroy()

    NameTrashContainer = lable

def NameRemove(event):
    global NameTrashContainer

    if NameTrashContainer != None:
        root.after(300, NameTrashContainer.destroy())

def firstline():
    global SourcePath, photopath, ButtonList, fileNames, EntryAcualText
    Widht = 200
    controller = False
    X_controller = 200
    Y_controller = 60

    limit = 0
    
    for el in range(Page, len(fileNames)):     
        if data[0][fileNames[el].split(".")[0]]["Category"] in ActualCategory and Check(EntryAcualText, fileNames[el].split(".")[0]) == True:
            limit += 1

            RemoveStartMenu()
            path = f"{SourcePath}/foto/firstline/{fileNames[el]}"
            savedpath = f"{SourcePath}/foto/Fsaved/{fileNames[el][4:]}-saved.png"
            Oimage = Image.open(path)
            Rimage = Oimage.resize((150, 200))
            Rimage.save(savedpath)
            photo = ImageTk.PhotoImage(file=savedpath)

            if limit <= 8:
                ButtonMovie = tk.Button(root, image = photo, borderwidth= 0, highlightthickness= 0,width=150, height = 200, command= lambda el= el: show_popup(fileNames[el].split(".")[0]))
                ButtonMovie.image = photo
                ButtonMovie.place(x = X_controller, y = Y_controller)
                ButtonMovie.bind("<Motion>", lambda event, el= el: NameShow(event, fileNames[el].split(".")[0]))
                ButtonMovie.bind("<Leave>", NameRemove)
  
            ButtonList.append(ButtonMovie)

            IMG = f"{photopath}/More/Shadow.png"

            X_controller += Widht
            
            if X_controller > 900 and controller == False:

                controller = True
                Y_controller = 300
                X_controller = 200



def Logo():
    global canvas, h, w

    path = f"{photopath}/More/Logo.png"
    Oimage = Image.open(path)
    Rimage = Oimage.resize((w, h))
    Rimage.save(path)
    photo = ImageTk.PhotoImage(file=path)
    Photo = tk.Label(root, image = photo, width= w, height = h)
    Photo.image = photo
    Photo.place(x = 0, y = 0)

    root.after(3000, lambda: Photo.destroy())


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

path1 = f"{photopath}/More/Logo1.png"
Oimage1 = Image.open(path1)
Rimage1 = Oimage1.resize((90, 80))
Rimage1.save(path1)
photo1 = ImageTk.PhotoImage(file=path1)
Photo1 = tk.Label(root, image = photo1, relief="solid", width= 90, height = 80)
Photo1.image = photo1
Photo1.place(x = 5, y = 515)



DrowStartMenu()
TitleButtonInit()
Logo()


root.mainloop()