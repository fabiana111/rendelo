import tkinter as tk
from tkinter import messagebox
from FA_calculate import FA_kiszamol_osszeg
from datetime import datetime


def FA_hozzaad_tetel(rendeles_lista, rendeles_listbox, etel):
    rendeles_lista.append(etel)
    rendeles_listbox.insert(tk.END, etel)
    rendeles_listbox.itemconfig(tk.END, {'bg': 'lightblue'})
    return rendeles_lista


def FA_torol_tetel(rendeles_lista, rendeles_listbox):
    try:
        kivalasztott_index = rendeles_listbox.curselection()[0]
        tetel_neve = rendeles_listbox.get(kivalasztott_index)
        rendeles_listbox.delete(kivalasztott_index)

        if tetel_neve in rendeles_lista:
            rendeles_lista.remove(tetel_neve)
        return rendeles_lista

    except IndexError:
        messagebox.showwarning("Figyelem", "Kérlek, válassz ki egy tételt a törléshez!")
        return rendeles_lista


def FA_veglegesit_rendeles(rendeles_lista, jelenlegi_asztal, rendeles_listbox, veglegesitett_rendelesek):
    asztal = jelenlegi_asztal.get()
    rendelt_etelek = rendeles_lista.copy()

    if not rendelt_etelek:
        messagebox.showerror("Hiba", f"A {asztal}. asztalhoz nem lett étel kiválasztva!")
        return False, [], "1"

    osszeg = FA_kiszamol_osszeg(rendelt_etelek)

    rendeles_objektum = {
        "asztal": asztal,
        "etelek": rendelt_etelek,
        "osszeg": osszeg,
        "idopont": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    veglegesitett_rendelesek.append(rendeles_objektum)

    messagebox.showinfo("Rendelés Lezárva",
                        f"A rendelés a {asztal}. asztalhoz sikeresen lezárva!\nÖsszeg: {osszeg} Ft")

    return True, [], "1"