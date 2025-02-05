
import tkinter as tk

def kuva_varv(v):
    print(v)


def main():
    aken = tk.Tk()
    aken.geometry("300x400")
    aken.title("värvi nupud")
    nupp1 = tk.Button(aken, text="Vajuta mind", bg="red", fg="red", font=("Arial", 16), command=kuva_varv("red"))
    nupp2 = tk.Button(aken, text="Vajuta mind", bg="orange", fg="orange", font=("Arial", 16), command=kuva_varv("orange"))
    nupp3 = tk.Button(aken, text="Vajuta mind", bg="yellow", fg="yellow", font=("Arial", 16), command=kuva_varv("yellow"))
    nupp4 = tk.Button(aken, text="Vajuta mind", bg="green", fg="green", font=("Arial", 16), command=kuva_varv("green"))
    nupp5 = tk.Button(aken, text="Vajuta mind", bg="blue", fg="blue", font=("Arial", 16), command=kuva_varv("blue"))
    vastus = tk.Label(aken, text=f"Siia tuleb vastus")
    vastus.pack(side="bottom", expand=True, fill="y")
    nupp1.pack(side="left", expand=True, fill="y")
    nupp2.pack(side="left", expand=True, fill="y")
    nupp3.pack(side="left", expand=True, fill="y")
    nupp4.pack(side="left", expand=True, fill="y")
    nupp5.pack(side="left", expand=True, fill="y")

    aken.mainloop()

if __name__ == "__main__":
    main()