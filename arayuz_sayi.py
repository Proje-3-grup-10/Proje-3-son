import tkinter as tk
from tkinter import messagebox
import ayarlar as opt

class SayiArayuzu:
    def __init__(self, pencere, motor, menu_don_fn):
        self.pencere = pencere
        self.motor = motor
        self.menu_don = menu_don_fn
        self.butonlar = []

        self.pencere.geometry(f"{opt.PENCERE_BOYUTU}x{opt.PENCERE_BOYUTU + 140}")
        self.pencere.config(bg=opt.RENK_ARKA_PLAN)
        self.butonlari_olustur()

    def butonlari_olustur(self):
        # Ana container
        ana_frame = tk.Frame(self.pencere, bg=opt.RENK_ARKA_PLAN)
        ana_frame.pack(expand=True, fill="both", padx=20, pady=20)

        # Başlık
        tk.Label(ana_frame, text="SAYI BULMACASI", font=opt.FONT_BASLIK,
                 fg=opt.RENK_BASLIK, bg=opt.RENK_ARKA_PLAN).pack(pady=15)

        # Puzzle çerçevesi (kart görünümü)
        grid_frame = tk.Frame(ana_frame, bg=opt.RENK_GRID_CERCEVE, bd=8, relief="ridge")
        grid_frame.pack(pady=10)

        for r in range(opt.BOYUT):
            satir_btns = []
            for c in range(opt.BOYUT):
                btn = tk.Button(grid_frame, relief="flat", borderwidth=0,
                                command=lambda r=r, c=c: self.tikla(r, c))
                btn.config(font=opt.FONT_SAYI, bg=opt.RENK_SAYI_ARKA,
                           fg=opt.RENK_SAYI_YAZI, activebackground="#22D3EE")
                btn.grid(row=r, column=c, padx=6, pady=6, ipadx=10, ipady=10)
                satir_btns.append(btn)
            self.butonlar.append(satir_btns)

        # Menüye Dön butonu
        tk.Button(ana_frame, text="← Menüye Dön", font=opt.FONT_BUTON,
                  bg=opt.RENK_VURGU, fg="black", activebackground="#67E8F9",
                  width=20, height=2, command=self.kapat).pack(pady=25)

        self.guncelle()

    def guncelle(self):
        for r in range(opt.BOYUT):
            for c in range(opt.BOYUT):
                deger = self.motor.tahta[r][c]
                if deger == 0:
                    self.butonlar[r][c].config(text="", bg=opt.RENK_SAYI_BOS)
                else:
                    self.butonlar[r][c].config(text=str(deger))

    def tikla(self, r, c):
        if self.motor.hareket_et(r, c):
            self.guncelle()
            if self.motor.kazandi_mi():
                messagebox.showinfo("🎉 Tebrikler!", "Sayıları başarıyla dizdiniz!")
                self.kapat()

    def kapat(self):
        for widget in self.pencere.winfo_children():
            widget.destroy()
        self.menu_don()
