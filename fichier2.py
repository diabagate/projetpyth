import random

def SaisirJeu():
    jeu = []
    while len(jeu)<7:
        nb = int(raw_input('Entrer un entier entre 1 et 49: '))
        if nb not in jeu and nb <50 : jeu.append(nb)
    print ('Votre jeu : ',jeu)
    return jeu                              
    
def hasard():
    return random.random()*48+1

def estGagnant(jeu=[], tirage=[]):
    nb=0
    for i in range(1,6):
        for y in range(1,6,1):
            if jeu[i]==tirage[y]:
                nb += 1
    return nb

def tirage():
    tirage = []
    while len(tirage)<7:
        nb = int(hasard())
        if nb not in tirage: tirage.append(nb)
    print ('Le tirage : ',tirage)
    return tirage                               
    
def Jeu():
    nb = estGagnant(SaisirJeu(), tirage())
    if nb > 2:
        print ('Gagne: ',nb,' bons numeros')
    else: print ('Perdu...')
    
while raw_input('Pour jouer taper 0 : ')=='0':
    Jeu()
else: print ('Salut !')
