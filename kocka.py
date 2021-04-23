import random
import tkinter
from PIL import ImageTk, Image

class Kocka:
    def __init__(self, x, y, canvas, majitel):
        self.x, self.y = x, y                       # suradnice na ktorych sa vytvori kocka
        self.canvas = canvas                        # aby to pouzivalo rovnaky canvas
        self.majitel = majitel                      # koho je kocka
        self.animacia_hadzanie_kocky = []           # obrazky pre animaciu kocky 
        self.hodene_kocky = []                      # obrazky co sa moze hodit
        self.pomoc_cas = 11                         # odratava obr v animacii
        self.moze_menu = True                       # moze kliknut na menu ak je v hre
        for i in range(1,7):
            self.anim_k = ImageTk.PhotoImage(Image.open(f'obrazky/kockaAnimacia/kocka{i}.png'))  # otvorim obr
            self.animacia_hadzanie_kocky.append(self.anim_k)                                            # pridam do zoznamu
            self.hod_k = ImageTk.PhotoImage(Image.open(f'obrazky/hodena_kocka/{i}.png'))                # otvorim obr
            self.hodene_kocky.append(self.hod_k)                                                        # pridam do zoz

    def hod(self):
        self.hodene = random.randrange(6)+1         # nahodne hodi
        self.moze_menu = False                      # ak je niekto prave hadze kockou, neda sa odist z hry
        self.obr_kocky = self.canvas.create_image(self.x, self.y, image= self.animacia_hadzanie_kocky[0])   # zobrazi sa prvy obr animacie
        self.pomoc_cas = 0
        self.hod_casovac()

    def hod_casovac(self):
        #-------- prvykrat prebehne animacia hadzania kocky ---------------------------------------------
        if self.pomoc_cas < 5:
            self.canvas.itemconfig(self.obr_kocky, image= self.animacia_hadzanie_kocky[self.pomoc_cas+1])
            self.pomoc_cas += 1
            self.canvas.after(80, self.hod_casovac)
        #-------- druhykrat prebehne animacia hadzania kocky --------------------------------------------
        elif self.pomoc_cas < 11:
            self.canvas.itemconfig(self.obr_kocky, image= self.animacia_hadzanie_kocky[self.pomoc_cas-5])
            self.pomoc_cas += 1
            self.canvas.after(80, self.hod_casovac)
        # -------- animacia skonci a ukaze sa kolko hrac hodil ------------------------------------------
        else:
            self.canvas.itemconfig(self.obr_kocky, image= self.hodene_kocky[self.hodene-1])
            self.majitel.posun(self.hodene)                     # zavola sa posunutie hraca, vstup - kolko hodil

    def kocka_prec(self):
        self.canvas.delete(self.obr_kocky)                      # vymaze obr kocky