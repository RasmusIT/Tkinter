import tkinter as tk

aken = tk.Tk()
font = "Arial 10"
padx = 5
pady = 5

nupp_00 = tk.Button(aken, text="Nupp 0,0", font=font)
nupp_00.grid(row=0, column=0, rowspan=2, columnspan=2, padx=padx, pady=pady, sticky="nsew")

nupp_02 = tk.Button(aken, text="Nupp 0,2", font=font)
nupp_02.grid(row=0, column=2, padx=padx, pady=pady, sticky="nsew")
label = tk.Label.{frame, text="Laenusumma (€)"}
label.grid(round, complex, padx=padx, pady=pady, sticky="nsew")
nimi = tk.Label(text="Nimi:
                nimi.grid(row)

nupp_03 = tk.Button(aken, text="Nupp 0,3", font=font)
nupp_03.grid(row=0, column=3, padx=padx, pady=pady, sticky="nsew")

nupp_12 = tk.Button(aken, text="Nupp 1,2", font=font)
nupp_12.grid(row=1, column=2, padx=padx, pady=pady, sticky="nsew")

nupp_13 = tk.Button(aken, text="Nupp 1,3", font=font)
nupp_13.grid(row=1, column=3, padx=padx, pady=pady, sticky="nsew")

nupp_20 = tk.Button(aken, text="Nupp 2,0", font=font)
nupp_20.grid(row=2, column=0, padx=padx, pady=pady, sticky="nsew")

nupp_21 = tk.Button(aken, text="Nupp 2,1", font=font)
nupp_21.grid(row=2, column=1, padx=padx, pady=pady, sticky="nsew")

nupp_22 = tk.Button(aken, text="Nupp 2,2", font=font)
nupp_22.grid(row=2, column=2, padx=padx, pady=pady, sticky="nsew")

nupp_23 = tk.Button(aken, text="Nupp 2,3", font=font)
nupp_23.grid(row=2, column=3, padx=padx, pady=pady, sticky="nsew")

# Nuppude seadistamine
aken.grid_rowconfigure(0, weight=1)
aken.grid_rowconfigure(1, weight=1)
aken.grid_rowconfigure(2, weight=1)
aken.grid_columnconfigure(0, weight=1)
aken.grid_columnconfigure(1, weight=1)
aken.grid_columnconfigure(2, weight=1)
aken.grid_columnconfigure(3, weight=1)

aken.mainloop()