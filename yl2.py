import tkinter as tk
import ctypes
from PIL import Image, ImageTK

def loe_fail(failinimi):
    with open(failinimi, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    aken = tk.Tk()
    aken.title("Tkinter ülesanded")
    aken.geometry("200x200")
    aken.resizable(False, True)

    pilt = Image.open("norris.jpg")
    p = 0
    pilt = pilt.crop((0+p, 0+p, 200+p, 200+p))
    foto = ImageTK.PhotoImage(pilt)


    label = tk.Label(aken, text="Chuck Norris", font=("Arial", 16, "bold"), fg="blue").pack()    

    label = tk.Label(aken, image=foto)
    label.image = foto
    label.pack()

    tekst = tk.Text(aken, wrap=tk.WORD, font=("Arial", 12, "bold"))
    scrollbar = tk.Scrollbar(aken, command=tekst.yview)
    tekst.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tekst.pack(expand=True, fill=tk.BOTH)

    failisisu = loe_fail("norris.txt")
    tekst.insert(tk.INSERT, failisisu)
    
    aken.mainloop

    if __name__ == "__main__":
        main()