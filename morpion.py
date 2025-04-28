grille ={'A':['','' ,''], 'B':['','' ,''], 'C':['','' ,'']}

def afficher_grille(grille: dict):
    for ligne, valeur in grille.items():
        print (f"{ligne} | {valeur}")

afficher_grille(grille)
