import tkinter as tk

def main():
    aken = tk.Tk()
    aken.geometry("300x300")

    
    def kuva_sisestus():
        tekst1 = sisestus1.get()  
        tekst2 = sisestus2.get()  
        vastus = tk.Label(aken, text=f"Esimene sisestus: {tekst1}, Teine sisestus: {tekst2}")
        vastus.pack()

    
    sisestus1 = tk.Entry(aken)
    sisestus1.pack()
   
    sisestus2 = tk.Entry(aken)
    sisestus2.pack()
   
    nupp = tk.Button(aken, text="Vajuta mind", command=kuva_sisestus)
    nupp.pack()

    aken.mainloop()

if __name__ == "__main__":
    main()