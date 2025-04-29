<<<<<<< HEAD
def lit_grille(fichier):
    grille = {'A': ['.', '.', '.'], 'B': ['.', '.', '.'], 'C': ['.', '.', '.']}
    with open(fichier, 'r') as f:
        ch = f.read()
        ch = ch.strip()
        i = 0
        print(ch)
        while i < len(ch):
            lettre = ch[i]
            i += 1
            chiffre = ch[i]
            i += 1
            joueur = ch[i]
            grille[lettre][int(chiffre) - 1] = joueur
            i += 1
    return grille  # <-- return en dehors de la boucle !

def afficher_grille(grille: dict):
    print(' ' + '-'*13)
    for l in grille.values():
        print(' | '+' | '.join(l)+' | ')
        print(' ' + '-'*13)
afficher_grille(lit_grille('grille.morpion'))
=======
grille ={'A':['','' ,''], 'B':['','' ,''], 'C':['','' ,'']}

def afficher_grille(grille: dict):
    for ligne, valeur in grille.items():
        print (f"{ligne} | {valeur}")

afficher_grille(grille)
>>>>>>> a58883a7620755511f001ddfec53d1477b98c5eb
