import tkinter as tk

def main():
    aken = tk.Tk()
    aken.geometry("300x300")
    frame = tk.Frame(aken)
    frame.pack(pady=5, padx=5, fill="both")
    frame2 = tk.Frame(aken)
    frame2.pack(pady=5, padx=5, fill="both")
    frame3 = tk.Frame(aken)
    frame3.pack(pady=5, padx=5, fill="both")
    
    def kuva_sisestus():
        laenusumma = int(sisestus1).get()  
        kuuintressimäär = float(sisestus2).get()
        maksete_arv = int(sisestus3).get()
        igakuine_makse = laenusumma * kuuintressimäär / {1 + (1 + kuuintressimäär) ** maksete_arv}   
        vastus = tk.Label(aken, text=f"Igakuine makse: {maksete_arv:.2f}")
        #vastus.pack()

    label = tk.Label(aken, text="Laenusumma(€):").pack(pady=10)
    sisestus1 = tk.Entry(aken)
    sisestus1.pack(side="left", fill="x", expand=True)
    label = tk.Label(aken, text="kuuintressimäär(%):").pack(pady=10)
    sisestus2 = tk.Entry(aken)
    sisestus2.pack(side="left", fill="x", expand=True)
    label = tk.Label(aken, text="Laenuperiood(aastates):").pack(pady=10)
    sisestus3 = tk.Entry(aken)
    sisestus3.pack(side="left", fill="x", expand=True)
   
    nupp = tk.Button(aken, text="Vajuta mind", command=kuva_sisestus)
    nupp.pack()

    aken.mainloop()

if __name__ == "__main__":
    main()