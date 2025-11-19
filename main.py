import tkinter as tk
from tkinter import messagebox
from FA_calculate import FA_kiszamol_osszeg, FA_mutat_veglegesitett
from FA_logic import FA_hozzaad_tetel, FA_torol_tetel, FA_veglegesit_rendeles

ETLAP = {
    "Levesek": ["Gulyásleves (1500 Ft)", "Paradicsomleves (900 Ft)", "Fokhagymakrémleves (1200 Ft)"],
    "Főételek": ["Rántott szelet (3200 Ft)", "Marhapörkölt galuskával (3500 Ft)", "Grillezett lazac (4800 Ft)"],
    "Desszertek": ["Palacsinta (1000 Ft)", "Somlói galuska (1400 Ft)", "Tiramisu (1600 Ft)"]
}

veglegesitett_rendelesek = []


class FA_RendelesApp:
    def __init__(self, master):
        self.master = master
        master.title("🍽️ Éttermi Rendelésfelvevő Demo")

        self.jelenlegi_asztal = tk.StringVar(master)
        self.jelenlegi_asztal.set("1")
        self.rendeles_lista = []

        self.epitsd_gui()
        self.etlap_elemek_hozzaadasa()

    def epitsd_gui(self):
        self.asztal_frame = tk.LabelFrame(self.master, text="Asztalszám")
        self.asztal_frame.pack(padx=10, pady=5, fill="x")

        asztal_label = tk.Label(self.asztal_frame, text="Válassz asztalt:")
        asztal_label.pack(side="left", padx=5, pady=5)

        asztalok = [str(i) for i in range(1, 11)]
        self.asztal_menu = tk.OptionMenu(self.asztal_frame, self.jelenlegi_asztal, *asztalok)
        self.asztal_menu.pack(side="left", padx=5, pady=5)

        self.etlap_frame = tk.LabelFrame(self.master, text="Étlap")
        self.etlap_frame.pack(padx=10, pady=5, fill="both", expand=True)

        self.kivalasztott_frame = tk.LabelFrame(self.master, text="Kiválasztott Ételek")
        self.kivalasztott_frame.pack(padx=10, pady=5, fill="both", expand=True)

        self.rendeles_listbox = tk.Listbox(self.kivalasztott_frame, height=8)
        self.rendeles_listbox.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        scrollbar = tk.Scrollbar(self.kivalasztott_frame, orient="vertical")
        scrollbar.config(command=self.rendeles_listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.rendeles_listbox.config(yscrollcommand=scrollbar.set)

        torles_gomb = tk.Button(self.kivalasztott_frame, text="Törlés a Rendelésből", command=self._torol_tetel_hivas)
        torles_gomb.pack(pady=5, padx=5)

        self.gombok_frame = tk.Frame(self.master)
        self.gombok_frame.pack(padx=10, pady=10, fill="x")

        veglegesites_gomb = tk.Button(self.gombok_frame, text="✅ Rendelés Véglegesítése",
                                      command=self._veglegesit_rendeles_hivas, bg="green", fg="white",
                                      font=("Arial", 10, "bold"))
        veglegesites_gomb.pack(side="right", padx=5)

        info_gomb = tk.Button(self.gombok_frame, text="ℹ️ Összes Rendelés", command=self._mutat_veglegesitett_hivas)
        info_gomb.pack(side="left", padx=5)

    def etlap_elemek_hozzaadasa(self):
        row = 0
        for kategoria, etelek in ETLAP.items():
            label = tk.Label(self.etlap_frame, text=f"--- {kategoria} ---", font=("Arial", 10, "bold"))
            label.grid(row=row, column=0, columnspan=2, pady=5, padx=5, sticky="w")
            row += 1

            for etel in etelek:
                gomb = tk.Button(self.etlap_frame, text=etel,
                                 command=lambda e=etel: self._hozzaad_rendeleshez_hivas(e))
                gomb.grid(row=row, column=0, columnspan=2, padx=5, pady=2, sticky="ew")
                row += 1

    def _hozzaad_rendeleshez_hivas(self, etel):
        self.rendeles_lista = FA_hozzaad_tetel(self.rendeles_lista, self.rendeles_listbox, etel)

    def _torol_tetel_hivas(self):
        self.rendeles_lista = FA_torol_tetel(self.rendeles_lista, self.rendeles_listbox)

    def _veglegesit_rendeles_hivas(self):
        global veglegesitett_rendelesek

        siker, uj_lista, uj_asztal = FA_veglegesit_rendeles(
            self.rendeles_lista,
            self.jelenlegi_asztal,
            self.rendeles_listbox,
            veglegesitett_rendelesek
        )

        if siker:
            self.rendeles_lista = uj_lista
            self.rendeles_listbox.delete(0, tk.END)
            self.jelenlegi_asztal.set(uj_asztal)

    def _mutat_veglegesitett_hivas(self):
        global veglegesitett_rendelesek
        FA_mutat_veglegesitett(self.master, veglegesitett_rendelesek)


if __name__ == "__main__":
    root = tk.Tk()
    app = FA_RendelesApp(root)
    root.mainloop()