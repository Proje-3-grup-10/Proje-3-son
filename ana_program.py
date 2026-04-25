import tkinter as tk
from motor import BulmacaMotoru
from arayuz_sayi import SayiArayuzu
from arayuz_resim import ResimArayuzu
import ayarlar as opt

class PuzzleUygulamasi:
    def __init__(self, root):
        self.root = root
        self.root.title("Puzzle Master")
        self.root.configure(bg=opt.RENK_ARKA_PLAN)
        self.root.geometry(f"{opt.PENCERE_BOYUTU}x{opt.PENCERE_BOYUTU + 100}")
        self.ana_menu()

    def ana_menu(self):
        # Önceki tüm widget'ları tamamen temizle
        for widget in self.root.winfo_children():
            widget.destroy()

        menu_frame = tk.Frame(self.root, bg=opt.RENK_ARKA_PLAN)
        menu_frame.pack(expand=True, fill="both")

        tk.Label(menu_frame, text="PUZZLE MASTER", font=opt.FONT_BASLIK,
                 fg=opt.RENK_BASLIK, bg=opt.RENK_ARKA_PLAN).pack(pady=50)

        tk.Button(menu_frame, text="Sayı Modu", font=opt.FONT_BUTON, width=24, height=2,
                  bg=opt.RENK_SAYI_ARKA, fg=opt.RENK_SAYI_YAZI,
                  activebackground="#22D3EE", command=self.sayi_baslat).pack(pady=15)

        tk.Button(menu_frame, text="Resim Modu", font=opt.FONT_BUTON, width=24, height=2,
                  bg=opt.RENK_SAYI_ARKA, fg=opt.RENK_SAYI_YAZI,
                  activebackground="#22D3EE", command=self.resim_baslat).pack(pady=15)

    def sayi_baslat(self):
        # Menüyü tamamen temizle
        for widget in self.root.winfo_children():
            widget.destroy()
        
        motor = BulmacaMotoru()
        motor.karistir()
        SayiArayuzu(self.root, motor, self.ana_menu)

    def resim_baslat(self):
        # Menüyü tamamen temizle
        for widget in self.root.winfo_children():
            widget.destroy()
        
        motor = BulmacaMotoru()
        motor.karistir()
        ResimArayuzu(self.root, motor, self.ana_menu)

if __name__ == "__main__":
    root = tk.Tk()
    app = PuzzleUygulamasi(root)
    root.mainloop()
