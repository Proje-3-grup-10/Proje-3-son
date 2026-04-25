import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageOps
import ayarlar as opt

class ResimArayuzu:
    def __init__(self, pencere, motor, menu_don_fn):
        self.pencere = pencere
        self.motor = motor
        self.menu_don = menu_don_fn
        self.parcalar = {}
        self.son_parca_gorseli = None
        self.bos_gorsel = None
        self.butonlar = []

        self.pencere.geometry(f"{opt.PENCERE_BOYUTU}x{opt.PENCERE_BOYUTU + 140}")
        self.pencere.config(bg=opt.RENK_ARKA_PLAN)

        if self.resim_sec_ve_hazirla():
            self.butonlari_olustur()
        else:
            self.menu_don()

    def resim_sec_ve_hazirla(self):
        yol = filedialog.askopenfilename(filetypes=[("Resim Dosyaları", "*.jpg *.png *.jpeg")])
        if not yol:
            return False

        img_orjinal = Image.open(yol)
        tam_resim = ImageOps.fit(img_orjinal, (opt.PENCERE_BOYUTU, opt.PENCERE_BOYUTU),
                                 centering=(0.5, 0.5), method=Image.LANCZOS)

        kırpılan_parçalar = []
        for r in range(opt.BOYUT):
            for c in range(opt.BOYUT):
                kutu = (c * opt.HUCRE_BOYUTU, r * opt.HUCRE_BOYUTU,
                        (c + 1) * opt.HUCRE_BOYUTU, (r + 1) * opt.HUCRE_BOYUTU)
                parca = tam_resim.crop(kutu)
                kırpılan_parçalar.append(ImageTk.PhotoImage(parca))

        for i in range(1, 9):
            self.parcalar[i] = kırpılan_parçalar[i - 1]

        self.son_parca_gorseli = kırpılan_parçalar[opt.BOYUT * opt.BOYUT - 1]

        bos_resim = Image.new('RGB', (opt.HUCRE_BOYUTU, opt.HUCRE_BOYUTU), color=opt.RENK_SAYI_BOS)
        self.bos_gorsel = ImageTk.PhotoImage(bos_resim)

        return True

    def butonlari_olustur(self):
        ana_frame = tk.Frame(self.pencere, bg=opt.RENK_ARKA_PLAN)
        ana_frame.pack(expand=True, fill="both", padx=20, pady=20)

        tk.Label(ana_frame, text="RESİM BULMACASI", font=opt.FONT_BASLIK,
                 fg=opt.RENK_BASLIK, bg=opt.RENK_ARKA_PLAN).pack(pady=15)

        grid_frame = tk.Frame(ana_frame, bg=opt.RENK_GRID_CERCEVE, bd=0, relief="ridge")
        grid_frame.pack(pady=10)

        for r in range(opt.BOYUT):
            satir_btns = []
            for c in range(opt.BOYUT):
                btn = tk.Button(grid_frame, relief="flat", borderwidth=0,
                                command=lambda r=r, c=c: self.tikla(r, c))
                btn.grid(row=r, column=c, padx=5, pady=5)
                satir_btns.append(btn)
            self.butonlar.append(satir_btns)

        tk.Button(ana_frame, text="← Menüye Dön", font=opt.FONT_BUTON,
                  bg=opt.RENK_VURGU, fg="black", activebackground="#67E8F9",
                  width=20, height=2, command=self.kapat).pack(pady=25)

        self.guncelle()

    def guncelle(self):
        for r in range(opt.BOYUT):
            for c in range(opt.BOYUT):
                deger = self.motor.tahta[r][c]
                if deger == 0:
                    if self.motor.kazandi_mi() and r == opt.BOYUT - 1 and c == opt.BOYUT - 1:
                        self.butonlar[r][c].config(image=self.son_parca_gorseli)
                    else:
                        self.butonlar[r][c].config(image=self.bos_gorsel)
                else:
                    self.butonlar[r][c].config(image=self.parcalar[deger])

    def tikla(self, r, c):
        if self.motor.hareket_et(r, c):
            self.guncelle()
            if self.motor.kazandi_mi():
                messagebox.showinfo("🎉 Tebrikler!", "Resim tamamlandı!")
                self.kapat()

    def kapat(self):
        for widget in self.pencere.winfo_children():
            widget.destroy()
        self.menu_don()
