import tkinter
from PIL import Image, ImageTk
from kocka import Kocka

class Hrac:
    def __init__(self, meno_postavy, canvas, program):
        self.program = program                              # aby mohol volat veci z hry
        self.peniaze = 100                                   # peniaze hraca
        self.pozicia = 0                                    # pociatocna pozicia - start
        self.nakupene = []                                  # karticky, co nakupil hrac
        self.meno_postavy = meno_postavy                    # za ktoru postavu hrac hra
        self.canvas = canvas                                # pouziva rovnaky canvas, nie novy
        self.pomocna_premenna_pre_casovac = 25              # odratava obrazky v animacii
        self.slovnik_pozicii = {}                           # suradnice pre kazdeho hraca na jednotl. poziciach
        self.pozicie_karticiek = []                         # suradnice kam vykresluje kupene karticky jednotl. hracom
        self.obr_karticiek = []                             # obrazky karticiek, ktore hrac kupil
        self.obr_karticiekTk = []                           # objekty v tkinteri - obr karticiek, ktore hrac kupil
        # --------- postava: MALEFICENT -------------------
        if self.meno_postavy == 'maleficent':
            self.Xkocky, self.Ykocky = 1026, 420            # suradnice, na ktorych sa objavi kocka na hodenie                         
            self.text_peniazky = self.canvas.create_text(1165, 445, text= f'{self.peniaze} ₳₳', fill= 'black', font= '"Gill Sans MT" 20')
            #.....suradnice na pohyb.......................
            self.slovnik_pozicii[0] = (910, 615)
            self.slovnik_pozicii[10] = (320, 600)
            self.slovnik_pozicii[20] = (335, 30)
            self.slovnik_pozicii[30] = (910, 30)
            self.slovnik_pozicii[40] = (345, 600)
            for i in range(1, 10):
                self.slovnik_pozicii[i] = (895-53*i, 610)
                self.slovnik_pozicii[10+i] = (330, 590-53*i)
                self.slovnik_pozicii[20+i] = (360+54*i, 35)
                self.slovnik_pozicii[30+i] = (920, 60+53*i)
            #....suradnice nakupenych karticiek.............
            for i in range(8):
                for j in range(4):
                    self.pozicie_karticiek.append((1018+j*67, 538+i*30))
        # --------- postava: URSULA -----------------------
        if self.meno_postavy == 'ursula':
            self.Xkocky, self.Ykocky = 249, 422
            self.text_peniazky = self.canvas.create_text(100, 445, text= f'{self.peniaze} ₳₳', fill= 'black', font= '"Gill Sans MT" 20')
            #.....suradnice na pohyb.......................
            self.slovnik_pozicii[0] = (940, 615)
            self.slovnik_pozicii[10] = (320, 635)
            self.slovnik_pozicii[20] = (355, 35)
            self.slovnik_pozicii[30] = (940, 35)
            self.slovnik_pozicii[40] = (365, 600)
            for i in range(1, 10):
                self.slovnik_pozicii[i] = (910-53*i, 620)
                self.slovnik_pozicii[10+i] = (350, 590-53*i)
                self.slovnik_pozicii[20+i] = (373+54*i, 38)
                self.slovnik_pozicii[30+i] = (940, 60+53*i)
            #....suradnice nakupenych karticiek.............
            for i in range(8):
                for j in range(4):
                    self.pozicie_karticiek.append((54+j*67, 540+i*30))
        # --------- postava: EVIL QUEEN -------------------
        if self.meno_postavy == 'evilqueen':
            self.Xkocky, self.Ykocky = 248, 117
            self.text_peniazky = self.canvas.create_text(100, 140, text= f'{self.peniaze} ₳₳', fill= 'black', font= '"Gill Sans MT" 20')
            #.....suradnice na pohyb.......................
            self.slovnik_pozicii[0] = (920, 635)
            self.slovnik_pozicii[10] = (350, 640)
            self.slovnik_pozicii[20] = (340, 50)
            self.slovnik_pozicii[30] = (920, 50)
            self.slovnik_pozicii[40] = (355, 620)
            for i in range(1, 10):
                self.slovnik_pozicii[i] = (900-53*i, 630)
                self.slovnik_pozicii[10+i] = (340, 600-53*i)
                self.slovnik_pozicii[20+i] = (365+54*i, 45)
                self.slovnik_pozicii[30+i] = (925, 70+53*i)
            #....suradnice nakupenych karticiek.............
            for i in range(8):
                for j in range(4):
                    self.pozicie_karticiek.append((54+j*67, 235+i*30))
        # --------- postava: JAFFAR -------------------
        if self.meno_postavy == 'jaffar':
            self.Xkocky, self.Ykocky = 1025, 115
            self.text_peniazky = self.canvas.create_text(1165, 140, text= f'{self.peniaze} ₳₳', fill= 'black', font= '"Gill Sans MT" 20')
            #.....suradnice na pohyb.......................
            self.slovnik_pozicii[0] = (950, 635)
            self.slovnik_pozicii[10] = (380, 640)
            self.slovnik_pozicii[20] = (365, 55)
            self.slovnik_pozicii[30] = (950, 55)
            self.slovnik_pozicii[40] = (375, 620)
            for i in range(1, 10):
                self.slovnik_pozicii[i] = (912-53*i, 640)
                self.slovnik_pozicii[10+i] = (360, 600-53*i)
                self.slovnik_pozicii[20+i] = (380+54*i, 52)
                self.slovnik_pozicii[30+i] = (950, 70+53*i)
            #....suradnice nakupenych karticiek.............
            for i in range(8):
                for j in range(4):
                    self.pozicie_karticiek.append((1018+j*67, 233+i*30))
        # -------- VLASTNA KOCKA --------------------------------------------------
        self.kocka = Kocka(self.Xkocky, self.Ykocky, self.canvas, self)     
        # -------- OBRAZOK PANACIKA -----------------------------------------------
        img = Image.open(f'obrazky/panacikovia/{self.meno_postavy}.png').resize((25, 50))       
        self.img_panacik = ImageTk.PhotoImage(img)
        self.o = canvas.create_image(self.slovnik_pozicii[self.pozicia], image=self.img_panacik)
        # -------- OBRAZOK NA ANIMACIU POSUVANIA -----------------------------------
        sparkle = Image.open(f'obrazky/sparkles/sparkle_{self.meno_postavy}.png').resize((200,200))
        self.animacia = [sparkle.resize((100,100)), sparkle.resize((130,130)),
        sparkle.resize((160,160)), sparkle, sparkle.resize((240,240)), sparkle.resize((270,270)), 
        sparkle.resize((310,310)), sparkle.resize((270,270)), sparkle.resize((240,240)), 
        sparkle, sparkle.resize((160,160)), sparkle.resize((130,130)), sparkle.resize((100,100))]

    def posun(self, hodene):
        self.hodene = hodene                                            # kolko hrac hodil
        self.sparkle_img = ImageTk.PhotoImage(self.animacia[0])         # prvy obr animacie posunutia, sparkle
        self.sparkles = self.canvas.create_image(self.slovnik_pozicii[self.pozicia], image= self.sparkle_img)
        self.pomocna_premenna_pre_casovac = 0
        self.posun_casovac()

    def posun_casovac(self):
        # ------ animacia na povodnej pozicii ---------------------------------------
        if self.pomocna_premenna_pre_casovac < 12:
            self.sparkle_img = ImageTk.PhotoImage(self.animacia[self.pomocna_premenna_pre_casovac+1]) 
            self.canvas.itemconfig(self.sparkles, image= self.sparkle_img)
            self.pomocna_premenna_pre_casovac += 1
            self.canvas.after(100, self.posun_casovac)
        # ------ posunie sa panacik --------------------------------------------------
        elif self.pomocna_premenna_pre_casovac == 12: 
            self.pozicia += self.hodene                                             # zmeni sa pozicia hraca
            if self.pozicia == 100:                                                 # ak je to zalar (specialne suradnice)
                self.pozicia = 40
            elif self.pozicia > 39:                                                 # po prechode startom +5M
                self.pozicia -= 40
                self.peniaze += 5
                self.program.vypis_peniazky()                                       # aktualizuju sa peniaze
            elif self.pozicia < 0:                                                  # ak ide dozadu
                self.pozicia += 40 
            self.canvas.coords(self.o, self.slovnik_pozicii[self.pozicia])          # panacik sa premiestni
            self.pomocna_premenna_pre_casovac += 1
            self.canvas.coords(self.sparkles, self.slovnik_pozicii[self.pozicia])   # animacia sa bude odohravat na novom policku
            self.sparkle_img = ImageTk.PhotoImage(self.animacia[0]) 
            self.canvas.itemconfig(self.sparkles, image= self.sparkle_img)
            self.canvas.after(100, self.posun_casovac)     
        # ------ animacia na novej pozicii ------------------------------------------
        elif self.pomocna_premenna_pre_casovac < 25:
            self.sparkle_img = ImageTk.PhotoImage(self.animacia[self.pomocna_premenna_pre_casovac-12]) 
            self.canvas.itemconfig(self.sparkles, image= self.sparkle_img)
            self.pomocna_premenna_pre_casovac += 1
            self.canvas.after(100, self.posun_casovac)
        # ------ zmiznutie ----------------------------------------------------------
        elif self.pomocna_premenna_pre_casovac == 25:   
            self.canvas.delete(self.sparkles)                                       # zmizne posledny obr z animacie sparkle
            #.....ak je v zalari...............................
            if self.pozicia == 40:                                                  
                try:
                    self.canvas.delete(self.program.karticka)                       # ak sa da zmaze obr aktualneho policka
                except AttributeError:
                    pass
                self.canvas.delete(self.program.cierna)                             # zmaze ciernu plochu
                self.program.canvas.bind('<ButtonPress>', self.program.klik)        # bude sa dat klikat
                self.program.prepni_hracov()                                        # prepne hracov
            #.....ak je hocikde inde..........................
            else:
                self.kocka.kocka_prec()                                             # zavola sa zmiznutie kocky
                self.program.policka()                                              # vysetruje sa na akom policku je
      
    def hadze(self):
        self.kocka.hod()                                                            # hodi kockou