from oui import *
from numpy import *
valeurtot = 0
def caseV(block,CaseVide):
    for nb in range(0,16):
        if block[nb].v == 0:
            CaseVide.append(block[nb])
    return(CaseVide)


def Down(a,b,block):
    #pour les blocs de 2 à 0, # si le bloc est vide on fait rien 'fin instruction'
    #si bloc pas vide,
        #1- si le bloc (n+1) est vide alors bloc (n°1) = bloc (n) et bloc(n) = vide
        #2 si bloc (n+1) = bloc (n) et si bloc (n+1) n'est pas fusionné alors
           # bloc(n+1) = 2 bloc(n+1)  et bloc =(n)= vides=
           # bloc (n+1) fusionné
    for n in range (a,b,-1):
        if block[n].v == block[n+1].v and block[n].f == 0 and block[n+1].f == 0 and block[n+1].v!=0: #si les valeurs des blocks sont égales ou que celui du dessous et nul et qu'il n'a pas déjà fussioné
            block[n+1].v = 2*(block[n].v)
            block[n].v = 0
            block[n+1].f = 1
            block[n].d = 1
        if block[n+1].v == 0:
            block[n+1].v = block[n].v
            block[n].v = 0
            block[n].d = 1

def Moov(a,b,c,block):
    for n in range(a,b,c):
        if block[n].v == block[n+c].v and block[n].f==0 and block[n+c].f == 0 and block[n+c].v!=0 :
            block[n].v = 2*(block[n].v)
            block[n].f = 1
            block[n+c].v = 0
            block[n].d = 1
        if  block[n].v == 0:
            block[n].v = block[n+c].v
            block[n+c].v = 0
            block[n].d= 1
def Clean(block):
    for n in range(0,16):
        block[n].f = 0
        block[n].d = 0

def Check(a,b,c,block,perdue):
    for n in range(a,b,c):
        if block[n].v == block[n+c].v :
            perdue = perdue+1
    return(perdue)
def Check2(a,b,block,perdue):
    for n in range (a,b,-1):
        if block[n].v == block[n+1].v :
            perdue = perdue +1
    return(perdue)
def ToPrint(a):
    valeurs = ""
    if a>0:
        valeurs = str(a)
    else:
        valeurs = ""
    return(valeurs)

def Color(a):
    couleur = ""
    if a == 0:
        couleur = "#CAC0B4"
    if a == 2:
        couleur = "#ECE2D9"
    if a == 4:
        couleur = "#EDDEC9"
    if a == 8:
        couleur = "#F7AD70"
    if a == 16:
        couleur = "#F69465"
    if a == 32:
        couleur = "#ED5E34"
    if a == 64:
        couleur = "#F55E31"
    if a == 128:
        couleur = "#F4D177"
    if a == 256:
        couleur = "#EBCA5F"
    if a == 512:
        couleur = "#EEC54F"
    if a == 1024:
        couleur = "#EDC33D"
    if a == 2048:
        couleur = "#F46676"
    return(couleur)

def somme(block):
    global valeurtot
    valeurtot = 0
    for n in range(0,16):
        valeurtot = valeurtot + block[n].v
    return(valeurtot)
