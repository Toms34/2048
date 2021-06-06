import tkinter as tk
from tkinter import *
from numpy import *
from PIL import Image, ImageTk
from oui import *
from lescases import *
import time
CaseVide =[]
spawn = (2,2,2,4)

#création des blocks a à p
a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p = Point(0,0),Point(0,100),Point(0,200),Point(0,300),Point(100,0),Point(100,100),Point(100,200),Point(100,300),Point(200,0),Point(200,100),Point(200,200),Point(200,300),Point(300,0),Point(300,100),Point(300,200),Point(300,300)
block = (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p)
caseV(block,CaseVide)
tps = time.time()
pop = False
rdom = random.randint(0,15,2) #on choisit aléatoirement les 2 cases de départ
CaseVide[rdom[0]].v = 2 #première case avec un deux
CaseVide[rdom[1]].v = 2 #deuxième case avec un deux
fenetre=tk.Tk()
fenetre.title(("2048       score :"+ str(somme(block)) ))
fenetre.iconbitmap("2048.ico")
canvas = Canvas(fenetre, width=403, height=403, bg="#C1AE9D") # création du canvas (aire de jeu)
for n in range(0,16):
    block[n].image2 = canvas.create_rectangle(block[n].x+6,block[n].y+6,block[n].x+100,block[n].y+100,fill=Color(block[n].v),width=0)
    block[n].image = canvas.create_text(block[n].x+50 , block[n].y+50, text = ToPrint(block[n].v))

def clavier(event): #event = pression sur une touche
    touche = event.keysym #récupération des touches
    global pop
    perdue = 0
    if touche =="r"or touche == "R":
        for n in range(0,16):
            block[n].v = 0
            block[n].f = 0
            block[n].d = 0
        caseV(block,CaseVide)
        rdom = random.randint(0,15,2) #on choisit aléatoirement les 2 cases de départ
        CaseVide[rdom[0]].v = 2 #première case avec un deux
        CaseVide[rdom[1]].v = 2 #deuxième case avec un deux
        perdue = 0
    if touche == "Down": #si le jouer appuit sur la flèche du bas
        Clean(block)
        z=0
        while z<3: #compteur
            Down(2,-1,block)
            Down(6,3,block)
            Down(10,7,block)
            Down(14,11,block)
            z=z+1 #le tour est finit on augemente donc le compteur de 1
        pop = True
    if touche == "Up": #si le jouer appuit sur la flèche du haut
        Clean(block)
        z=0
        while z<3: #compteur
            Moov(0,3,1,block)
            Moov(4,7,1,block)
            Moov(8,11,1,block)
            Moov(12,15,1,block)
            z=z+1 #le tour est finit on augemente donc le compteur de 1
        pop = True
    if touche == "Left": #si le jouer appuit sur la flèche de gauche
        Clean(block)
        z=0
        while z<3: #compteur
            Moov(0,12,4,block)
            Moov(1,13,4,block)
            Moov(2,14,4,block)
            Moov(3,15,4,block)
            z=z+1 #le tour est finit on augemente donc le compteur de 1
        pop = True
    if  touche == "Right": #si le jouer appuit sur la flèche de droite
        Clean(block)
        z=0
        while z<3:#compteur du nombre de tour effectué
            Moov(12,0,-4,block)
            Moov(13,1,-4,block)
            Moov(14,2,-4,block)
            Moov(15,3,-4,block)
            z=z+1 #le tour est finit on augemente donc le compteur de 1
        pop = True
    caseV(block,CaseVide) #on fait verifier le nombre de case vide pour la suite
    count = 0
    for n in range(0,16):
        if block[n].d == 1:
            count = count + 1
    if len(CaseVide)>0 and pop == True and count>0: #si il y a des cases vides et que l'on vient de jouer alors on fait apparaitre un nouveau block aléatoire 2
        CaseVide[random.randint(0,len(CaseVide))].v = spawn[random.randint(0,4)]
        pop = False
        count = 0
    for n in range(0,16):
        block[n].d = 0
    if len(CaseVide)==0:
        Check(0,3,1,block,perdue)
        Check(4,7,1,block,perdue)
        Check(8,11,1,block,perdue)
        Check(12,15,1,block,perdue)
        Check(0,12,4,block,perdue)
        Check(1,13,4,block,perdue)
        Check(2,14,4,block,perdue)
        Check(3,15,4,block,perdue)
        Check(12,0,-4,block,perdue)
        Check(13,1,-4,block,perdue)
        Check(14,2,-4,block,perdue)
        Check(15,3,-4,block,perdue)
        Check2(2,-1,block,perdue)
        Check2(6,3,block,perdue)
        Check2(10,7,block,perdue)
        Check2(14,11,block,perdue)
        if perdue == 0:
            for n in range(0,16):
                block[n].v = 0
                block[n].f = 0
                block[n].d = 0
            caseV(block,CaseVide)
            rdom = random.randint(0,15,2) #on choisit aléatoirement les 2 cases de départ
            CaseVide[rdom[0]].v = 2 #première case avec un deux
            CaseVide[rdom[1]].v = 2 #deuxième case avec un deux
    for n in range(0,16):
        canvas.delete(block[n].image,block[n].image2)
        block[n].image2 = canvas.create_rectangle(block[n].x+3,block[n].y+3,block[n].x+97,block[n].y+97,fill=Color(block[n].v),width=0)
        block[n].image = canvas.create_text(block[n].x+50 , block[n].y+50, text = ToPrint(block[n].v))

    CaseVide[:] = []
    fenetre.title(("2048       score :"+ str(somme(block)) ))


# ajout du bond sur les touches du clavier
canvas.focus_set()
canvas.bind("<Key>", clavier)
# création du canvas (affichage)
canvas.pack()
fenetre.mainloop()
