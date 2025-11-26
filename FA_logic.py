import tkinter as tk
from tkinter import messagebox
from FA_calculate import FA_kiszamol_osszeg
from datetime import datetime


def FA_hozzaad_tetel(rendelesLista, rendelesListbox, etel):
    rendelesLista.append(etel)
    rendelesListbox.insert(tk.END, etel)
    rendelesListbox.itemconfig(tk.END, {'bg': 'lightblue'})
    return rendelesLista


def FA_torol_tetel(rendelesLista, rendelesListbox):
    try:
        kivalasztottIndex = rendelesListbox.curselection()[0]
        tetelNeve = rendelesListbox.get(kivalasztottIndex)
        rendelesListbox.delete(kivalasztottIndex)

        if tetelNeve in rendelesLista:
            rendelesLista.remove(tetelNeve)
        return rendelesLista

    except IndexError:
        messagebox.showwarning("Figyelem", "Kérlek, válassz ki egy tételt a törléshez!")
        return rendelesLista


def FA_veglegesit_rendeles(rendelesLista, jelenlegiAsztal, rendelesListbox, veglegesitettRendelesek):
    asztal = jelenlegiAsztal.get()
    rendeltRtelek = rendelesLista.copy()

    if not rendeltRtelek:
        messagebox.showerror("Hiba", f"A {asztal}. asztalhoz nem lett étel kiválasztva!")
        return False, [], "1"

    osszeg = FA_kiszamol_osszeg(rendeltRtelek)

    rendelesObjektum = {
        "asztal": asztal,
        "etelek": rendeltRtelek,
        "osszeg": osszeg,
        "idopont": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    veglegesitettRendelesek.append(rendelesObjektum)

    messagebox.showinfo("Rendelés Lezárva",
                        f"A rendelés a {asztal}. asztalhoz sikeresen lezárva!\nÖsszeg: {osszeg} Ft")

    return True, [], "1"