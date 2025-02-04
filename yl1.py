import tkinter as tk
import ctypes
from PIL import Image, ImageTK

def main():
    aken = tk.Tk()
    aken.title("Tkinter ülesanded")
    aken.geometry("400x400")
    aken.resizable(False, True)

    pilt = Image.open("norris.jpg")
    pilt = pilt.crop((0, 0, 200, 200))
    foto = ImageTK.PhotoImage(pilt)


    label = tk.Label(aken, text="Chuck Norris", font=("Arial", 16, "bold"), fg="blue").pack()    

    label = tk.Label(aken, image=foto)
    label.image = foto
    label.pack()