import tkinter as tk
from tkinter import messagebox


def FA_kiszamol_osszeg(etelek):
    osszeg = 0
    for etel in etelek:
        try:
            start = etel.rfind('(') + 1
            end = etel.rfind(' Ft')
            ar_str = etel[start:end]
            osszeg += int(ar_str)
        except Exception:
            pass
    return osszeg

def FA_mutat_veglegesitett(master, veglegesitett_rendelesek):
    if not veglegesitett_rendelesek:
        messagebox.showinfo("Összes Rendelés", "Még nem lett rendelés véglegesítve.")
        return

    osszesito = "--- Véglegesített Rendelések ---\n\n"
    teljes_bevetele = 0

    for rendeles in veglegesitett_rendelesek:
        etelek_listaja = "\n - ".join(rendeles["etelek"])

        osszesito += f"➡️ Asztal: **{rendeles['asztal']}**\n"
        osszesito += f"   Tételek:\n - {etelek_listaja}\n"
        osszesito += f"   **Összesen: {rendeles['osszeg']} Ft**\n"
        osszesito += f"🕓 Időpont: {rendeles['idopont']}\n"
        osszesito += "--------------------------------------\n"
        teljes_bevetele += rendeles['osszeg']

    osszesito += f"\n💰 **Összes bevétel:** {teljes_bevetele} Ft"

    top = tk.Toplevel(master)
    top.title("Összes Rendelés")

    szoveg_widget = tk.Text(top, height=20, width=60, wrap=tk.WORD)
    szoveg_widget.insert(tk.END, osszesito)
    szoveg_widget.config(state=tk.DISABLED)
    szoveg_widget.pack(padx=10, pady=10)