import random
from hrac import Hrac, tkinter, Image, ImageTk

class Program:
    def __init__(self):
        self.sirka, self.vyska = 1277, 680                  # rozmery okna
        self.stred = (638, 340)                             # suradnice stredu
        self.zoznam_hracov = []
        
        self.okno = tkinter.Tk()
        self.okno.title('MONOPOLY night out')
        obrazok = ImageTk.PhotoImage(file= 'obrazky/kocky.png')
        self.okno.iconphoto(False, obrazok)
        #----farby----
        self.modra = '#b8f1f1'
        self.ruzova = '#ffcbe5'
        self.zelena = '#c1f3d6'
        self.silno_ruzova = '#ff9fcf'
        self.zlta = '#f9ff9b'
        self.canvas = tkinter.Canvas(width= self.sirka, height= self.vyska, bg= 'black')
        self.canvas.pack()
        
        self.vytvor_menu()

        self.okno.mainloop()
    #---------- UVODNE MENU --------------------------------------------------------------------------
    def vytvor_menu(self):
        #----------------------najprv skusi vymazat---------------------------
        try:
            self.canvas.delete(self.buttonSpat)
            self.canvas.delete(self.buttonHrat) 
            self.canvas.delete(self.plocha)
            self.canvas.delete(self.meno_evilqueen)
            self.canvas.delete(self.meno_ursula)
            self.canvas.delete(self.meno_maleficent)
            self.canvas.delete(self.meno_jaffar)
        except AttributeError:
            pass
        try:
            self.canvas.delete(self.buttonNacitajHra1)
            self.canvas.delete(self.buttonNacitajHra2)
            self.canvas.delete(self.buttonNacitajHra3)
            self.canvas.delete(self.menu)
        except AttributeError:
            pass
        #............................pozadnie.................................
        self.obr = ImageTk.PhotoImage(Image.open('obrazky/uvod_menu.png'))
        self.menu = self.canvas.create_image(630, 340, image= self.obr)
        #............................tlacidka.................................
        #....nova hra....
        buttonNovaHra = tkinter.Button(self.canvas, text= 'NOVÁ HRA', command= self.vyber_hracov)
        buttonNovaHra.configure(activebackground= self.ruzova, activeforeground= 'black', 
        fg= 'black', bg= self.modra, font= '"Gill Sans MT" 20', width= 10) 
        self.buttonNovaHra = self.canvas.create_window(610, 320, window= buttonNovaHra)
        #....stara hra....
        buttonStaraHra = tkinter.Button(self.canvas, text= 'STARÁ HRA', command= self.menu_nacitat)
        buttonStaraHra.configure(activebackground= self.ruzova, activeforeground= 'black', 
        fg= 'black', bg= self.modra, font= '"Gill Sans MT" 20', width= 10) 
        self.buttonStaraHra = self.canvas.create_window(610, 390, window= buttonStaraHra)
        #....pravidla....
        buttonPravidla = tkinter.Button(self.canvas, text= 'PRAVIDLÁ', command = self.pravidla)
        buttonPravidla.configure(activebackground= self.ruzova, activeforeground= 'black', 
        fg= 'black', bg= self.modra, font= '"Gill Sans MT" 20', width= 10) 
        self.buttonPravidla = self.canvas.create_window(610, 460, window= buttonPravidla)
        #....koniec....
        buttonKoniec = tkinter.Button(self.canvas, text = 'KONIEC', command= self.okno.destroy)
        buttonKoniec.configure(activebackground= self.ruzova, activeforeground= 'black', 
        fg= 'black', bg= self.modra, font= '"Gill Sans MT" 20', width= 10) 
        self.buttonKoniec = self.canvas.create_window(610,530, window= buttonKoniec)
    
    def pravidla(self):
        try:
            self.canvas.delete(self.buttonPokracovat)
        except AttributeError:
            pass
        try:
            self.canvas.delete(self.buttonVlavo)
        except AttributeError:
            pass
        try:
            self.canvas.delete(self.buttonVpravo)
        except AttributeError:
            pass
        self.canvas.delete(self.buttonNovaHra)
        self.canvas.delete(self.buttonStaraHra)
        self.canvas.delete(self.buttonPravidla)
        self.canvas.delete(self.buttonKoniec)
        self.p1 = ImageTk.PhotoImage(Image.open('obrazky/pravidla1.png'))
        self.prav = self.canvas.create_image(self.stred[0], self.stred[1]+10, image= self.p1)
        #....tlacidko spat....
        self.spat = ImageTk.PhotoImage(Image.open('obrazky/vlavo.png').resize((50,50)))          
        buttonSpat = tkinter.Button(self.canvas, image= self.spat, command= self.vymaz_prav) 
        buttonSpat.configure(activebackground= 'black', bg= 'black', font= '"Gill Sans MT" 20', borderwidth= 0) 
        self.buttonSpat = self.canvas.create_window(2, 2, anchor= 'nw', window= buttonSpat)
        #....tlacidko vpravo....
        self.vpr = ImageTk.PhotoImage(Image.open('obrazky/vpravo.png').resize((70,70)))          
        buttonVpravo = tkinter.Button(self.canvas, image= self.vpr, command= self.pravidlo2) 
        buttonVpravo.configure(activebackground= 'black', bg= 'black', font= '"Gill Sans MT" 20', borderwidth= 0) 
        self.buttonVpravo = self.canvas.create_window(self.stred[0]+140, 15, anchor= 'nw', window= buttonVpravo)

    def pravidla_z_hry(self):
        if self.zoznam_hracov[self.kto_je_na_rade[0][1]].kocka.moze_menu and self.ide_casovac:
            try:
                self.canvas.delete(self.buttonVlavo)
            except AttributeError:
                pass
            try:
                self.canvas.delete(self.buttonVpravo)
            except AttributeError:
                pass
            self.canvas.delete(self.buttonZbieranie)
            self.canvas.delete(self.buttonUlozit)
            self.canvas.delete(self.buttonPravidla_obr)
            self.canvas.delete(self.buttonMenu)
            self.p1 = ImageTk.PhotoImage(Image.open('obrazky/pravidla1.png'))
            self.prav = self.canvas.create_image(self.stred[0], self.stred[1]+5, image= self.p1)
            #....tlacidko spat....
            self.spat = ImageTk.PhotoImage(Image.open('obrazky/vlavo.png').resize((50,50)))          
            buttonSpat = tkinter.Button(self.canvas, image= self.spat, command= self.pokracovat) 
            buttonSpat.configure(activebackground= 'black', bg= 'black', font= '"Gill Sans MT" 20', borderwidth= 0) 
            self.buttonSpat = self.canvas.create_window(2, 2, anchor= 'nw', window= buttonSpat)
            #....tlacidko vpravo....
            self.vpr = ImageTk.PhotoImage(Image.open('obrazky/vpravo.png').resize((70,70)))          
            buttonVpravo = tkinter.Button(self.canvas, image= self.vpr, command= self.pravidlo_z_hry2) 
            buttonVpravo.configure(activebackground= 'black', bg= 'black', font= '"Gill Sans MT" 20', borderwidth= 0) 
            self.buttonVpravo = self.canvas.create_window(self.stred[0]+140, 15, anchor= 'nw', window= buttonVpravo)

    def vymaz_prav(self):
        self.canvas.delete(self.prav)
        self.canvas.delete(self.buttonSpat)
        try:
            self.canvas.delete(self.buttonVpravo)
        except AttributeError:
            pass
        try:
            self.canvas.delete(self.buttonVlavo)
        except AttributeError:
            pass
        self.vytvor_menu()

    def pravidlo2(self):
        self.canvas.delete(self.prav)
        self.canvas.delete(self.buttonSpat)
        try:
            self.canvas.delete(self.buttonVpravo)
        except AttributeError:
            pass
        try:
            self.canvas.delete(self.buttonVlavo)
        except AttributeError:
            pass
        self.p1 = ImageTk.PhotoImage(Image.open('obrazky/pravidla2.png'))
        self.prav = self.canvas.create_image(self.stred[0], self.stred[1]+10, image= self.p1)
        #....tlacidko spat....
        self.spat = ImageTk.PhotoImage(Image.open('obrazky/vlavo.png').resize((50,50)))          
        buttonSpat = tkinter.Button(self.canvas, image= self.spat, command= self.vymaz_prav) 
        buttonSpat.configure(activebackground= 'black', bg= 'black', font= '"Gill Sans MT" 20', borderwidth= 0) 
        self.buttonSpat = self.canvas.create_window(2, 2, anchor= 'nw', window= buttonSpat)
        #....tlacidko vpravo....
        self.vpr = ImageTk.PhotoImage(Image.open('obrazky/vpravo.png').resize((70,70)))          
        buttonVpravo = tkinter.Button(self.canvas, image= self.vpr, command= self.pravidlo3) 
        buttonVpravo.configure(activebackground= 'black', bg= 'black', font= '"Gill Sans MT" 20', borderwidth= 0) 
        self.buttonVpravo = self.canvas.create_window(self.stred[0]+140, 15, anchor= 'nw', window= buttonVpravo)
        #....tlacidko vlavo....
        self.vl = ImageTk.PhotoImage(Image.open('obrazky/vlavo.png').resize((70,70)))          
        buttonVlavo = tkinter.Button(self.canvas, image= self.vl, command= self.pravidla) 
        buttonVlavo.configure(activebackground= 'black', bg= 'black', font= '"Gill Sans MT" 20', borderwidth= 0) 
        self.buttonVlavo = self.canvas.create_window(self.stred[0]-220, 15, anchor= 'nw', window= buttonVlavo)

    def pravidlo_z_hry2(self):
        self.canvas.delete(self.prav)
        self.canvas.delete(self.buttonSpat)
        try:
            self.canvas.delete(self.buttonVpravo)
        except AttributeError:
            pass
        try:
            self.canvas.delete(self.buttonVlavo)
        except AttributeError:
            pass
        self.p1 = ImageTk.PhotoImage(Image.open('obrazky/pravidla2.png'))
        self.prav = self.canvas.create_image(self.stred[0], self.stred[1]+5, image= self.p1)
        #....tlacidko spat....
        self.spat = ImageTk.PhotoImage(Image.open('obrazky/vlavo.png').resize((50,50)))          
        buttonSpat = tkinter.Button(self.canvas, image= self.spat, command= self.pokracovat) 
        buttonSpat.configure(activebackground= 'black', bg= 'black', font= '"Gill Sans MT" 20', borderwidth= 0) 
        self.buttonSpat = self.canvas.create_window(2, 2, anchor= 'nw', window= buttonSpat)
        #....tlacidko vpravo....
        self.vpr = ImageTk.PhotoImage(Image.open('obrazky/vpravo.png').resize((70,70)))          
        buttonVpravo = tkinter.Button(self.canvas, image= self.vpr, command= self.pravidlo_z_hry3) 
        buttonVpravo.configure(activebackground= 'black', bg= 'black', font= '"Gill Sans MT" 20', borderwidth= 0) 
        self.buttonVpravo = self.canvas.create_window(self.stred[0]+140, 15, anchor= 'nw', window= buttonVpravo)
        #....tlacidko vlavo....
        self.vl = ImageTk.PhotoImage(Image.open('obrazky/vlavo.png').resize((70,70)))          
        buttonVlavo = tkinter.Button(self.canvas, image= self.vl, command= self.pravidla_z_hry) 
        buttonVlavo.configure(activebackground= 'black', bg= 'black', font= '"Gill Sans MT" 20', borderwidth= 0) 
        self.buttonVlavo = self.canvas.create_window(self.stred[0]-220, 15, anchor= 'nw', window= buttonVlavo)

    def pravidlo3(self):
        self.canvas.delete(self.prav)
        self.canvas.delete(self.buttonSpat)
        try:
            self.canvas.delete(self.buttonVpravo)
        except AttributeError:
            pass
        try:
            self.canvas.delete(self.buttonVlavo)
        except AttributeError:
            pass
        self.p1 = ImageTk.PhotoImage(Image.open('obrazky/pravidla3.png'))
        self.prav = self.canvas.create_image(self.stred[0], self.stred[1]+10, image= self.p1)
        #....tlacidko spat....
        self.spat = ImageTk.PhotoImage(Image.open('obrazky/vlavo.png').resize((50,50)))          
        buttonSpat = tkinter.Button(self.canvas, image= self.spat, command= self.vymaz_prav) 
        buttonSpat.configure(activebackground= 'black', bg= 'black', font= '"Gill Sans MT" 20', borderwidth= 0) 
        self.buttonSpat = self.canvas.create_window(2, 2, anchor= 'nw', window= buttonSpat)
        #....tlacidko vlavo....
        self.vl = ImageTk.PhotoImage(Image.open('obrazky/vlavo.png').resize((70,70)))          
        buttonVlavo = tkinter.Button(self.canvas, image= self.vl, command= self.pravidlo2) 
        buttonVlavo.configure(activebackground= 'black', bg= 'black', font= '"Gill Sans MT" 20', borderwidth= 0) 
        self.buttonVlavo = self.canvas.create_window(self.stred[0]-220, 15, anchor= 'nw', window= buttonVlavo)

    def pravidlo_z_hry3(self):
        self.canvas.delete(self.prav)
        self.canvas.delete(self.buttonSpat)
        try:
            self.canvas.delete(self.buttonVpravo)
        except AttributeError:
            pass
        try:
            self.canvas.delete(self.buttonVlavo)
        except AttributeError:
            pass
        self.p1 = ImageTk.PhotoImage(Image.open('obrazky/pravidla3.png'))
        self.prav = self.canvas.create_image(self.stred[0], self.stred[1]+5, image= self.p1)
        #....tlacidko spat....
        self.spat = ImageTk.PhotoImage(Image.open('obrazky/vlavo.png').resize((50,50)))          
        buttonSpat = tkinter.Button(self.canvas, image= self.spat, command= self.pokracovat) 
        buttonSpat.configure(activebackground= 'black', bg= 'black', font= '"Gill Sans MT" 20', borderwidth= 0) 
        self.buttonSpat = self.canvas.create_window(2, 2, anchor= 'nw', window= buttonSpat)
        #....tlacidko vlavo....
        self.vl = ImageTk.PhotoImage(Image.open('obrazky/vlavo.png').resize((70,70)))          
        buttonVlavo = tkinter.Button(self.canvas, image= self.vl, command= self.pravidlo_z_hry2) 
        buttonVlavo.configure(activebackground= 'black', bg= 'black', font= '"Gill Sans MT" 20', borderwidth= 0) 
        self.buttonVlavo = self.canvas.create_window(self.stred[0]-220, 15, anchor= 'nw', window= buttonVlavo)

    def vyber_hracov(self):
        #........vymazem vsetko co netreba..............
        self.canvas.delete(self.buttonNovaHra)
        self.canvas.delete(self.buttonStaraHra)
        self.canvas.delete(self.buttonPravidla)
        self.canvas.delete(self.buttonKoniec)
        try:
            self.canvas.delete(self.buttonPokracovat)
        except AttributeError:
            pass
        #..........idem kreslit............................
        #....obrazok pozadia....
        self.p = ImageTk.PhotoImage(Image.open('obrazky/hraci.png'))
        self.plocha = self.canvas.create_image(630, 320, image= self.p)
        #....texty....
        self.canvas.create_text(630, 50, text= 'VYBER HRÁČOV:', fill= 'white', font= '"Gill Sans MT" 50')  
        for i in 135, 260, 375, 500:   
            self.canvas.create_text(580, i, text= 'MENO:', fill= 'black', font= '"Gill Sans MT" 25')
        #....vstupy pre mena....
        self.meno_m = tkinter.Entry(self.canvas, bg= self.ruzova, font= '"Gill Sans MT" 20', width= 13)
        self.meno_maleficent = self.canvas.create_window(578, 183, window= self.meno_m)
        self.meno_u = tkinter.Entry(self.canvas, bg= '#ddf8e8', font= '"Gill Sans MT" 20', width= 13)
        self.meno_ursula = self.canvas.create_window(580, 307, window= self.meno_u)
        self.meno_e = tkinter.Entry(self.canvas, bg='#fffbbe', font= '"Gill Sans MT" 20', width= 13)
        self.meno_evilqueen= self.canvas.create_window(580, 427, window= self.meno_e)
        self.meno_j = tkinter.Entry(self.canvas, bg='#d5f7f7', font= '"Gill Sans MT" 20', width= 13)
        self.meno_jaffar= self.canvas.create_window(580, 548, window= self.meno_j)
        #------ak by bolo malo hracov--------
        self.zle = self.canvas.create_text(630, 90, text = '')
        #....tlacidko hrat....
        buttonHrat = tkinter.Button(self.canvas, text= 'Hrať!', command= self.overenie)
        buttonHrat.configure(activebackground= 'white', activeforeground= 'black', 
        fg= 'white', bg= 'black', font= '"Gill Sans MT" 20', borderwidth= 0) 
        self.buttonHrat = self.canvas.create_window(630, 620, window= buttonHrat)
        #....tlacidko spat....
        self.spat = ImageTk.PhotoImage(Image.open('obrazky/vlavo.png').resize((50,50)))          
        buttonSpat = tkinter.Button(self.canvas, image= self.spat, command= self.vytvor_menu) 
        buttonSpat.configure(activebackground= 'black', bg= 'black', font= '"Gill Sans MT" 20', borderwidth= 0) 
        self.buttonSpat = self.canvas.create_window(2, 2, anchor= 'nw', window= buttonSpat)

    def nopockajzajac(self):
        # ------------ pouzitie pri ulozeni --------------
        try:
            self.canvas.delete(self.text_ulozene)
        except AttributeError:
            pass
        # ---------- pouzitie pri overeni ----------------
        try:    
            self.canvas.itemconfig(self.zle, text = '')     # zmizne text ze je malo hracov
        except AttributeError:
            pass

    def overenie(self):
        #----- nacita mena a postavy hracov --------
        self.slovnik_meno_priezvisko = {}
        n = 0
        if self.meno_m.get() != '':
            self.slovnik_meno_priezvisko['maleficent'] = self.meno_m.get()
            n += 1
        if self.meno_u.get() != '':
            self.slovnik_meno_priezvisko['ursula'] = self.meno_u.get()
            n += 1
        if self.meno_e.get() != '':
            self.slovnik_meno_priezvisko['evilqueen'] = self.meno_e.get()
            n += 1
        if self.meno_j.get() != '':
            self.slovnik_meno_priezvisko['jaffar'] = self.meno_j.get()
            n += 1
        #---------------- ak je malo hracov ---------------
        if n < 2:
            # prepise sa text v self.zle
            self.canvas.itemconfig(self.zle, text= 'Málo hráčov. Musia byť aspoň 2.', fill= 'red', font= '"Gill Sans MT" 15')
            # zapne sa casovac
            self.canvas.after(1500, self.nopockajzajac)
        #----------ak je dost hracov, zapne sa hra ---------
        elif n >= 2:
            self.vytvor_plochu()

    def menu_z_hry(self):
        # -------------- da sa ist do menu iba ak nikto nie je na rade -----------------------
        if self.zoznam_hracov[self.kto_je_na_rade[0][1]].kocka.moze_menu and self.ide_casovac:
            try:
                self.canvas.delete(self.buttonMenu)
                self.canvas.delete(self.buttonUlozit)
                self.canvas.delete(self.buttonZbieranie)
                self.canvas.delete(self.buttonPravidla_obr)
            except AttributeError:
                pass
            try:
                self.canvas.delete(self.buttonSpat)
                self.canvas.delete(self.buttonUlozHra1)
                self.canvas.delete(self.buttonUlozHra2)
                self.canvas.delete(self.buttonUlozHra3)
            except AttributeError:
                pass
            self.canvas.unbind('<ButtonPress>')
            self.obr = ImageTk.PhotoImage(Image.open('obrazky/uvod_hra.png'))
            self.menu = self.canvas.create_image(630, 340, image= self.obr)
            buttonPokracovat = tkinter.Button(self.canvas, text= 'POKRAČOVAŤ', command= self.pokracovat)
            buttonPokracovat.configure(activebackground= self.ruzova, activeforeground= 'black', 
            fg= 'black', bg= self.modra, font= '"Gill Sans MT" 20', width= 13) 
            self.buttonPokracovat = self.canvas.create_window(610, 320, window= buttonPokracovat)
            buttonNovaHra = tkinter.Button(self.canvas, text= 'NOVÁ HRA', command= self.vyber_hracov)
            buttonNovaHra.configure(activebackground= self.ruzova, activeforeground= 'black', 
            fg= 'black', bg= self.modra, font= '"Gill Sans MT" 20', width= 13) 
            self.buttonNovaHra = self.canvas.create_window(610, 390, window= buttonNovaHra)
            buttonStaraHra = tkinter.Button(self.canvas, text= 'STARÁ HRA', command= self.menu_nacitat)
            buttonStaraHra.configure(activebackground= self.ruzova, activeforeground= 'black', 
            fg= 'black', bg= self.modra, font= '"Gill Sans MT" 20', width= 13) 
            self.buttonStaraHra = self.canvas.create_window(610, 460, window= buttonStaraHra)
            buttonPravidla = tkinter.Button(self.canvas, text= 'PRAVIDLÁ', command= self.pravidla)
            buttonPravidla.configure(activebackground= self.ruzova, activeforeground= 'black', 
            fg= 'black', bg= self.modra, font= '"Gill Sans MT" 20', width= 13) 
            self.buttonPravidla = self.canvas.create_window(610, 530, window= buttonPravidla)
            buttonKoniec = tkinter.Button(self.canvas, text= 'KONIEC', command= self.okno.destroy)
            buttonKoniec.configure(activebackground= self.ruzova, activeforeground= 'black', 
            fg= 'black', bg= self.modra, font= '"Gill Sans MT" 20', width= 13) 
            self.buttonKoniec = self.canvas.create_window(610, 600, window= buttonKoniec)

    def pokracovat(self):
        try:
            self.canvas.delete(self.prav)
        except AttributeError:
            pass
        try:
            self.canvas.delete(self.menu)
            self.canvas.delete(self.buttonPokracovat)
            self.canvas.delete(self.buttonNovaHra)
            self.canvas.delete(self.buttonStaraHra)
            self.canvas.delete(self.buttonPravidla)
            self.canvas.delete(self.buttonKoniec)
        except AttributeError:
            pass
        try:
            self.canvas.delete(self.buttonSpat)
            try:
                self.canvas.delete(self.buttonVlavo)
            except AttributeError:
                pass
            try:
                self.canvas.delete(self.buttonVpravo)
            except AttributeError:
                pass
        except AttributeError:
            pass
        self.canvas.bind('<ButtonPress>', self.klik)
        #.... tlacidlo ist do menu ....
        self.obr_menu = ImageTk.PhotoImage(Image.open('obrazky/menu.png').resize((50,50)))          
        buttonMenu = tkinter.Button(self.canvas, image= self.obr_menu, command= self.menu_z_hry)
        buttonMenu.configure(activebackground= 'black', bg= 'black', borderwidth= 0) 
        self.buttonMenu = self.canvas.create_window(7, 7, anchor= 'nw', window= buttonMenu)
        #.... tlacidlo ulozit hru ....
        self.obr_ulozit = ImageTk.PhotoImage(Image.open('obrazky/ulozit.png').resize((50,50)))
        buttonUlozit = tkinter.Button(self.canvas, image= self.obr_ulozit, command= self.ponuka_ulozit)
        buttonUlozit.configure(activebackground= 'black', bg = 'black', borderwidth= 0) 
        self.buttonUlozit = self.canvas.create_window(self.sirka-10, 7, anchor= 'ne', window= buttonUlozit)
        #.... tlacidlo zbieranie ....
        self.zbier = ImageTk.PhotoImage(Image.open('obrazky/zbieranie.png').resize((50,50)))
        buttonZbieranie = tkinter.Button(self.canvas, image= self.zbier, command= self.zbieranie)
        buttonZbieranie.configure(activebackground= 'black', bg = 'black', borderwidth= 0) 
        self.buttonZbieranie = self.canvas.create_window(110, 7, anchor= 'nw', window= buttonZbieranie)
        #.... tlacidlo pravidla ....
        self.obr_pravidla = ImageTk.PhotoImage(Image.open('obrazky/pravidla.png').resize((50,50)))
        buttonPravidla_obr = tkinter.Button(self.canvas, image= self.obr_pravidla, command= self.pravidla_z_hry)
        buttonPravidla_obr.configure(activebackground= 'black', bg = 'black', borderwidth= 0) 
        self.buttonPravidla_obr = self.canvas.create_window(60, 7, anchor= 'nw', window= buttonPravidla_obr)

    def vytvor_plochu(self):
        # -------------- ak sa da vymaze -------------
        try:
            self.canvas.delete(self.buttonHrat)
            self.canvas.delete(self.meno_maleficent)
            self.canvas.delete(self.meno_ursula)
            self.canvas.delete(self.meno_evilqueen)
            self.canvas.delete(self.meno_jaffar)
            self.canvas.delete(self.buttonSpat)
        except AttributeError:
            pass
        # ---------------- da sa klikat --------------
        self.canvas.bind('<ButtonPress>', self.klik)
        # ----------------- pozadie ------------------
        self.pozadie = ImageTk.PhotoImage(Image.open('obrazky/hracia_plocha.png'))          
        self.plocha = self.canvas.create_image(630, 320, image= self.pozadie)
        self.kto_je_na_rade = []                        # zoznam hracov ako su na rade
        self.zoznam_hracov = []                         # zoznam kde su ulozeni hraci
        nieco = 0                                       # poradie v zozname hracov
        for kluc in self.slovnik_meno_priezvisko:    
            self.zoznam_hracov.append(Hrac(kluc, self.canvas, self))
            self.kto_je_na_rade.append((kluc, nieco))   # dvojice: postava a poradie v zozname hracov
            nieco += 1
        # ----- nastavenia hracov podla toho ci postava hra ----------
        self.nehra = ImageTk.PhotoImage(Image.open('obrazky/nehra.png'))
        if 'evilqueen' in self.slovnik_meno_priezvisko:
            self.canvas.create_text(100, 90, text= self.slovnik_meno_priezvisko['evilqueen'], fill= 'black', font= '"Gill Sans MT" 20')
        else:
            self.bez_hry_e = self.canvas.create_image(155, 213, image= self.nehra)
        if 'ursula' in self.slovnik_meno_priezvisko:
            self.canvas.create_text(100, 397, text= self.slovnik_meno_priezvisko['ursula'], fill= 'black', font= '"Gill Sans MT" 20')
        else:
            self.bez_hry_u = self.canvas.create_image(155, 519, image= self.nehra)
        if 'jaffar' in self.slovnik_meno_priezvisko:
            self.canvas.create_text(1165, 90, text= self.slovnik_meno_priezvisko['jaffar'], fill= 'black', font= '"Gill Sans MT" 20')
        else:
            self.bez_hry_u = self.canvas.create_image(1120, 211, image= self.nehra)
        if 'maleficent' in self.slovnik_meno_priezvisko:
            self.canvas.create_text(1165, 397, text= self.slovnik_meno_priezvisko['maleficent'], fill= 'black', font= '"Gill Sans MT" 20')
        else:
            self.bez_hry_m = self.canvas.create_image(1120, 518, image= self.nehra)
        # -------- ostatne nastavenia --------------------
        #.... kocka sa nastavi tomu kto zacina
        self.kocka_plocha = self.canvas.create_image(self.zoznam_hracov[self.kto_je_na_rade[0][1]].Xkocky, 
        self.zoznam_hracov[self.kto_je_na_rade[0][1]].Ykocky, 
        image= self.zoznam_hracov[0].kocka.animacia_hadzanie_kocky[random.randrange(6)])
        #.... da sa odist z hry ....
        self.ide_casovac = True
        self.cennik = {(7, 17, 23, 33): 15, (1, 16, 26, 34): 10, (3, 4, 11, 29): 8, (12, 19, 21, 36): 7, 
        (9, 24, 31, 39): 6, (6, 14, 28, 38): 5}
        self.nekupene_policka = {7, 17, 23, 33, 1, 16, 26, 34, 3, 4, 11, 29, 12, 19, 21, 36, 9, 24, 31, 39, 6, 14, 28, 38}
        #.... tlacidlo ist do menu ....
        self.obr_menu = ImageTk.PhotoImage(Image.open('obrazky/menu.png').resize((50,50)))          
        buttonMenu = tkinter.Button(self.canvas, image= self.obr_menu, command= self.menu_z_hry)
        buttonMenu.configure(activebackground= 'black', bg= 'black', borderwidth= 0) 
        self.buttonMenu = self.canvas.create_window(7, 7, anchor= 'nw', window= buttonMenu)
        #.... tlacidlo ulozit hru ....
        self.obr_ulozit = ImageTk.PhotoImage(Image.open('obrazky/ulozit.png').resize((50,50)))
        buttonUlozit = tkinter.Button(self.canvas, image= self.obr_ulozit, command= self.ponuka_ulozit)
        buttonUlozit.configure(activebackground= 'black', bg = 'black', borderwidth= 0) 
        self.buttonUlozit = self.canvas.create_window(self.sirka-10, 7, anchor= 'ne', window= buttonUlozit)
        #.... tlacidlo zbieranie ....
        self.zbier = ImageTk.PhotoImage(Image.open('obrazky/zbieranie.png').resize((50,50)))
        buttonZbieranie = tkinter.Button(self.canvas, image= self.zbier, command= self.zbieranie)
        buttonZbieranie.configure(activebackground= 'black', bg = 'black', borderwidth= 0) 
        self.buttonZbieranie = self.canvas.create_window(110, 7, anchor= 'nw', window= buttonZbieranie)
        #.... tlacidlo pravidla ....
        self.obr_pravidla = ImageTk.PhotoImage(Image.open('obrazky/pravidla.png').resize((50,50)))
        buttonPravidla_obr = tkinter.Button(self.canvas, image= self.obr_pravidla, command= self.pravidla_z_hry)
        buttonPravidla_obr.configure(activebackground= 'black', bg = 'black', borderwidth= 0) 
        self.buttonPravidla_obr = self.canvas.create_window(60, 7, anchor= 'nw', window= buttonPravidla_obr)

    def zbieranie(self):
        if self.zoznam_hracov[self.kto_je_na_rade[0][1]].kocka.moze_menu and self.ide_casovac:
            #... vymazem co sa da ....
            self.canvas.unbind('<ButtonPress>')
            self.canvas.delete(self.buttonPravidla_obr)
            self.canvas.delete(self.buttonUlozit)
            self.canvas.delete(self.buttonZbieranie)
            self.canvas.delete(self.buttonMenu)
            #.... otvorim obrazok ....
            self.o_z = ImageTk.PhotoImage(Image.open('obrazky/zbieranie_obr.png'))
            self.obr_zb = self.canvas.create_image(self.stred, image= self.o_z)
            #....tlacidko spat....
            self.spat = ImageTk.PhotoImage(Image.open('obrazky/vlavo.png').resize((50,50)))          
            buttonSpat = tkinter.Button(self.canvas, image= self.spat, command= self.zatvor_zbieranie) 
            buttonSpat.configure(activebackground= 'black', bg= 'black', font= '"Gill Sans MT" 20', borderwidth= 0) 
            self.buttonSpat = self.canvas.create_window(2, 2, anchor= 'nw', window= buttonSpat)

    def zatvor_zbieranie(self):
        self.canvas.delete(self.spat)
        self.canvas.delete(self.obr_zb)
        self.canvas.bind('<ButtonPress>', self.klik)
        #.... tlacidlo ist do menu ....
        self.obr_menu = ImageTk.PhotoImage(Image.open('obrazky/menu.png').resize((50,50)))          
        buttonMenu = tkinter.Button(self.canvas, image= self.obr_menu, command= self.menu_z_hry)
        buttonMenu.configure(activebackground= 'black', bg= 'black', borderwidth= 0) 
        self.buttonMenu = self.canvas.create_window(7, 7, anchor= 'nw', window= buttonMenu)
        #.... tlacidlo ulozit hru ....
        self.obr_ulozit = ImageTk.PhotoImage(Image.open('obrazky/ulozit.png').resize((50,50)))
        buttonUlozit = tkinter.Button(self.canvas, image= self.obr_ulozit, command= self.ponuka_ulozit)
        buttonUlozit.configure(activebackground= 'black', bg = 'black', borderwidth= 0) 
        self.buttonUlozit = self.canvas.create_window(self.sirka-10, 7, anchor= 'ne', window= buttonUlozit)
        #.... tlacidlo zbieranie ....
        self.zbier = ImageTk.PhotoImage(Image.open('obrazky/zbieranie.png').resize((50,50)))
        buttonZbieranie = tkinter.Button(self.canvas, image= self.zbier, command= self.zbieranie)
        buttonZbieranie.configure(activebackground= 'black', bg = 'black', borderwidth= 0) 
        self.buttonZbieranie = self.canvas.create_window(110, 7, anchor= 'nw', window= buttonZbieranie)
        #.... tlacidlo pravidla ....
        self.obr_pravidla = ImageTk.PhotoImage(Image.open('obrazky/pravidla.png').resize((50,50)))
        buttonPravidla_obr = tkinter.Button(self.canvas, image= self.obr_pravidla, command= self.pravidla_z_hry)
        buttonPravidla_obr.configure(activebackground= 'black', bg = 'black', borderwidth= 0) 
        self.buttonPravidla_obr = self.canvas.create_window(60, 7, anchor= 'nw', window= buttonPravidla_obr)

    def ponuka_ulozit(self):
        # ------------ ak prave neprebieha nikoho tah -------------------
        if self.zoznam_hracov[self.kto_je_na_rade[0][1]].kocka.moze_menu and self.ide_casovac:
            self.canvas.delete(self.buttonMenu)
            self.canvas.delete(self.buttonUlozit)
            self.canvas.delete(self.buttonPravidla_obr)
            self.canvas.delete(self.buttonZbieranie)
            self.canvas.unbind('<ButtonPress>')
            self.obr = ImageTk.PhotoImage(Image.open('obrazky/ulozit_hru.png'))
            self.menu = self.canvas.create_image(630, 340, image = self.obr)
            # --------- nacitam obr truhlic ----------------------
            self.obr_tr1 = ImageTk.PhotoImage(Image.open('obrazky/truhlica1u.png').resize((250,250)))
            self.obr_tr2 = ImageTk.PhotoImage(Image.open('obrazky/truhlica2u.png').resize((250,250)))
            self.obr_tr3 = ImageTk.PhotoImage(Image.open('obrazky/truhlica3u.png').resize((250,250)))
            # -------- vytvorim tlacidka ---------------
            #... hra1 ...
            buttonHra1 = tkinter.Button(self.canvas, image= self.obr_tr1, command = self.ulozit1)
            buttonHra1.configure(activebackground= 'black', bg= 'black', borderwidth= 0) 
            self.buttonUlozHra1 = self.canvas.create_window(self.stred[0]-410, self.stred[1]+20, window= buttonHra1)   
            #... hra2 ...
            buttonHra2 = tkinter.Button(self.canvas, image= self.obr_tr2, command = self.ulozit2)
            buttonHra2.configure(activebackground= 'black', bg= 'black', borderwidth= 0) 
            self.buttonUlozHra2 = self.canvas.create_window(self.stred[0]-180, self.stred[1]+200, window= buttonHra2)
            #... hra3 ...
            buttonHra3 = tkinter.Button(self.canvas, image= self.obr_tr3, command = self.ulozit3)
            buttonHra3.configure(activebackground= 'black', bg= 'black', borderwidth= 0) 
            self.buttonUlozHra3 = self.canvas.create_window(self.stred[0]+40, self.stred[1]-10, window= buttonHra3)        
            #....tlacidko spat....
            self.spat = ImageTk.PhotoImage(Image.open('obrazky/vlavo.png').resize((50,50)))          
            buttonSpat = tkinter.Button(self.canvas, image= self.spat, command= self.menu_z_hry) 
            buttonSpat.configure(activebackground= 'black', bg= 'black', font= '"Gill Sans MT" 20', borderwidth= 0) 
            self.buttonSpat = self.canvas.create_window(2, 2, anchor= 'nw', window= buttonSpat)

    def ulozit1(self):
        with open('save1.txt', 'w') as subor:
            for dvojica in self.kto_je_na_rade:                     # kto je na rade
                print(dvojica[0], dvojica[1], file= subor, end= ' ')
            print(file= subor)
            for p in self.nekupene_policka:                         # nekupene policka
                print(p, file= subor, end= ' ')
            print(file= subor)
            for hrac in self.zoznam_hracov:
                print(hrac.peniaze, file= subor)
                print(hrac.pozicia, file= subor)
                if len(hrac.nakupene) == 0:
                    print('nic', file= subor)
                else:
                    for n in hrac.nakupene:
                        print(n, file= subor, end= ' ')
                    print(file= subor)
                print(hrac.meno_postavy, file= subor)
                print(self.slovnik_meno_priezvisko[hrac.meno_postavy], file= subor)
                print(file= subor)
        self.text_ulozene = self.canvas.create_text(self.stred[0]-70, 30, fill= self.zelena, 
        font= '"Gill Sans MT" 20', text= 'ULOŽENÉ')
        self.canvas.after(4000, self.nopockajzajac)                 # po 4 sek zmizne

    def ulozit2(self):
        with open('save2.txt', 'w') as subor:
            for dvojica in self.kto_je_na_rade:                     # kto je na rade
                print(dvojica[0], dvojica[1], file= subor, end= ' ')
            print(file= subor)
            for p in self.nekupene_policka:                         # nekupene policka
                print(p, file= subor, end= ' ')
            print(file= subor)
            for hrac in self.zoznam_hracov:
                print(hrac.peniaze, file= subor)
                print(hrac.pozicia, file= subor)
                if len(hrac.nakupene) == 0:
                    print('nic', file= subor)
                else:
                    for n in hrac.nakupene:
                        print(n, file= subor, end= ' ')
                    print(file= subor)
                print(hrac.meno_postavy, file= subor)
                print(self.slovnik_meno_priezvisko[hrac.meno_postavy], file= subor)
                print(file= subor)
        self.text_ulozene = self.canvas.create_text(self.stred[0]-70, 30, fill= self.zelena, 
        font= '"Gill Sans MT" 20', text= 'ULOŽENÉ')
        self.canvas.after(4000, self.nopockajzajac)                 # po 4 sek zmizne

    def ulozit3(self):
        with open('save3.txt', 'w') as subor:
            for dvojica in self.kto_je_na_rade:                     # kto je na rade
                print(dvojica[0], dvojica[1], file= subor, end= ' ')
            print(file= subor)
            for p in self.nekupene_policka:                         # nekupene policka
                print(p, file= subor, end= ' ')
            print(file= subor)
            for hrac in self.zoznam_hracov:
                print(hrac.peniaze, file= subor)
                print(hrac.pozicia, file= subor)
                if len(hrac.nakupene) == 0:
                    print('nic', file= subor)
                else:
                    for n in hrac.nakupene:
                        print(n, file= subor, end= ' ')
                    print(file= subor)
                print(hrac.meno_postavy, file= subor)
                print(self.slovnik_meno_priezvisko[hrac.meno_postavy], file= subor)
                print(file= subor)
        self.text_ulozene = self.canvas.create_text(self.stred[0]-70, 30, fill= self.zelena, 
        font= '"Gill Sans MT" 20', text= 'ULOŽENÉ')
        self.canvas.after(4000, self.nopockajzajac)                 # po 4 sek zmizne

    def menu_nacitat(self):
        try:
            self.canvas.delete(self.buttonPokracovat)
        except AttributeError:
            pass
        self.canvas.delete(self.buttonNovaHra)
        self.canvas.delete(self.buttonStaraHra)
        self.canvas.delete(self.buttonPravidla)
        self.canvas.delete(self.buttonKoniec)
        self.obr = ImageTk.PhotoImage(Image.open('obrazky/hrat_hru.png'))
        self.menu = self.canvas.create_image(630, 340, image = self.obr)
        # --------- nacitam obr truhlic ----------------------
        self.obr_tr1 = ImageTk.PhotoImage(Image.open('obrazky/truhlica1n.png').resize((250,250)))
        self.obr_tr2 = ImageTk.PhotoImage(Image.open('obrazky/truhlica2n.png').resize((250,250)))
        self.obr_tr3 = ImageTk.PhotoImage(Image.open('obrazky/truhlica3n.png').resize((250,250)))
        # -------- vytvorim tlacidka ---------------
        #... hra1 ...
        buttonHra1 = tkinter.Button(self.canvas, image= self.obr_tr1, command = self.nacitaj1)
        buttonHra1.configure(activebackground= 'black', bg= 'black', borderwidth= 0) 
        self.buttonNacitajHra1 = self.canvas.create_window(self.stred[0]-110, self.stred[1]+20, window= buttonHra1)   
        #... hra2 ...
        buttonHra2 = tkinter.Button(self.canvas, image= self.obr_tr2, command = self.nacitaj2)
        buttonHra2.configure(activebackground= 'black', bg= 'black', borderwidth= 0) 
        self.buttonNacitajHra2 = self.canvas.create_window(self.stred[0]+120, self.stred[1]+200, window= buttonHra2)
        #... hra3 ...
        buttonHra3 = tkinter.Button(self.canvas, image= self.obr_tr3, command = self.nacitaj3)
        buttonHra3.configure(activebackground= 'black', bg= 'black', borderwidth= 0) 
        self.buttonNacitajHra3 = self.canvas.create_window(self.stred[0]+340, self.stred[1]-10, window= buttonHra3)        
        #....tlacidko spat....
        self.spat = ImageTk.PhotoImage(Image.open('obrazky/vlavo.png').resize((50,50)))          
        buttonSpat = tkinter.Button(self.canvas, image= self.spat, command= self.vytvor_menu) 
        buttonSpat.configure(activebackground= 'black', bg= 'black', font= '"Gill Sans MT" 20', borderwidth= 0) 
        self.buttonSpat = self.canvas.create_window(2, 2, anchor= 'nw', window= buttonSpat)
    
    def nacitaj1(self):
        self.canvas.delete(self.buttonNacitajHra1)
        self.canvas.delete(self.buttonNacitajHra2)
        self.canvas.delete(self.buttonNacitajHra3)
        self.canvas.delete(self.buttonSpat)
        # ----- otvorim subor ----------------------
        with open('save1.txt', 'r') as subor:
            kto_je_na_rade = subor.readline()[:-1]
            nekupene_policka = subor.readline()[:-1]
            riadok = subor.readline()
            peniaze = []
            pozicie = []
            nakupene = []
            meno_postavy = []
            meno_hraca = []
            while riadok != '':
                peniaze.append(riadok[:-1])
                pozicie.append(subor.readline()[:-1])
                nakupene.append(subor.readline()[:-1])
                meno_postavy.append(subor.readline()[:-1])
                meno_hraca.append(subor.readline()[:-1])
                riadok = subor.readline()
                riadok = subor.readline()
        # ------- vytvorim slovnik meno_priezvisko a tak hru------
        self.slovnik_meno_priezvisko = {}
        for i in range(len(meno_postavy)):
            self.slovnik_meno_priezvisko[meno_postavy[i]] = meno_hraca[i]
        self.vytvor_plochu()
        # ------- zmenim ostatne udaje ---------------------------
        nekupene_policka = nekupene_policka.split()
        self.nekupene_policka = set()
        for n in nekupene_policka:
            self.nekupene_policka.add(int(n))
        kto_je_na_rade = kto_je_na_rade.split()
        self.kto_je_na_rade = []
        for i in range(0, len(kto_je_na_rade), 2):
            self.kto_je_na_rade.append((kto_je_na_rade[i], int(kto_je_na_rade[i+1])))
        # kedze zoznam hracov sa vytvoril vo vytvor plochu zo slovnika meno priezvisko
        # prechadzam zoznam a menim hodnoty
        for h in self.zoznam_hracov:
            if h.meno_postavy == 'maleficent':
                for m in range(len(meno_postavy)):
                    if meno_postavy[m] == 'maleficent':
                        index = m 
                h.peniaze = int(peniaze[index])
                nakupene_m = nakupene[index].split()
                if nakupene_m[0] != 'nic':
                    for n in nakupene_m:
                        h.nakupene.append(int(n))
                h.pozicia = int(pozicie[index])
            elif h.meno_postavy == 'ursula':
                for m in range(len(meno_postavy)):
                    if meno_postavy[m] == 'ursula':
                        index = m 
                h.peniaze = int(peniaze[index])
                nakupene_m = nakupene[index].split()
                if nakupene_m[0] != 'nic':
                    for n in nakupene_m:
                        h.nakupene.append(int(n))
                h.pozicia = int(pozicie[index])
            elif h.meno_postavy == 'evilqueen':
                for m in range(len(meno_postavy)):
                    if meno_postavy[m] == 'evilqueen':
                        index = m 
                h.peniaze = int(peniaze[index])
                nakupene_m = nakupene[index].split()
                if nakupene_m[0] != 'nic':
                    for n in nakupene_m:
                        h.nakupene.append(int(n))
                h.pozicia = int(pozicie[index])
            elif h.meno_postavy == 'jaffar':
                for m in range(len(meno_postavy)):
                    if meno_postavy[m] == 'jaffar':
                        index = m 
                h.peniaze = int(peniaze[index])
                nakupene_m = nakupene[index].split()
                if nakupene_m[0] != 'nic':
                    for n in nakupene_m:
                        h.nakupene.append(int(n))
                h.pozicia = int(pozicie[index])
            self.canvas.coords(h.o, h.slovnik_pozicii[h.pozicia])
        self.vypis_peniazky()
        self.canvas.delete(self.kocka_plocha)
        self.kocka_plocha = self.canvas.create_image(self.zoznam_hracov[self.kto_je_na_rade[0][1]].Xkocky, 
        self.zoznam_hracov[self.kto_je_na_rade[0][1]].Ykocky, 
        image= self.zoznam_hracov[0].kocka.animacia_hadzanie_kocky[random.randrange(6)])
        # ----- vykreslim policka co maju hraci pokupene ------------------------
        for h in self.zoznam_hracov:
            pozicicia_suradnic = 0
            for p in h.nakupene:
                img = Image.open(f'obrazky/karticky/{p}.png')
                h.obr_karticiek.append(ImageTk.PhotoImage(img))
                h.obr_karticiekTk.append(self.canvas.create_image(h.pozicie_karticiek[pozicicia_suradnic], 
                image= h.obr_karticiek[-1]))
                pozicicia_suradnic += 1

    def nacitaj2(self):
        self.canvas.delete(self.buttonNacitajHra1)
        self.canvas.delete(self.buttonNacitajHra2)
        self.canvas.delete(self.buttonNacitajHra3)
        self.canvas.delete(self.buttonSpat)
        # ----- otvorim subor ----------------------
        with open('save2.txt', 'r') as subor:
            kto_je_na_rade = subor.readline()[:-1]
            nekupene_policka = subor.readline()[:-1]
            riadok = subor.readline()
            peniaze = []
            pozicie = []
            nakupene = []
            meno_postavy = []
            meno_hraca = []
            while riadok != '':
                peniaze.append(riadok[:-1])
                pozicie.append(subor.readline()[:-1])
                nakupene.append(subor.readline()[:-1])
                meno_postavy.append(subor.readline()[:-1])
                meno_hraca.append(subor.readline()[:-1])
                riadok = subor.readline()
                riadok = subor.readline()
        # ------- vytvorim slovnik meno_priezvisko a tak hru------
        self.slovnik_meno_priezvisko = {}
        for i in range(len(meno_postavy)):
            self.slovnik_meno_priezvisko[meno_postavy[i]] = meno_hraca[i]
        self.vytvor_plochu()
        # ------- zmenim ostatne udaje ---------------------------
        nekupene_policka = nekupene_policka.split()
        self.nekupene_policka = set()
        for n in nekupene_policka:
            self.nekupene_policka.add(int(n))
        kto_je_na_rade = kto_je_na_rade.split()
        self.kto_je_na_rade = []
        for i in range(0, len(kto_je_na_rade), 2):
            self.kto_je_na_rade.append((kto_je_na_rade[i], int(kto_je_na_rade[i+1])))
        # kedze zoznam hracov sa vytvoril vo vytvor plochu zo slovnika meno priezvisko
        # prechadzam zoznam a menim hodnoty
        for h in self.zoznam_hracov:
            if h.meno_postavy == 'maleficent':
                for m in range(len(meno_postavy)):
                    if meno_postavy[m] == 'maleficent':
                        index = m 
                h.peniaze = int(peniaze[index])
                nakupene_m = nakupene[index].split()
                if nakupene_m[0] != 'nic':
                    for n in nakupene_m:
                        h.nakupene.append(int(n))
                h.pozicia = int(pozicie[index])
            elif h.meno_postavy == 'ursula':
                for m in range(len(meno_postavy)):
                    if meno_postavy[m] == 'ursula':
                        index = m 
                h.peniaze = int(peniaze[index])
                nakupene_m = nakupene[index].split()
                if nakupene_m[0] != 'nic':
                    for n in nakupene_m:
                        h.nakupene.append(int(n))
                h.pozicia = int(pozicie[index])
            elif h.meno_postavy == 'evilqueen':
                for m in range(len(meno_postavy)):
                    if meno_postavy[m] == 'evilqueen':
                        index = m 
                h.peniaze = int(peniaze[index])
                nakupene_m = nakupene[index].split()
                if nakupene_m[0] != 'nic':
                    for n in nakupene_m:
                        h.nakupene.append(int(n))
                h.pozicia = int(pozicie[index])
            elif h.meno_postavy == 'jaffar':
                for m in range(len(meno_postavy)):
                    if meno_postavy[m] == 'jaffar':
                        index = m 
                h.peniaze = int(peniaze[index])
                nakupene_m = nakupene[index].split()
                if nakupene_m[0] != 'nic':
                    for n in nakupene_m:
                        h.nakupene.append(int(n))
                h.pozicia = int(pozicie[index])
            self.canvas.coords(h.o, h.slovnik_pozicii[h.pozicia])
        self.vypis_peniazky()
        self.canvas.delete(self.kocka_plocha)
        self.kocka_plocha = self.canvas.create_image(self.zoznam_hracov[self.kto_je_na_rade[0][1]].Xkocky, 
        self.zoznam_hracov[self.kto_je_na_rade[0][1]].Ykocky, 
        image= self.zoznam_hracov[0].kocka.animacia_hadzanie_kocky[random.randrange(6)])
        # ----- vykreslim policka co maju hraci pokupene ------------------------
        for h in self.zoznam_hracov:
            pozicicia_suradnic = 0
            for p in h.nakupene:
                img = Image.open(f'obrazky/karticky/{p}.png')
                h.obr_karticiek.append(ImageTk.PhotoImage(img))
                h.obr_karticiekTk.append(self.canvas.create_image(h.pozicie_karticiek[pozicicia_suradnic], 
                image= h.obr_karticiek[-1]))
                pozicicia_suradnic += 1

    def nacitaj3(self):
        self.canvas.delete(self.buttonNacitajHra1)
        self.canvas.delete(self.buttonNacitajHra2)
        self.canvas.delete(self.buttonNacitajHra3)
        self.canvas.delete(self.buttonSpat)
        # ----- otvorim subor ----------------------
        with open('save3.txt', 'r') as subor:
            kto_je_na_rade = subor.readline()[:-1]
            nekupene_policka = subor.readline()[:-1]
            riadok = subor.readline()
            peniaze = []
            pozicie = []
            nakupene = []
            meno_postavy = []
            meno_hraca = []
            while riadok != '':
                peniaze.append(riadok[:-1])
                pozicie.append(subor.readline()[:-1])
                nakupene.append(subor.readline()[:-1])
                meno_postavy.append(subor.readline()[:-1])
                meno_hraca.append(subor.readline()[:-1])
                riadok = subor.readline()
                riadok = subor.readline()
        # ------- vytvorim slovnik meno_priezvisko a tak hru------
        self.slovnik_meno_priezvisko = {}
        for i in range(len(meno_postavy)):
            self.slovnik_meno_priezvisko[meno_postavy[i]] = meno_hraca[i]
        self.vytvor_plochu()
        # ------- zmenim ostatne udaje ---------------------------
        nekupene_policka = nekupene_policka.split()
        self.nekupene_policka = set()
        for n in nekupene_policka:
            self.nekupene_policka.add(int(n))
        kto_je_na_rade = kto_je_na_rade.split()
        self.kto_je_na_rade = []
        for i in range(0, len(kto_je_na_rade), 2):
            self.kto_je_na_rade.append((kto_je_na_rade[i], int(kto_je_na_rade[i+1])))
        # kedze zoznam hracov sa vytvoril vo vytvor plochu zo slovnika meno priezvisko
        # prechadzam zoznam a menim hodnoty
        for h in self.zoznam_hracov:
            if h.meno_postavy == 'maleficent':
                for m in range(len(meno_postavy)):
                    if meno_postavy[m] == 'maleficent':
                        index = m 
                h.peniaze = int(peniaze[index])
                nakupene_m = nakupene[index].split()
                if nakupene_m[0] != 'nic':
                    for n in nakupene_m:
                        h.nakupene.append(int(n))
                h.pozicia = int(pozicie[index])
            elif h.meno_postavy == 'ursula':
                for m in range(len(meno_postavy)):
                    if meno_postavy[m] == 'ursula':
                        index = m 
                h.peniaze = int(peniaze[index])
                nakupene_m = nakupene[index].split()
                if nakupene_m[0] != 'nic':
                    for n in nakupene_m:
                        h.nakupene.append(int(n))
                h.pozicia = int(pozicie[index])
            elif h.meno_postavy == 'evilqueen':
                for m in range(len(meno_postavy)):
                    if meno_postavy[m] == 'evilqueen':
                        index = m 
                h.peniaze = int(peniaze[index])
                nakupene_m = nakupene[index].split()
                if nakupene_m[0] != 'nic':
                    for n in nakupene_m:
                        h.nakupene.append(int(n))
                h.pozicia = int(pozicie[index])
            elif h.meno_postavy == 'jaffar':
                for m in range(len(meno_postavy)):
                    if meno_postavy[m] == 'jaffar':
                        index = m 
                h.peniaze = int(peniaze[index])
                nakupene_m = nakupene[index].split()
                if nakupene_m[0] != 'nic':
                    for n in nakupene_m:
                        h.nakupene.append(int(n))
                h.pozicia = int(pozicie[index])
            self.canvas.coords(h.o, h.slovnik_pozicii[h.pozicia])
        self.vypis_peniazky()
        self.canvas.delete(self.kocka_plocha)
        self.kocka_plocha = self.canvas.create_image(self.zoznam_hracov[self.kto_je_na_rade[0][1]].Xkocky, 
        self.zoznam_hracov[self.kto_je_na_rade[0][1]].Ykocky, 
        image= self.zoznam_hracov[0].kocka.animacia_hadzanie_kocky[random.randrange(6)])
        # ----- vykreslim policka co maju hraci pokupene ------------------------
        for h in self.zoznam_hracov:
            pozicicia_suradnic = 0
            for p in h.nakupene:
                img = Image.open(f'obrazky/karticky/{p}.png')
                h.obr_karticiek.append(ImageTk.PhotoImage(img))
                h.obr_karticiekTk.append(self.canvas.create_image(h.pozicie_karticiek[pozicicia_suradnic], 
                image= h.obr_karticiek[-1]))
                pozicicia_suradnic += 1

    def klik(self, event):
        if len(self.zoznam_hracov) == 0:
            pass
        # ----- ak je na rade ten co je v zalari a klikne na kocku --------------------
        elif (self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia == 40
         and event.x in list(range(self.zoznam_hracov[self.kto_je_na_rade[0][1]].Xkocky-45, 
        self.zoznam_hracov[self.kto_je_na_rade[0][1]].Xkocky+45)) 
        and event.y in list(range(self.zoznam_hracov[self.kto_je_na_rade[0][1]].Ykocky-45, 
        self.zoznam_hracov[self.kto_je_na_rade[0][1]].Ykocky+45))):
            self.canvas.unbind('<ButtonPress>')
            try:
                self.canvas.delete(self.cierna)
            except AttributeError:
                pass
            self.cierna = self.canvas.create_rectangle(418, 150, 875, 553, fill= 'black')           # vytvori ciernu plochu
            self.zoznam_hracov[self.kto_je_na_rade[0][1]].peniaze -= 5                              # odrata peniaze za vykupenie
            self.vypis_peniazky()
            self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia = 10                              # presunie sa na iba na navsteve
            self.canvas.coords(self.zoznam_hracov[self.kto_je_na_rade[0][1]].o, self.zoznam_hracov[self.kto_je_na_rade[0][1]].slovnik_pozicii[self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia])
            self.karticka = self.canvas.create_text(self.stred, text= 'Podplatil/a si čarodejníka. Si voľný/á.', font= '"Gill Sans MT" 20', fill= 'white')
            self.otrasny_cas()                                                                      # text sa objavi na chvilu
        # -------------- ak ide hrac normalne a klikne na kocku, hadze ----------------------------
        elif (event.x in list(range(self.zoznam_hracov[self.kto_je_na_rade[0][1]].Xkocky-45, 
        self.zoznam_hracov[self.kto_je_na_rade[0][1]].Xkocky+45)) 
        and event.y in list(range(self.zoznam_hracov[self.kto_je_na_rade[0][1]].Ykocky-45, 
        self.zoznam_hracov[self.kto_je_na_rade[0][1]].Ykocky+45)) 
        and self.zoznam_hracov[self.kto_je_na_rade[0][1]].pomocna_premenna_pre_casovac == 25):
            self.canvas.unbind('<ButtonPress>')
            self.zoznam_hracov[self.kto_je_na_rade[0][1]].hadze()

    def prepni_hracov(self):
        self.canvas.delete(self.kocka_plocha)       # zmaze obr kocky
        try:
            self.canvas.delete(self.t)
        except AttributeError:
            pass
        isiel = self.kto_je_na_rade.pop(0)          # toho kto prave isiel vyhodi zo zoznamu a da na koniec
        self.kto_je_na_rade.append(isiel)           # nakresli novu kocku pre dalsieho
        self.kocka_plocha = self.canvas.create_image(self.zoznam_hracov[self.kto_je_na_rade[0][1]].Xkocky, self.zoznam_hracov[self.kto_je_na_rade[0][1]].Ykocky, image=self.zoznam_hracov[self.kto_je_na_rade[0][1]].kocka.animacia_hadzanie_kocky[random.randrange(6)])
        self.zoznam_hracov[self.kto_je_na_rade[0][1]].kocka.moze_menu = True        # dokym nehadzal moze sa vratit do menu
        self.zisti_stav()                           # zisti ci niekto nevyhral

    def otrasny_cas(self):
        if self.ide_casovac:
            self.ide_casovac = False
            # -------- ak je hrac vo vazani, text sa ukaze dlhsie --------------
            if self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia == 40: 
                self.canvas.after(5000, self.otrasny_cas)
            # ----------- ak hrac nie je vo vazani staci obr policka na 2s -----
            else:
                self.canvas.after(2000, self.otrasny_cas)
        else:
            self.canvas.delete(self.cierna)
            self.canvas.delete(self.karticka)
            self.canvas.bind('<ButtonPress>', self.klik)
            # -------- ak hrac nehadze znovu, prepnu sa ------------------------
            if self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia not in [5, 15, 25, 35]:
                self.prepni_hracov()
            else:
                self.zoznam_hracov[self.kto_je_na_rade[0][1]].kocka.moze_menu = True
            self.ide_casovac = True

    def vypis_peniazky(self):
        for i in self.zoznam_hracov:
            self.canvas.itemconfig(i.text_peniazky, text= f'{i.peniaze} ₳₳')
                
    #--------POLICKA------------------------
    def policka(self):
        self.cierna = self.canvas.create_rectangle(418, 150, 875, 553, fill= 'black')                       # vytvori sa cierna plocha
        # ------------ policka: start, na navsteve, relax ---------------------------------------------
        if self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia in [0, 10, 20]:       
            # ................ kontrola ci moze vyhrat lebo ma svoju farbu ............................                     
            if self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia == 20 and self.moze_vyhrat(1):
                self.vitaz_t = self.canvas.create_text(self.stred[0], self.stred[1]-50, fill = 'white', font= '"Gill Sans MT" 20',
                text = 'Čarodejnícka rada ti ponúkla pomoc\nso zničením rozprávkového sveta.')
                button_vyhrat = tkinter.Button(self.canvas, text = 'Chcem vyhrať. Prijímam ich ponuku.', command = self.vyhrat)
                button_vyhrat.configure(activebackground= 'white', activeforeground= 'black', 
                fg= 'black', bg= self.silno_ruzova, font= '"Gill Sans MT" 20') 
                self.button_vyhrat = self.canvas.create_window(self.stred[0], self.stred[1]+30, window= button_vyhrat)
            # ................ kontrola ci moze vyhrat lebo ma dost karticiek .........................
            elif self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia == 20 and self.moze_vyhrat():
                self.vitaz_t = self.canvas.create_text(self.stred[0], self.stred[1]-50, fill = 'white', font= '"Gill Sans MT" 20',
                text = 'Čarodejnícka rada ti ponúkla pomoc\nso zničením rozprávkového sveta.\nStačí zaplatiť symbolickú sumu 5 ₳₳.')
                button_vyhrat = tkinter.Button(self.canvas, text = 'Zaplatiť', command = self.zaplatit_vyhrat)
                button_vyhrat.configure(activebackground = 'white', activeforeground = 'black', 
                bd = None, fg = 'black', bg = self.silno_ruzova, font ='"Gill Sans MT" 20') 
                self.button_vyhrat = self.canvas.create_window(self.stred[0], self.stred[1], window= button_vyhrat)
            # ............... inak sa na chvilu zobrazi obr policka ..................................
            else:
                self.pol = ImageTk.PhotoImage(Image.open(f'obrazky/policka/{self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia}.png'))
                self.karticka = self.canvas.create_image(self.stred, image= self.pol)
                self.otrasny_cas()
        # ----------- policko: chod do zalara --------------------------------------------------------
        elif self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia == 30:                                   
            #ukaze sa obrazok policka v strede plochy, panacik sa presunie na poziciu 40 pomocou animacie
            self.pol = ImageTk.PhotoImage(Image.open('obrazky/policka/30.png'))
            self.karticka = self.canvas.create_image(self.stred, image= self.pol)
            self.zoznam_hracov[self.kto_je_na_rade[0][1]].posun(70)        
        # ------------- policko: sanca ----------------------------------------------------------------
        elif self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia in [2, 8, 13, 18, 22, 27, 32, 37]:        
            # nahodne sa vyberie uloha
            cislo_karticky_sanca = random.randrange(19)
            self.sanca = self.canvas.create_text(self.stred[0], self.stred[1]-190, text= '‧͙⁺˚*･༓☾ ŠANCA ☽༓･*˚⁺‧͙', fill= 'white', font ='"Gill Sans MT" 30') 
            if cislo_karticky_sanca == 0:
                # Odhalili ťa. Choď do žalára. Neprejdeš cez štart. Nezískaš 5M. Nedostaneš jesť. 
                button_moznost1 = tkinter.Button(self.canvas, text= 'Odhalili ťa. Choď do žalára.\nNeprejdeš cez štart.\nNezískaš 5 ₳₳. Nedostaneš jesť.', command= self.bez_jedla)
                button_moznost1.configure(activebackground= 'white', activeforeground= 'black', 
                fg= 'black', bg= self.silno_ruzova, font= '"Gill Sans MT" 20') 
                self.button_moznost1= self.canvas.create_window(self.stred[0], self.stred[1]-75, window= button_moznost1)
                # ALEBO
                self.alebo = self.canvas.create_text(self.stred[0], self.stred[1]+25, text= 'ALEBO', fill= 'white', font= '"Gill Sans MT" 20') 
                # Zaplať do kráľovsekej pokladnice 6M.
                button_moznost2 = tkinter.Button(self.canvas, text= 'Zaplať do kráľovskej\npokladnice 6 ₳₳.', command= self.zaplat_do_pokladnice)
                button_moznost2.configure(activebackground= 'white', activeforeground= 'black', 
                fg= 'black', bg= self.modra, font= '"Gill Sans MT" 20') 
                self.button_moznost2 = self.canvas.create_window(self.stred[0], self.stred[1]+110, window= button_moznost2)
            elif cislo_karticky_sanca == 1:
                # Čarodejníckej rade sa zapáčil tvoj nápad. Prevezmi si 4M.
                self.t = self.canvas.create_text(self.stred[0], self.stred[1]-25, text= 'Čarodejníckej rade sa zapáčil tvoj nápad.\nPosielajú ti odmenu. Prevezmi si 4 ₳₳.',
                font= '"Gill Sans MT" 20', fill= 'white')
                button_prevziat = tkinter.Button(self.canvas, text= 'Prevziať', command= self.prevziat_penezi)
                button_prevziat.configure(activebackground= 'white', activeforeground= 'black', 
                fg= 'black', bg= self.zelena, font= '"Gill Sans MT" 20') 
                self.button_prevziat = self.canvas.create_window(self.stred[0], self.stred[1]+50, window= button_prevziat)
            elif cislo_karticky_sanca == 2:
                # Zaplať 2M a hádž znovu 
                button_moznost1 = tkinter.Button(self.canvas, text= 'Zaplať 2 ₳₳ a hádž znovu.', command= self.zaplat_hadz)
                button_moznost1.configure(activebackground= 'white', activeforeground= 'black', 
                fg= 'black', bg= self.modra, font= '"Gill Sans MT" 20', width= 20) 
                self.button_moznost1 = self.canvas.create_window(self.stred[0], self.stred[1]-75, window= button_moznost1)
                # ALEBO
                self.alebo = self.canvas.create_text(self.stred, text= 'ALEBO', fill= 'white', font= '"Gill Sans MT" 20') 
                # Zaplať 1M a ostaň stáť.
                button_moznost2 = tkinter.Button(self.canvas, text= 'Zaplať 1 ₳₳ a ostaň stáť.', command= self.zaplat_stoj)
                button_moznost2.configure(activebackground= 'white', activeforeground= 'black', 
                fg= 'black', bg= self.zelena, font= '"Gill Sans MT" 20', width= 20) 
                self.button_moznost2 = self.canvas.create_window(self.stred[0], self.stred[1]+75, window= button_moznost2)
            elif cislo_karticky_sanca == 3:
                # Urob krok vpred. 
                button_moznost1 = tkinter.Button(self.canvas, text = 'Urob krok vpred.', command = self.krok_vpred)
                button_moznost1.configure(activebackground = 'white', activeforeground = 'black', 
                bd = None, fg = 'black', bg = self.modra, font ='"Gill Sans MT" 20', width= 16) 
                self.button_moznost1 = self.canvas.create_window(self.stred[0], self.stred[1]-75, window= button_moznost1)
                # ALEBO
                self.alebo = self.canvas.create_text(630, 340, text= 'ALEBO', fill= 'white', font ='"Gill Sans MT" 20') 
                # Urob krok späť.
                button_moznost2 = tkinter.Button(self.canvas, text= 'Urob krok späť.', command = self.krok_spat)
                button_moznost2.configure(activebackground = 'white', activeforeground = 'black', 
                bd = None, fg = 'black', bg = self.silno_ruzova, font ='"Gill Sans MT" 20', width= 16) 
                self.button_moznost2 = self.canvas.create_window(self.stred[0], self.stred[1]+75, window= button_moznost2)
            elif cislo_karticky_sanca == 4:
                # Našiel/la si cudzí mešec plný dukátov. Koho asi sú?
                self.t = self.canvas.create_text(self.stred[0], self.stred[1]-50, text= '   Našiel/la si cudzí\nmešec plný dukátov.\n     Koho asi sú?', fill= 'white', font ='"Gill Sans MT" 20')
                button_zdvihnut = tkinter.Button(self.canvas, text= 'Zdvihnúť mešec', command= self.zdvihnut)
                button_zdvihnut.configure(activebackground= 'white', activeforeground= 'black', 
                fg= 'black', bg= self.silno_ruzova, font= '"Gill Sans MT" 20') 
                self.button_zdvihnut = self.canvas.create_window(self.stred[0], self.stred[1]+50, window= button_zdvihnut)
            elif cislo_karticky_sanca == 5:
                # Stratil si mesec plny dukatov.
                self.t = self.canvas.create_text(self.stred[0], self.stred[1]-50, text= '  Stratil/a si mešec plný\ndukátov. Kto ich našiel?', fill= 'white', font ='"Gill Sans MT" 20')
                button_fnuk = tkinter.Button(self.canvas, text= 'Fňuk', command= self.fnuk)
                button_fnuk.configure(activebackground= 'white', activeforeground= 'black', 
                fg= 'black', bg= self.zlta, font= '"Gill Sans MT" 20') 
                self.button_zdvihnut = self.canvas.create_window(self.stred[0], self.stred[1]+50, window= button_fnuk)
            elif cislo_karticky_sanca == 6:
                # Odhalili tvoje plány. Choď do žalára. Neprejdeš cez štart. Nezískaš 2M.
                self.t = self.canvas.create_text(self.stred[0], self.stred[1]-50, text= 'Odhalili tvoje plány.\n   Choď do žalára.\nNeprejdeš cez štart.\n     Nezískaš 5 ₳₳.', 
                fill= 'white', font= '"Gill Sans MT" 20')
                button_ist_do_zalara = tkinter.Button(self.canvas, text= 'Ísť do žalára', command= self.do_zalara)
                button_ist_do_zalara.configure(activebackground= 'white', activeforeground= 'black', 
                fg= 'black', bg= self.zlta, font= '"Gill Sans MT" 20') 
                self.button_ist_do_zalara = self.canvas.create_window(self.stred[0], self.stred[1]+80, window= button_ist_do_zalara)
            elif cislo_karticky_sanca == 7:
                # Prichytili ťa pri čine. Zaplať do kráľovsekej pokladnice 3M.
                self.t = self.canvas.create_text(self.stred[0], self.stred[1]-50, text= '           Prichytili ťa pri čine.\nZaplať do kráľovskej pokladnice 3 ₳₳.', 
                fill= 'white', font= '"Gill Sans MT" 20')
                button_zaplatit_pokutu = tkinter.Button(self.canvas, text= 'Zaplatiť', command= self.zaplatit_pokutu)
                button_zaplatit_pokutu.configure(activebackground= 'white', activeforeground= 'black', 
                fg= 'black', bg= self.zelena, font= '"Gill Sans MT" 20') 
                self.button_zaplatit_pokutu = self.canvas.create_window(self.stred[0], self.stred[1]+50, window= button_zaplatit_pokutu)
            elif cislo_karticky_sanca == 8:
                # Vedia, čo máš zalubom. Utekaj! Posuň sa o 3 políčka vpred.
                self.t = self.canvas.create_text(self.stred[0], self.stred[1]-50, text= '  Vedia, čo máš zalubom.\n              Utekaj!\nPosuň sa o 3 políčka vpred.', 
                fill= 'white', font= '"Gill Sans MT" 20')
                button_utekat = tkinter.Button(self.canvas, text= 'Utekať', command= self.utekat)
                button_utekat.configure(activebackground= 'white', activeforeground= 'black', 
                fg= 'black', bg= self.modra, font= '"Gill Sans MT" 20') 
                self.button_utekat = self.canvas.create_window(self.stred[0], self.stred[1]+70, window= button_utekat)
            elif cislo_karticky_sanca == 9:
                # Vypadol ti mozog z hlavy.
                self.t = self.canvas.create_text(self.stred[0], self.stred[1]-100, text= 'Vypadol ti mozog z hlavy.', fill= 'white', font ='"Gill Sans MT" 20')
                # Vráť sa poň 4 políčka dozadu. 
                button_moznost1 = tkinter.Button(self.canvas, text= 'Vráť sa poň 4 políčka dozadu', command= self.mozog_vratit)
                button_moznost1.configure(activebackground = 'white', activeforeground = 'black', 
                fg= 'black', bg= self.modra, font= '"Gill Sans MT" 20', width= 23) 
                self.button_moznost1 = self.canvas.create_window(self.stred[0], self.stred[1]-30, window= button_moznost1)
                # ALEBO
                self.alebo = self.canvas.create_text(self.stred[0], self.stred[1]+30, text= 'ALEBO', fill= 'white', font= '"Gill Sans MT" 20') 
                # Pokračuj 3 políčka bez neho a vynechaj ďalšie kolo.
                button_moznost2 = tkinter.Button(self.canvas, text= 'Zaplať 4 ₳₳ a kúp si nový', command= self.bez_mozgu)
                button_moznost2.configure(activebackground= 'white', activeforeground= 'black', 
                fg= 'black', bg= self.silno_ruzova, font= '"Gill Sans MT" 20', width= 23) 
                self.button_moznost2 = self.canvas.create_window(self.stred[0], self.stred[1]+90, window= button_moznost2)
            elif cislo_karticky_sanca == 10:
                # Zle si vyriekla/ol zaklínadlo. Presuň sa na štart.
                self.t = self.canvas.create_text(self.stred[0], self.stred[1]-50, text= 'Zle si vyriekla/ol zaklínadlo.\n      Presuň sa na štart.', fill= 'white', font ='"Gill Sans MT" 20')
                button_presun_start = tkinter.Button(self.canvas, text= 'Presunúť sa na štart', command= self.presun_start)
                button_presun_start.configure(activebackground= 'white', activeforeground= 'black', 
                fg= 'black', bg= self.zelena, font= '"Gill Sans MT" 20') 
                self.button_presun_start = self.canvas.create_window(self.stred[0], self.stred[1]+25, window= button_presun_start)
            elif cislo_karticky_sanca == 11:
                # Choď na políčko
                self.t = self.canvas.create_text(self.stred[0], self.stred[1]-100, text= 'Choď na políčko', fill= 'white', font= '"Gill Sans MT" 20')
                button_moznost1 = tkinter.Button(self.canvas, text= 'Zrkadlo', command= self.presun_zrkadlo)
                button_moznost1.configure(activebackground= 'white', activeforeground= 'black', 
                fg= 'black', bg= self.zlta, font= '"Gill Sans MT" 20', width= 8) 
                self.button_moznost1 = self.canvas.create_window(self.stred[0], self.stred[1]-30, window= button_moznost1)
                # ALEBO
                self.alebo = self.canvas.create_text(self.stred[0], self.stred[1]+40, text= 'ALEBO', fill= 'white', font ='"Gill Sans MT" 20') 
                # na toto policko
                button_moznost2 = tkinter.Button(self.canvas, text= 'princ Erik', command= self.presun_erik)
                button_moznost2.configure(activebackground = 'white', activeforeground= 'black', 
                fg ='black', bg= self.zelena, font= '"Gill Sans MT" 20', width= 8) 
                self.button_moznost2 = self.canvas.create_window(self.stred[0], self.stred[1]+110, window= button_moznost2)
            elif cislo_karticky_sanca == 12:
                # Choď na políčko
                self.t = self.canvas.create_text(self.stred[0], self.stred[1]-100, text= 'Choď na políčko', fill= 'white', font= '"Gill Sans MT" 20')
                button_moznost1 = tkinter.Button(self.canvas, text= 'Trpaslíci', command= self.presun_trpaslici)
                button_moznost1.configure(activebackground= 'white', activeforeground= 'black', 
                fg= 'black', bg= self.zlta, font= '"Gill Sans MT" 20', width= 8) 
                self.button_moznost1 = self.canvas.create_window(self.stred[0], self.stred[1]-30, window= button_moznost1)
                # ALEBO
                self.alebo = self.canvas.create_text(self.stred[0], self.stred[1]+40, text= 'ALEBO', fill= 'white', font= '"Gill Sans MT" 20') 
                # na toto policko
                button_moznost2 = tkinter.Button(self.canvas, text= 'Jasmína', command= self.presun_jasmina)
                button_moznost2.configure(activebackground= 'white', activeforeground= 'black', 
                fg= 'black', bg= self.modra, font= '"Gill Sans MT" 20', width= 8) 
                self.button_moznost2 = self.canvas.create_window(self.stred[0], self.stred[1]+110, window= button_moznost2)
            elif cislo_karticky_sanca == 13:
                # Choď na políčko
                self.t = self.canvas.create_text(self.stred[0], self.stred[1]-100, text= 'Choď na políčko', fill= 'white', font ='"Gill Sans MT" 20')
                button_moznost1 = tkinter.Button(self.canvas, text= 'Aladin', command= self.presun_aladin)
                button_moznost1.configure(activebackground= 'white', activeforeground= 'black', 
                fg= 'black', bg = self.modra, font= '"Gill Sans MT" 20', width= 8) 
                self.button_moznost1 = self.canvas.create_window(self.stred[0], self.stred[1]-30, window= button_moznost1)
                # ALEBO
                self.alebo = self.canvas.create_text(self.stred[0], self.stred[1]+40, text= 'ALEBO', fill= 'white', font= '"Gill Sans MT" 20') 
                # na toto policko
                button_moznost2 = tkinter.Button(self.canvas, text= 'Sebastian', command= self.presun_sebastian)
                button_moznost2.configure(activebackground= 'white', activeforeground= 'black', 
                fg= 'black', bg= self.zelena, font= '"Gill Sans MT" 20', width= 8) 
                self.button_moznost2 = self.canvas.create_window(self.stred[0], self.stred[1]+110, window= button_moznost2)
            elif cislo_karticky_sanca == 14:
                # Choď na políčko
                self.t = self.canvas.create_text(self.stred[0], self.stred[1]-100, text= 'Choď na políčko', fill= 'white', font= '"Gill Sans MT" 20')
                button_moznost1 = tkinter.Button(self.canvas, text= 'Jablko', command= self.presun_jablko)
                button_moznost1.configure(activebackground= 'white', activeforeground= 'black', 
                fg= 'black', bg= self.zlta, font= '"Gill Sans MT" 20', width= 9) 
                self.button_moznost1 = self.canvas.create_window(self.stred[0], self.stred[1]-30, window= button_moznost1)
                # ALEBO
                self.alebo = self.canvas.create_text(self.stred[0], self.stred[1]+40, text= 'ALEBO', fill= 'white', font= '"Gill Sans MT" 20') 
                # na toto policko
                button_moznost2 = tkinter.Button(self.canvas, text= 'Kolovrátok', command= self.presun_kolovratok)
                button_moznost2.configure(activebackground= 'white', activeforeground= 'black', 
                fg= 'black', bg= self.silno_ruzova, font= '"Gill Sans MT" 20', width= 9) 
                self.button_moznost2 = self.canvas.create_window(self.stred[0], self.stred[1]+110, window= button_moznost2)
            elif cislo_karticky_sanca == 15:
                # Choď na políčko
                self.t = self.canvas.create_text(self.stred[0], self.stred[1]-100, text= 'Choď na políčko', fill= 'white', font= '"Gill Sans MT" 20')
                button_moznost1 = tkinter.Button(self.canvas, text= 'Havrany', command= self.presun_havrany)
                button_moznost1.configure(activebackground= 'white', activeforeground= 'black', 
                fg= 'black', bg= self.silno_ruzova, font= '"Gill Sans MT" 20', width= 8) 
                self.button_moznost1 = self.canvas.create_window(self.stred[0], self.stred[1]-30, window= button_moznost1)
                # ALEBO
                self.alebo = self.canvas.create_text(self.stred[0], self.stred[1]+40, text= 'ALEBO', fill= 'white', font= '"Gill Sans MT" 20') 
                # na toto policko
                button_moznost2 = tkinter.Button(self.canvas, text= 'Jago', command= self.presun_jago)
                button_moznost2.configure(activebackground= 'white', activeforeground= 'black', 
                fg= 'black', bg= self.modra, font= '"Gill Sans MT" 20', width= 8) 
                self.button_moznost2 = self.canvas.create_window(self.stred[0], self.stred[1]+110, window= button_moznost2)
            elif cislo_karticky_sanca == 16:
                # Choď na políčko
                self.t = self.canvas.create_text(self.stred[0], self.stred[1]-100, text= 'Choď na políčko', fill= 'white', font= '"Gill Sans MT" 20')
                button_moznost1 = tkinter.Button(self.canvas, text= 'Vtáčiky', command= self.presun_vtaciky)
                button_moznost1.configure(activebackground= 'white', activeforeground= 'black', 
                fg= 'black', bg= self.silno_ruzova, font= '"Gill Sans MT" 20', width= 8) 
                self.button_moznost1 = self.canvas.create_window(self.stred[0], self.stred[1]-30, window= button_moznost1)
                # ALEBO
                self.alebo = self.canvas.create_text(self.stred[0], self.stred[1]+40, text= 'ALEBO', fill= 'white', font= '"Gill Sans MT" 20') 
                # na toto policko
                button_moznost2 = tkinter.Button(self.canvas, text= 'Ariel', command= self.presun_ariel)
                button_moznost2.configure(activebackground= 'white', activeforeground= 'black', 
                fg= 'black', bg= self.zelena, font= '"Gill Sans MT" 20', width= 8) 
                self.button_moznost2 = self.canvas.create_window(self.stred[0], self.stred[1]+110, window= button_moznost2)
            elif cislo_karticky_sanca == 17:
                # Choď na políčko
                self.t = self.canvas.create_text(self.stred[0], self.stred[1]-100, text= 'Choď na políčko', fill= 'white', font= '"Gill Sans MT" 20')
                button_moznost1 = tkinter.Button(self.canvas, text= 'Šaty Snehulienky', command= self.presun_saty_sneh)
                button_moznost1.configure(activebackground= 'white', activeforeground= 'black', 
                fg= 'black', bg= self.zlta, font= '"Gill Sans MT" 20', width= 13) 
                self.button_moznost1 = self.canvas.create_window(self.stred[0], self.stred[1]-30, window= button_moznost1)
                # ALEBO
                self.alebo = self.canvas.create_text(self.stred[0], self.stred[1]+40, text= 'ALEBO', fill= 'white', font= '"Gill Sans MT" 20') 
                # na toto policko
                button_moznost2 = tkinter.Button(self.canvas, text= 'Rajah', command= self.presun_rajah)
                button_moznost2.configure(activebackground= 'white', activeforeground= 'black', 
                fg= 'black', bg= self.modra, font= '"Gill Sans MT" 20', width= 13) 
                self.button_moznost2 = self.canvas.create_window(self.stred[0], self.stred[1]+110, window= button_moznost2)
            elif cislo_karticky_sanca == 18:
                # Choď na políčko
                self.t = self.canvas.create_text(self.stred[0], self.stred[1]-100, text= 'Choď na políčko', fill= 'white', font= '"Gill Sans MT" 20')
                button_moznost1 = tkinter.Button(self.canvas, text= 'princ Filip', command= self.presun_filip)
                button_moznost1.configure(activebackground= 'white', activeforeground= 'black', 
                fg= 'black', bg= self.silno_ruzova, font= '"Gill Sans MT" 20', width= 8) 
                self.button_moznost1 = self.canvas.create_window(self.stred[0], self.stred[1]-30, window= button_moznost1)
                # ALEBO
                self.alebo = self.canvas.create_text(self.stred[0], self.stred[1]+40, text= 'ALEBO', fill= 'white', font= '"Gill Sans MT" 20') 
                # na toto policko
                button_moznost2 = tkinter.Button(self.canvas, text= 'Úhory', command= self.presun_uhory)
                button_moznost2.configure(activebackground= 'white', activeforeground= 'black', 
                fg= 'black', bg= self.zelena, font= '"Gill Sans MT" 20', width= 8) 
                self.button_moznost2 = self.canvas.create_window(self.stred[0], self.stred[1]+110, window= button_moznost2)
        # ----------------------- policko: hadz znovu -----------------------------------------------
        elif self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia in [5, 15, 25, 35]:                      
            #zjavi sa obrazok policka v strede na chvilu
            self.pol = ImageTk.PhotoImage(Image.open(f'obrazky/policka/hadz.png'))
            self.karticka = self.canvas.create_image(self.stred, image= self.pol)
            self.otrasny_cas()
        # ------------------------ policka na kupenie ---------------------------------------------
        else:                                                                                                   
            #zjavi sa obrazok policka v strede s cenou a moznostou kupit 
            self.pol = ImageTk.PhotoImage(Image.open(f'obrazky/policka/{self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia}.png'))
            self.karticka = self.canvas.create_image(self.stred, image= self.pol)
            self.kupit = ImageTk.PhotoImage(Image.open('obrazky/kupit.png').resize((50,50)))
            self.nekupit = ImageTk.PhotoImage(Image.open('obrazky/nekupit.png').resize((50,50)))
            # ... zisti cenu ...
            for kluc in self.cennik:
                if self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia in kluc:
                    cena = self.cennik[kluc]
            # ... ak sa da kupit ....
            if self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia in self.nekupene_policka:
                self.cena = self.canvas.create_text(self.stred[0], self.stred[1]-220, text= f'{cena} ₳₳', font= '"Gill Sans MT" 30', fill= 'white')
                button_kupit = tkinter.Button(self.canvas, image= self.kupit, command= self.overit_kupu)
                button_kupit.configure(activebackground= 'black', activeforeground= 'black', 
                borderwidth= 0, bg= 'black')
                self.button_kupit = self.canvas.create_window(460,self.stred[1], window= button_kupit)
                button_nekupit = tkinter.Button(self.canvas, image= self.nekupit, command= self.ne_kupit)
                button_nekupit.configure(activebackground= 'black', activeforeground= 'black', 
                borderwidth= 0, bg= 'black')
                self.button_nekupit = self.canvas.create_window(820,self.stred[1], window= button_nekupit)
            # ... ak sa neda kupit ....
            else:
                # .... ak je vlastne po case zmizne ...
                if self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia in self.zoznam_hracov[self.kto_je_na_rade[0][1]].nakupene:
                    self.canvas.after(2000, self.ne_kupit)
                # ... plati sa pokuta ...
                else:
                    self.cena = self.canvas.create_text(self.stred[0], self.stred[1]-220, text= f'Požičanie: {int(cena)//2} ₳₳', font= '"Gill Sans MT" 30', fill= 'white')
                    button_pozicanie = tkinter.Button(self.canvas, image= self.kupit, command= self.pozicanie)
                    button_pozicanie.configure(activebackground= 'black', activeforeground= 'black', 
                    borderwidth= 0, bg= 'black') 
                    self.button_pozicanie = self.canvas.create_window(820, self.stred[1], window= button_pozicanie)

    def moze_vyhrat(self, typ= 0):
        self.cennik = {(7, 17, 23, 33): 15, (1, 16, 26, 34): 10, (3, 4, 11, 29): 8, (12, 19, 21, 36): 7, (9, 24, 31, 39): 6, (6, 14, 28, 38): 5}
        if typ == 0:
            princezna, princ, kamarati, zvierata, sila, saty = False, False, False, False, False, False
            for pozemok in self.zoznam_hracov[self.kto_je_na_rade[0][1]].nakupene:
                if pozemok in [7, 17, 23, 33]:                  # princezne
                    princezna = True
                elif pozemok in [1, 16, 26, 34]:
                    princ = True
                elif pozemok in [3, 4, 11, 29]:
                    kamarati = True
                elif pozemok in [12, 19, 21, 36]:
                    zvierata = True
                elif pozemok in [9, 24, 31, 39]: 
                    sila = True
                elif pozemok in [6, 14, 28, 38]: 
                    saty = True
            return (princezna and princ and kamarati and zvierata and sila and saty)    
        elif typ == 1:
            su_polia = True
            m = self.zoznam_hracov[self.kto_je_na_rade[0][1]].meno_postavy
            if m == 'evilqueen':
                zoznam_poli = [1, 9, 14, 23, 29, 36]
            elif m == 'ursula':
                zoznam_poli = [3, 6, 16, 21, 33, 39]
            elif m == 'jaffar':
                zoznam_poli = [7, 11, 19, 26, 31, 38]
            elif m == 'maleficent':
                zoznam_poli = [4, 12, 17, 24, 28, 34]
            for pozemok in zoznam_poli:
                if pozemok not in self.zoznam_hracov[self.kto_je_na_rade[0][1]].nakupene:
                    su_polia = False
            return su_polia              

    def vyhrat(self):
        self.canvas.delete(self.button_vyhrat)
        self.canvas.delete(self.cierna)
        pozicia = self.kto_je_na_rade[0][1]
        for i in range(len(self.zoznam_hracov)-1, 0, -1):
            if i != pozicia:
                self.zoznam_hracov.pop(i)
        self.zisti_stav()
    
    def zaplatit_vyhrat(self):
        self.canvas.delete(self.button_vyhrat)
        if self.zoznam_hracov[self.kto_je_na_rade[0][1]].peniaze < 5:
            self.t = self.canvas.create_text(self.stred, text= 'Fnuk. Nemas dost dukatov. Mozno nabuduce.', fill = 'white', font='"Gill Sans MT" 20')
            self.canvas.after(4000, self.prepni_hracov)
        else:
            self.zoznam_hracov[self.kto_je_na_rade[0][1]].peniaze -= 5
            self.vypis_peniazky()
            self.vyhrat()

    def zisti_stav(self):
        for i in range(len(self.zoznam_hracov)):
            if self.zoznam_hracov[i].peniaze < 0:
                for pozemok in self.zoznam_hracov[i].nakupene:
                    self.nekupene_policka.add(pozemok)
                m = self.zoznam_hracov[i].meno_postavy
                self.zoznam_hracov[i].peniaze = 0
                self.vypis_peniazky()
                for o in self.zoznam_hracov[i].obr_karticiekTk:
                    self.canvas.delete(o)
                if m == 'evilqueen':
                    self.krach_e = ImageTk.PhotoImage(Image.open('obrazky/krach.png').resize((558, 300)))
                    self.prehra_e = self.canvas.create_image(165, 213, image = self.krach_e)
                elif m == 'ursula':
                    self.krach_u = ImageTk.PhotoImage(Image.open('obrazky/krach.png').resize((558, 300)))
                    self.prehra_u = self.canvas.create_image(165, 519, image = self.krach_u)
                elif m == 'jaffar':
                    self.krach_j = ImageTk.PhotoImage(Image.open('obrazky/krach.png').resize((558, 300)))
                    self.prehra_j = self.canvas.create_image(1130, 211, image = self.krach_j)
                elif m == 'maleficent':
                    self.krach_m = ImageTk.PhotoImage(Image.open('obrazky/krach.png').resize((558, 300)))
                    self.prehra_m = self.canvas.create_image(1130, 518, image = self.krach_m)

                for j in range(len(self.kto_je_na_rade)):
                    if self.kto_je_na_rade[j][1] == i:
                        index = j
                for postavicka in range(len(self.kto_je_na_rade)):
                    if self.kto_je_na_rade[postavicka][1] > i:
                        self.kto_je_na_rade[postavicka] = (self.kto_je_na_rade[postavicka][0], self.kto_je_na_rade[postavicka][1]-1)
                self.kto_je_na_rade.pop(index)
                self.canvas.delete(self.zoznam_hracov[i].o)
                self.zoznam_hracov.pop(i)
                break
        if len(self.zoznam_hracov) == 1:
            self.cierna = self.canvas.create_rectangle(418, 150, 875, 553, fill= 'black')
            meno =  self.zoznam_hracov[0].meno_postavy 
            self.pozadie_v = ImageTk.PhotoImage(Image.open(f'obrazky/vitaz_{meno}.png'))
            self.p_v = self.canvas.create_image(self.stred, image= self.pozadie_v)
            self.vitaz = ImageTk.PhotoImage(Image.open('obrazky/konfety.png').resize((475,475)))
            self.kon = self.canvas.create_image(self.stred, image= self.vitaz)
            self.canvas.create_text(self.stred[0]-100, self.stred[1]+50, text= 'VÍŤAZ:', fill = 'white', font='"Gill Sans MT" 20')  
            self.canvas.create_text(self.stred[0]-100, self.stred[1]+120, text=self.slovnik_meno_priezvisko[meno], fill = 'white', font='"Gill Sans MT" 70')  
  
    def pozicanie(self):
        for i in range(len(self.zoznam_hracov)):
            if self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia in self.zoznam_hracov[i].nakupene:
                index = i
        for kluc in self.cennik:
            if self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia in kluc:
                cena = self.cennik[kluc]
        if self.zoznam_hracov[self.kto_je_na_rade[0][1]].peniaze < int(cena//2):
            self.zoznam_hracov[index].peniaze += self.zoznam_hracov[self.kto_je_na_rade[0][1]].peniaze
            self.zoznam_hracov[self.kto_je_na_rade[0][1]].peniaze = -1
        else:
            self.zoznam_hracov[index].peniaze += int(cena//2)
            self.zoznam_hracov[self.kto_je_na_rade[0][1]].peniaze -= int(cena//2)
        self.vypis_peniazky()
        self.canvas.delete(self.button_pozicanie)
        self.ne_kupit()

    def ne_kupit(self):
        self.canvas.delete(self.cierna)
        try:
            self.canvas.delete(self.cena)
            self.canvas.delete(self.button_kupit)
            self.canvas.delete(self.button_nekupit)
            self.canvas.delete(self.nemas_peniazky)
        except AttributeError:
            pass
        self.canvas.delete(self.karticka)
        self.canvas.bind('<ButtonPress>', self.klik)
        self.prepni_hracov()

    def overit_kupu(self):
        # ------------- zistim cenu ----------------
        for kluc in self.cennik:
            if self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia in kluc:
                cena = self.cennik[kluc]
        # ci mam dost penazi, ak nie napise text a pojde dalsi cez ne_kupit
        if self.zoznam_hracov[self.kto_je_na_rade[0][1]].peniaze < cena:
            self.canvas.delete(self.button_kupit)
            self.canvas.delete(self.button_nekupit)
            self.nemas_peniazky = self.canvas.create_text(self.stred[0], self.stred[1]+220, text= 'Fňuk. Nemáš dosť zlatiek. Možno nabudúce.', 
            font ='"Gill Sans MT" 19', fill= 'red')
            self.canvas.after(4000, self.ne_kupit)
        # ak ano odrata peniazky prida policko a zavola ne_kupit aby siel dalsi
        else:
            self.zoznam_hracov[self.kto_je_na_rade[0][1]].peniaze -= cena
            self.vypis_peniazky()
            self.zoznam_hracov[self.kto_je_na_rade[0][1]].nakupene.append(self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia)
            self.nekupene_policka.remove(self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia)
            self.vykresli_karticky()
            self.ne_kupit()

    def vykresli_karticky(self):
        p = self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia
        img = Image.open(f'obrazky/karticky/{p}.png')
        pozicicia_suradnic = len(self.zoznam_hracov[self.kto_je_na_rade[0][1]].nakupene)-1
        if self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicie_karticiek[pozicicia_suradnic][1] + 64 > 355 and (self.zoznam_hracov[self.kto_je_na_rade[0][1]].meno_postavy == 'evilqueen' or self.zoznam_hracov[self.kto_je_na_rade[0][1]] == 'jaffar'):
            d = self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicie_karticiek[pozicicia_suradnic][1] + 64 - 355
            img = img.crop([0,0,75,128-d])
        elif self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicie_karticiek[pozicicia_suradnic][1] + 64 > 660 and (self.zoznam_hracov[self.kto_je_na_rade[0][1]].meno_postavy == 'maleficent' or self.zoznam_hracov[self.kto_je_na_rade[0][1]] == 'ursula'):
            d = self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicie_karticiek[pozicicia_suradnic][1] + 64 - 660
            img = img.crop([0,0,75,128-d])
        self.zoznam_hracov[self.kto_je_na_rade[0][1]].obr_karticiek.append(ImageTk.PhotoImage(img))
        self.zoznam_hracov[self.kto_je_na_rade[0][1]].obr_karticiekTk.append(self.canvas.create_image(self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicie_karticiek[pozicicia_suradnic], 
        image= self.zoznam_hracov[self.kto_je_na_rade[0][1]].obr_karticiek[-1]))

    def bez_jedla(self):
        try:
            self.canvas.delete(self.button_moznost1)
            self.canvas.delete(self.button_moznost2)
            self.canvas.delete(self.alebo)
        except AttributeError:
            pass
        try:
            self.canvas.delete(self.nemas_peniazky)
        except AttributeError:
            pass        
        self.canvas.delete(self.cierna)
        self.canvas.delete(self.sanca)
        self.zoznam_hracov[self.kto_je_na_rade[0][1]].posun(100 - self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia)
        self.canvas.bind('<ButtonPress>', self.klik)

    def zaplat_do_pokladnice(self):
        self.canvas.delete(self.button_moznost1)
        self.canvas.delete(self.button_moznost2)
        self.canvas.delete(self.alebo)
        if self.zoznam_hracov[self.kto_je_na_rade[0][1]].peniaze >= 6:
            self.zoznam_hracov[self.kto_je_na_rade[0][1]].peniaze -= 6
            self.vypis_peniazky()
            self.canvas.delete(self.cierna)
            self.canvas.delete(self.sanca)
            self.canvas.bind('<ButtonPress>', self.klik)
            self.prepni_hracov()
        else:
            self.nemas_peniazky = self.canvas.create_text(self.stred, text= 'Fňuk. Nemáš dosť zlatiek.', 
            font ='"Gill Sans MT" 20', fill= 'red')
            self.canvas.after(4000, self.bez_jedla)

    def prevziat_penezi(self):
        self.canvas.delete(self.button_prevziat)
        self.canvas.delete(self.t)
        self.zoznam_hracov[self.kto_je_na_rade[0][1]].peniaze += 4
        self.vypis_peniazky()
        self.canvas.delete(self.cierna)
        self.canvas.delete(self.sanca)
        self.canvas.bind('<ButtonPress>', self.klik)
        self.prepni_hracov()        

    def zaplat_hadz(self):
        self.canvas.delete(self.button_moznost1)
        self.canvas.delete(self.button_moznost2)
        self.canvas.delete(self.alebo)
        if self.zoznam_hracov[self.kto_je_na_rade[0][1]].peniaze >= 2:
            self.zoznam_hracov[self.kto_je_na_rade[0][1]].peniaze -= 2
            self.vypis_peniazky()
            self.canvas.delete(self.cierna)
            self.canvas.delete(self.sanca)
            self.canvas.bind('<ButtonPress>', self.klik) 
        else:
            self.nemas_peniazky = self.canvas.create_text(self.stred, text= 'Fňuk. Nemáš dosť zlatiek.', 
            font ='"Gill Sans MT" 20', fill= 'red')
            self.canvas.after(4000, self.zaplat_stoj)

    def zaplat_stoj(self):
        try:
            self.canvas.delete(self.button_moznost1)
            self.canvas.delete(self.button_moznost2)
            self.canvas.delete(self.alebo)
        except AttributeError:
            pass
        self.zoznam_hracov[self.kto_je_na_rade[0][1]].peniaze -= 1
        self.vypis_peniazky()
        self.canvas.delete(self.cierna)
        self.canvas.delete(self.sanca)
        self.canvas.bind('<ButtonPress>', self.klik)
        self.prepni_hracov()     

    def krok_vpred(self):
        self.canvas.delete(self.button_moznost1)
        self.canvas.delete(self.button_moznost2)
        self.canvas.delete(self.alebo)
        self.zoznam_hracov[self.kto_je_na_rade[0][1]].posun(1)
        self.canvas.delete(self.cierna)
        self.canvas.delete(self.sanca)
        self.canvas.bind('<ButtonPress>', self.klik)

    def krok_spat(self):
        self.canvas.delete(self.button_moznost1)
        self.canvas.delete(self.button_moznost2)
        self.canvas.delete(self.alebo)
        self.zoznam_hracov[self.kto_je_na_rade[0][1]].posun(-1)
        self.canvas.delete(self.cierna)
        self.canvas.delete(self.sanca)
        self.canvas.bind('<ButtonPress>', self.klik)

    def zdvihnut(self):
        self.canvas.delete(self.button_zdvihnut)
        self.canvas.delete(self.t)
        self.canvas.delete(self.cierna)
        self.canvas.delete(self.sanca)
        n = random.randrange(len(self.zoznam_hracov)-1)+1
        hp = self.zoznam_hracov[self.kto_je_na_rade[n][1]].peniaze
        if hp != 0:
            c = min(6, hp-1)
            p = random.randrange(c)+1
            self.zoznam_hracov[self.kto_je_na_rade[0][1]].peniaze += p
            self.zoznam_hracov[self.kto_je_na_rade[n][1]].peniaze -= p
        self.vypis_peniazky()
        self.canvas.bind('<ButtonPress>', self.klik)
        self.prepni_hracov()

    def fnuk(self):
        self.canvas.delete(self.button_zdvihnut)
        self.canvas.delete(self.t)
        self.canvas.delete(self.cierna)
        self.canvas.delete(self.sanca)
        n = random.randrange(len(self.zoznam_hracov)-1)+1
        hp = self.zoznam_hracov[self.kto_je_na_rade[0][1]].peniaze
        if hp != 0:
            c = min(6, hp-1)
            p = random.randrange(c)+1
            self.zoznam_hracov[self.kto_je_na_rade[n][1]].peniaze += p
            self.zoznam_hracov[self.kto_je_na_rade[0][1]].peniaze -= p
        self.vypis_peniazky()
        self.canvas.bind('<ButtonPress>', self.klik)
        self.prepni_hracov()

    def do_zalara(self):
        self.canvas.delete(self.t)
        self.canvas.delete(self.button_ist_do_zalara)
        self.canvas.delete(self.cierna)
        self.canvas.delete(self.sanca)
        self.zoznam_hracov[self.kto_je_na_rade[0][1]].posun(100 - self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia)
        self.canvas.bind('<ButtonPress>', self.klik)

    def zaplatit_pokutu(self):
        self.canvas.delete(self.t)
        self.canvas.delete(self.button_zaplatit_pokutu)
        self.zoznam_hracov[self.kto_je_na_rade[0][1]].peniaze -= 3
        self.vypis_peniazky()
        self.canvas.delete(self.cierna)
        self.canvas.delete(self.sanca)
        self.canvas.bind('<ButtonPress>', self.klik)
        self.prepni_hracov()

    def utekat(self):
        self.canvas.delete(self.t)
        self.canvas.delete(self.button_utekat)
        self.zoznam_hracov[self.kto_je_na_rade[0][1]].posun(3)
        self.canvas.delete(self.cierna)
        self.canvas.delete(self.sanca)
        self.canvas.bind('<ButtonPress>', self.klik)

    def mozog_vratit(self):
        self.canvas.delete(self.t)
        self.canvas.delete(self.button_moznost1)
        self.canvas.delete(self.button_moznost2)
        self.canvas.delete(self.alebo)
        self.zoznam_hracov[self.kto_je_na_rade[0][1]].posun(-4)
        self.canvas.delete(self.cierna)
        self.canvas.delete(self.sanca)
        self.canvas.bind('<ButtonPress>', self.klik)

    def bez_mozgu(self):
        self.canvas.delete(self.t)
        self.canvas.delete(self.button_moznost1)
        self.canvas.delete(self.button_moznost2)
        self.canvas.delete(self.alebo)
        if self.zoznam_hracov[self.kto_je_na_rade[0][1]].peniaze >= 4:
            self.zoznam_hracov[self.kto_je_na_rade[0][1]].peniaze -= 4
            self.vypis_peniazky()
            self.canvas.delete(self.cierna)
            self.canvas.delete(self.sanca)
            self.canvas.bind('<ButtonPress>', self.klik)
            self.prepni_hracov()
        else:
            self.mozog_vratit()

    def presun_start(self):
        self.canvas.delete(self.t)
        self.canvas.delete(self.button_presun_start)
        self.zoznam_hracov[self.kto_je_na_rade[0][1]].posun(-self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia)
        self.canvas.delete(self.cierna)
        self.canvas.delete(self.sanca)
        self.canvas.bind('<ButtonPress>', self.klik)

    def presun_zrkadlo(self):
        self.canvas.delete(self.t)
        self.canvas.delete(self.alebo)
        self.canvas.delete(self.button_moznost1)
        self.canvas.delete(self.button_moznost2)
        if self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia > 36:
            self.zoznam_hracov[self.kto_je_na_rade[0][1]].peniaze += 5
            self.vypis_peniazky()
        self.zoznam_hracov[self.kto_je_na_rade[0][1]].posun(36-self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia)
        self.canvas.delete(self.cierna)
        self.canvas.delete(self.sanca)
        self.canvas.bind('<ButtonPress>', self.klik)

    def presun_erik(self):
        self.canvas.delete(self.t)
        self.canvas.delete(self.alebo)
        self.canvas.delete(self.button_moznost1)
        self.canvas.delete(self.button_moznost2)
        if self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia > 16:
            self.zoznam_hracov[self.kto_je_na_rade[0][1]].peniaze += 5
            self.vypis_peniazky()
        self.zoznam_hracov[self.kto_je_na_rade[0][1]].posun(16-self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia)
        self.canvas.delete(self.cierna)
        self.canvas.delete(self.sanca)
        self.canvas.bind('<ButtonPress>', self.klik)

    def presun_trpaslici(self):
        self.canvas.delete(self.t)
        self.canvas.delete(self.alebo)
        self.canvas.delete(self.button_moznost1)
        self.canvas.delete(self.button_moznost2)
        if self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia > 29:
            self.zoznam_hracov[self.kto_je_na_rade[0][1]].peniaze += 5
            self.vypis_peniazky()
        self.zoznam_hracov[self.kto_je_na_rade[0][1]].posun(29-self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia)
        self.canvas.delete(self.cierna)
        self.canvas.delete(self.sanca)
        self.canvas.bind('<ButtonPress>', self.klik)

    def presun_jasmina(self):
        self.canvas.delete(self.t)
        self.canvas.delete(self.alebo)
        self.canvas.delete(self.button_moznost1)
        self.canvas.delete(self.button_moznost2)
        if self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia > 7:
            self.zoznam_hracov[self.kto_je_na_rade[0][1]].peniaze += 5
            self.vypis_peniazky()
        self.zoznam_hracov[self.kto_je_na_rade[0][1]].posun(7-self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia)
        self.canvas.delete(self.cierna)
        self.canvas.delete(self.sanca)
        self.canvas.bind('<ButtonPress>', self.klik)

    def presun_aladin(self):
        self.canvas.delete(self.t)
        self.canvas.delete(self.alebo)
        self.canvas.delete(self.button_moznost1)
        self.canvas.delete(self.button_moznost2)
        if self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia > 26:
            self.zoznam_hracov[self.kto_je_na_rade[0][1]].peniaze += 5
            self.vypis_peniazky()
        self.zoznam_hracov[self.kto_je_na_rade[0][1]].posun(26-self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia)
        self.canvas.delete(self.cierna)
        self.canvas.delete(self.sanca)
        self.canvas.bind('<ButtonPress>', self.klik)

    def presun_sebastian(self):
        self.canvas.delete(self.t)
        self.canvas.delete(self.alebo)
        self.canvas.delete(self.button_moznost1)
        self.canvas.delete(self.button_moznost2)
        if self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia > 3:
            self.zoznam_hracov[self.kto_je_na_rade[0][1]].peniaze += 5
            self.vypis_peniazky()
        self.zoznam_hracov[self.kto_je_na_rade[0][1]].posun(3-self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia)
        self.canvas.delete(self.cierna)
        self.canvas.delete(self.sanca)
        self.canvas.bind('<ButtonPress>', self.klik)

    def presun_jablko(self):
        self.canvas.delete(self.t)
        self.canvas.delete(self.alebo)
        self.canvas.delete(self.button_moznost1)
        self.canvas.delete(self.button_moznost2)
        if self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia > 9:
            self.zoznam_hracov[self.kto_je_na_rade[0][1]].peniaze += 5
            self.vypis_peniazky()
        self.zoznam_hracov[self.kto_je_na_rade[0][1]].posun(9-self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia)
        self.canvas.delete(self.cierna)
        self.canvas.delete(self.sanca)
        self.canvas.bind('<ButtonPress>', self.klik)

    def presun_kolovratok(self):
        self.canvas.delete(self.t)
        self.canvas.delete(self.alebo)
        self.canvas.delete(self.button_moznost1)
        self.canvas.delete(self.button_moznost2)
        if self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia > 24:
            self.zoznam_hracov[self.kto_je_na_rade[0][1]].peniaze += 5
            self.vypis_peniazky()
        self.zoznam_hracov[self.kto_je_na_rade[0][1]].posun(24-self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia)
        self.canvas.delete(self.cierna)
        self.canvas.delete(self.sanca)
        self.canvas.bind('<ButtonPress>', self.klik)

    def presun_jago(self):
        self.canvas.delete(self.t)
        self.canvas.delete(self.alebo)
        self.canvas.delete(self.button_moznost1)
        self.canvas.delete(self.button_moznost2)
        if self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia > 31:
            self.zoznam_hracov[self.kto_je_na_rade[0][1]].peniaze += 5
            self.vypis_peniazky()
        self.zoznam_hracov[self.kto_je_na_rade[0][1]].posun(31-self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia)
        self.canvas.delete(self.cierna)
        self.canvas.delete(self.sanca)
        self.canvas.bind('<ButtonPress>', self.klik)

    def presun_havrany(self):
        self.canvas.delete(self.t)
        self.canvas.delete(self.alebo)
        self.canvas.delete(self.button_moznost1)
        self.canvas.delete(self.button_moznost2)
        if self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia > 12:
            self.zoznam_hracov[self.kto_je_na_rade[0][1]].peniaze += 5
            self.vypis_peniazky()
        self.zoznam_hracov[self.kto_je_na_rade[0][1]].posun(12-self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia)
        self.canvas.delete(self.cierna)
        self.canvas.delete(self.sanca)
        self.canvas.bind('<ButtonPress>', self.klik)

    def presun_ariel(self):
        self.canvas.delete(self.t)
        self.canvas.delete(self.alebo)
        self.canvas.delete(self.button_moznost1)
        self.canvas.delete(self.button_moznost2)
        if self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia > 33:
            self.zoznam_hracov[self.kto_je_na_rade[0][1]].peniaze += 5
            self.vypis_peniazky()
        self.zoznam_hracov[self.kto_je_na_rade[0][1]].posun(33-self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia)
        self.canvas.delete(self.cierna)
        self.canvas.delete(self.sanca)
        self.canvas.bind('<ButtonPress>', self.klik)

    def presun_vtaciky(self):
        self.canvas.delete(self.t)
        self.canvas.delete(self.alebo)
        self.canvas.delete(self.button_moznost1)
        self.canvas.delete(self.button_moznost2)
        if self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia > 4:
            self.zoznam_hracov[self.kto_je_na_rade[0][1]].peniaze += 5
            self.vypis_peniazky()
        self.zoznam_hracov[self.kto_je_na_rade[0][1]].posun(4-self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia)
        self.canvas.delete(self.cierna)
        self.canvas.delete(self.sanca)
        self.canvas.bind('<ButtonPress>', self.klik)

    def presun_rajah(self):
        self.canvas.delete(self.t)
        self.canvas.delete(self.alebo)
        self.canvas.delete(self.button_moznost1)
        self.canvas.delete(self.button_moznost2)
        if self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia > 11:
            self.zoznam_hracov[self.kto_je_na_rade[0][1]].peniaze += 5
            self.vypis_peniazky()
        self.zoznam_hracov[self.kto_je_na_rade[0][1]].posun(11-self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia)
        self.canvas.delete(self.cierna)
        self.canvas.delete(self.sanca)
        self.canvas.bind('<ButtonPress>', self.klik)

    def presun_saty_sneh(self):
        self.canvas.delete(self.t)
        self.canvas.delete(self.alebo)
        self.canvas.delete(self.button_moznost1)
        self.canvas.delete(self.button_moznost2)
        if self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia > 14:
            self.zoznam_hracov[self.kto_je_na_rade[0][1]].peniaze += 5
            self.vypis_peniazky()
        self.zoznam_hracov[self.kto_je_na_rade[0][1]].posun(14-self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia)
        self.canvas.delete(self.cierna)
        self.canvas.delete(self.sanca)
        self.canvas.bind('<ButtonPress>', self.klik)
    
    def presun_filip(self):
        self.canvas.delete(self.t)
        self.canvas.delete(self.alebo)
        self.canvas.delete(self.button_moznost1)
        self.canvas.delete(self.button_moznost2)
        if self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia > 34:
            self.zoznam_hracov[self.kto_je_na_rade[0][1]].peniaze += 5
            self.vypis_peniazky()
        self.zoznam_hracov[self.kto_je_na_rade[0][1]].posun(34-self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia)
        self.canvas.delete(self.cierna)
        self.canvas.delete(self.sanca)
        self.canvas.bind('<ButtonPress>', self.klik)

    def presun_uhory(self):
        self.canvas.delete(self.t)
        self.canvas.delete(self.alebo)
        self.canvas.delete(self.button_moznost1)
        self.canvas.delete(self.button_moznost2)
        # OPTRAVIT nastavit na self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia = 21  
        if self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia > 21:
            self.zoznam_hracov[self.kto_je_na_rade[0][1]].peniaze += 5 
            self.vypis_peniazky()
        self.zoznam_hracov[self.kto_je_na_rade[0][1]].posun(21-self.zoznam_hracov[self.kto_je_na_rade[0][1]].pozicia)
        self.canvas.delete(self.cierna)
        self.canvas.delete(self.sanca)
        self.canvas.bind('<ButtonPress>', self.klik)
    
Program()