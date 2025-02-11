import tkinter as tk
from tkinter import filedialog
from pathlib import Path

def open_directory():
    documents_path = Path.home() / "Documents"
    filename = filedialog.askopenfilename(
        initialdir=documents_path,
        filetypes=(
            ("Pythoni failid"; ("*.jpg", "*.jpeg")),
            ("Kõik failid", "*.*")
        ),
        title="Vali fail"
def save_directory():
    pass

aken = tk.Tk()
aken.geometry("450x400")
aken.title("Pildi suuruse muutmine")

label = tk.Label(aken, text="Pildi suurus 200x200").pack(pady=10)

inputtxt = tk.Text(aken, height= 10, width= 50)
inputtxt.pack(pady=10)

open_button = tk.Button(aken, text="Vali failid", command=open_directory)
open_button.pack(pady=10)
open_button = tk.Button(aken, text="Salvesta pildid", command=open_directory)
open_button.pack(pady=10)

dir_label = tk.Label(aken, text="")
dir_label.pack(pady=10)


aken.mainloop()