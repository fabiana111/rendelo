Fábián Ákos RYGR3E
Egy egyszerű éttermi rendelő alkalmazás ami a kézi jegyzetelést vagy pincért vált ki.
Ki lehet választani az adott asztalt, majd ezután a megadott ételekből a nekünk tetszőt.
A kiválasztott ételek bekerülnek a listába ahonnan véglegesítés előtt még van lehetőségünk szerkeszteni (többet hozzáadni, kitörölni).
A rendelés véglegesítése után az összes rendelés gombra kattintva megjelenik minden asztal rendelése, az összegek assztalonkénti szummázásával
és a rendelés leadásának idejével.
Ez után bármelyik másik asztalhoz felvehetünk bármilyen rendelést.
Használt modulok:
tkinter
 tk.Toplevel
 tk.Text
 tk.StringVar
 tk.LabelFrame
 tk.Label
 tk.OptionMenu
 tk.Listbox
 tk.Scrollbar
 tk.Button
 tk.Frame
 tk.Tk
    messagebox.showinfo
               shorerror
               showwarning
datetime
    datetime.now().strftime("%Y-%m-%d %H:%M:%S")

osztály FA_RendelesApp main.py-ben, főként megjelenítési logika
 epitsd_gui- alap felépítés
 etlap_elemek_hozzaadasa - kinézeti listához adás majd a lentebbi logic metódus hívás
FA_calculate.py (matematikai műveleteket tartalmaz)
 FA_mutat_veglegesitett - megmutatja új ablakban a véglegesített rendeléseket és azok tartalmát, végösszegét
 FA_kiszamol_osszeg - kiszámolja a teljes összeget bemeneti étellista alapján és visszatér az összeggel
FA_logic.py
 FA_hozzaad_tetel - hozzáadja a listához az adott ételt
 FA_torol_tetel - törli a listából a kiválasztott ételt
 FA_veglegesit_rendeles - a listában lévő tételeket az asztalhoz véglegesíti
