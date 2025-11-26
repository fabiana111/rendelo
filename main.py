import tkinter as tk
from tkinter import messagebox
from FA_calculate import FA_kiszamol_osszeg, FA_mutat_veglegesitett
from FA_logic import FA_hozzaad_tetel, FA_torol_tetel, FA_veglegesit_rendeles

ETLAP = {
    "Levesek": ["Gulyásleves (1500 Ft)", "Paradicsomleves (900 Ft)", "Fokhagymakrémleves (1200 Ft)"],
    "Főételek": ["Rántott szelet (3200 Ft)", "Marhapörkölt galuskával (3500 Ft)", "Grillezett lazac (4800 Ft)"],
    "Desszertek": ["Palacsinta (1000 Ft)", "Somlói galuska (1400 Ft)", "Tiramisu (1600 Ft)"]
}

veglegesitettRendelesek = []


class FA_RendelesApp:
    def __init__(self, master):
        self.master = master
        master.title("🍽️ Éttermi Rendelésfelvevő Demo")

        self.jelenlegiAsztal = tk.StringVar(master)
        self.jelenlegiAsztal.set("1")
        self.rendelesLista = []

        self.epitsd_gui()
        self.etlap_elemek_hozzaadasa()

    def epitsd_gui(self):
        self.asztalFrame = tk.LabelFrame(self.master, text="Asztalszám")
        self.asztalFrame.pack(padx=10, pady=5, fill="x")

        asztalLabel = tk.Label(self.asztalFrame, text="Válassz asztalt:")
        asztalLabel.pack(side="left", padx=5, pady=5)

        asztalok = [str(i) for i in range(1, 11)]
        self.asztalMenu = tk.OptionMenu(self.asztalFrame, self.jelenlegiAsztal, *asztalok)
        self.asztalMenu.pack(side="left", padx=5, pady=5)

        self.etlapFrame = tk.LabelFrame(self.master, text="Étlap")
        self.etlapFrame.pack(padx=10, pady=5, fill="both", expand=True)

        self.kivalasztottFrame = tk.LabelFrame(self.master, text="Kiválasztott Ételek")
        self.kivalasztottFrame.pack(padx=10, pady=5, fill="both", expand=True)

        self.rendelesListbox = tk.Listbox(self.kivalasztottFrame, height=8)
        self.rendelesListbox.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        scrollbar = tk.Scrollbar(self.kivalasztottFrame, orient="vertical")
        scrollbar.config(command=self.rendelesListbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.rendelesListbox.config(yscrollcommand=scrollbar.set)

        torlesGomb = tk.Button(self.kivalasztottFrame, text="Törlés a Rendelésből", command=self._torol_tetel_hivas)
        torlesGomb.pack(pady=5, padx=5)

        self.gombokFrame = tk.Frame(self.master)
        self.gombokFrame.pack(padx=10, pady=10, fill="x")

        veglegesitesGomb = tk.Button(self.gombokFrame, text="✅ Rendelés Véglegesítése",
                                     command=self._veglegesit_rendeles_hivas, bg="green", fg="white",
                                     font=("Arial", 10, "bold"))
        veglegesitesGomb.pack(side="right", padx=5)

        infoGomb = tk.Button(self.gombokFrame, text="ℹ️ Összes Rendelés", command=self._mutat_veglegesitett_hivas)
        infoGomb.pack(side="left", padx=5)

    def etlap_elemek_hozzaadasa(self):
        row = 0
        for kategoria, etelek in ETLAP.items():
            label = tk.Label(self.etlapFrame, text=f"--- {kategoria} ---", font=("Arial", 10, "bold"))
            label.grid(row=row, column=0, columnspan=2, pady=5, padx=5, sticky="w")
            row += 1

            for etel in etelek:
                gomb = tk.Button(self.etlapFrame, text=etel,
                                 command=lambda e=etel: self._hozzaad_rendeleshez_hivas(e))
                gomb.grid(row=row, column=0, columnspan=2, padx=5, pady=2, sticky="ew")
                row += 1

    def _hozzaad_rendeleshez_hivas(self, etel):
        self.rendelesLista = FA_hozzaad_tetel(self.rendelesLista, self.rendelesListbox, etel)

    def _torol_tetel_hivas(self):
        self.rendelesLista = FA_torol_tetel(self.rendelesLista, self.rendelesListbox)

    def _veglegesit_rendeles_hivas(self):
        global veglegesitettRendelesek

        siker, ujLista, ujAsztal = FA_veglegesit_rendeles(
            self.rendelesLista,
            self.jelenlegiAsztal,
            self.rendelesListbox,
            veglegesitettRendelesek
        )

        if siker:
            self.rendelesLista = ujLista
            self.rendelesListbox.delete(0, tk.END)
            self.jelenlegiAsztal.set(ujAsztal)

    def _mutat_veglegesitett_hivas(self):
        global veglegesitettRendelesek
        FA_mutat_veglegesitett(self.master, veglegesitettRendelesek)


if __name__ == "__main__":
    root = tk.Tk()
    app = FA_RendelesApp(root)
    root.mainloop()