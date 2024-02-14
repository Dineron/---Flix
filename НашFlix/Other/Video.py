import tkinter as tk
from PIL import Image, ImageTk
import imageio

Vwidth, Vheight = 600, 450
fps_interval = 1  # Збільште це значення для меншого FPS
speed_factor = 10  # Збільште це значення для прискорення відтворення

class VideoApp:
    def __init__(self, root, video_path):
        global Vwidth, Vheight
        self.root = root
        self.root.title("Video Player")

        self.video_path = video_path
        self.video = imageio.get_reader(video_path)

        print(self.video.get_meta_data())
        print(self.video.get_meta_data()['size'])

        self.canvas = tk.Canvas(root, width=Vwidth, height=Vheight)
        self.canvas.pack()

        self.play_video()

    def play_video(self):
        global Vwidth, Vheight
        try:
            frame = self.video.get_next_data()
            
            resized_frame = Image.fromarray(frame).resize((Vwidth, Vheight))
            
            self.photo = ImageTk.PhotoImage(image=resized_frame)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
            
            # Збільшення швидкості відтворення кадрів
            self.root.after(fps_interval, self.play_video)
        except StopIteration:
            pass

root = tk.Tk()
app = VideoApp(root, "C:/Users/roma_/Downloads/Rounded Red Lines Background video _ Footage _ Screensaver.mp4")
root.mainloop()