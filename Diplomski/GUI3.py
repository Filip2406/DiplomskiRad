from tkinter import *
import pandas as pd
from tkinter import ttk
from ttkthemes import ThemedStyle


df = pd.read_excel("autafinal3-CopyVerzija2.xlsx")
df["Cijena"] = df["Cijena"].astype(float)


def click():
    c = 0
    m = 0
    ukupna_cijena = 0
    prosjecna_cijena = 0
    brojac2 = 0
    unos4 = unos1.get()
    unos5 = unos2.get()
    unos6 = unos3.get()
    unos4=unos4.lower()
    unos5=unos5.lower()
    unos6=unos6.lower()
    space =" " in unos5
    if space:
        unos5=unos5.replace(" ","")
    
    if unos5 != "" and unos4 != "" and unos6 != "":
        for a in df["Model"]:
            space2=" " in a
            a=a.lower()
            if space2:
                a=a.replace(" ","")
            marka = df["Marka"][brojac2]
            marka=marka.lower()
            godiste = str(df["Godiste"][brojac2])
            b = df["Cijena"][brojac2]
            m = m + 1
            if a == unos5 and godiste == unos6 and marka == unos4:
                ukupna_cijena = b + ukupna_cijena
                c = c + 1
            brojac2 = brojac2 + 1
    if c > 0:
        prosjecna_cijena = ukupna_cijena / c
        prosjecna_cijena2 = str(int(prosjecna_cijena))
        l4.configure(text="Pronađena su sva vozila tražene kategorije: ")
        l5.configure(text="Marka: " + unos4.capitalize())
        l6.configure(text="Model: " + unos5.capitalize())
        l7.configure(text="Godište: " + unos6)
        l8.configure(text="Njihova prosječna cijena je: " +
                     prosjecna_cijena2 + "€")

        frame2.pack(pady=20)
        frame3.pack_forget()

    elif m == 0:
        l9.configure(text="Morate unijeti sve podatke")
        frame3.pack(pady=20)
        frame2.pack_forget()
    elif m > 0:
        l9.configure(
            text="Nije pronađen nijedan automobil sa ovako unesenim podacima")

        frame3.pack(pady=20)
        frame2.pack_forget()


root = Tk()
root.geometry("500x500+500+200")
root.title("Automobili")
root.config(bg="#6aa3b1")
tema=ThemedStyle(root)
# clam
# xpnative
# vista
tema.set_theme("xpnative")
root.minsize(width=700, height=650)
root.maxsize(width=1920, height=1080)
root.geometry("{}x{}+{}+{}".format(700, 650, int((root.winfo_screenwidth()-700)/2),
                            int((root.winfo_screenheight()-650)/2)))


frame = Frame(root)
frame.pack(pady=20)
frame.config(bg="#f5f5f5")


l10 = Label(frame, text="Molim Vas unesite sledeće podatke:", background="#f5f5f5", font=("Helvetica", 18))
l10.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

l1 = Label(frame, text="Marka:", background="#f5f5f5", font=("Helvetica", 18))
l1.grid(row=1, column=0, padx=10, pady=10)

l2 = Label(frame, text="Model:", background="#f5f5f5", font=("Helvetica", 18))
l2.grid(row=2, column=0, padx=10, pady=10)

l3 = Label(frame, text="Godište:",
           background="#f5f5f5", font=("Helvetica", 18))
l3.grid(row=3, column=0, padx=10, pady=10)

marka = []
for a in df["Marka"]:
    if a not in marka:
        marka.append(a)

unos1 = ttk.Combobox(frame, values=marka, font=("Helvetica", 16))
unos1.grid(row=1, column=1, padx=10, pady=10)

model = []
for a in df["Model"]:
    if a not in model:
        model.append(a)

unos2 = ttk.Combobox(frame, values=model, font=("Helvetica", 16))
unos2.grid(row=2, column=1, padx=10, pady=10)

godiste = []
for a in df["Godiste"]:
    if a not in godiste:
        godiste.append(a)
godiste.sort(reverse=True)
unos3 = ttk.Combobox(frame, values=godiste, font=("Helvetica", 16))
unos3.grid(row=3, column=1, padx=10, pady=10)

btn = Button(frame, text="Pronađi", font=("Helvetica", 18),  command=click)
btn.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

frame2 = Frame(root)
frame2.config(bg="#f5f5f5")


l4 = Label(frame2, text="", background="#f5f5f5", font=("Helvetica", 16))
l4.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

l5 = Label(frame2, text="", background="#f5f5f5", font=("Helvetica", 16))
l5.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

l6 = Label(frame2, text="", background="#f5f5f5", font=("Helvetica", 16))
l6.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

l7 = Label(frame2, text="", background="#f5f5f5", font=("Helvetica", 16))
l7.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

l8 = Label(frame2, text="", background="#f5f5f5", font=("Helvetica", 16))
l8.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

frame3 = Frame(root)
frame3.config(bg="#f5f5f5")

l9 = Label(frame3, text="", background="#f5f5f5", font=("Helvetica", 16))
l9.grid(row=10, column=0, columnspan=2, padx=10, pady=10)


root.mainloop()