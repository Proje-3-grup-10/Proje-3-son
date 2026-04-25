import random
import ayarlar as opt

class BulmacaMotoru:
    def __init__(self):
        self.size = opt.BOYUT
        self.tahta = []
        self.hedef = []
        self.kurulum()

    def kurulum(self):
        sayilar = list(range(1, self.size * self.size)) + [0]
        self.hedef = [sayilar[i:i + self.size] for i in range(0, len(sayilar), self.size)]
        self.tahta = [satir[:] for satir in self.hedef]

    def bosluk_bul(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.tahta[r][c] == 0:
                    return r, c

    def hareket_et(self, r, c):
        br, bc = self.bosluk_bul()
        if abs(r - br) + abs(c - bc) == 1:
            self.tahta[br][bc], self.tahta[r][c] = self.tahta[r][c], self.tahta[br][bc]
            return True
        return False

    def karistir(self):
        for _ in range(1000):
            r, c = random.randint(0, self.size-1), random.randint(0, self.size-1)
            self.hareket_et(r, c)

    def kazandi_mi(self):
        return self.tahta == self.hedef
