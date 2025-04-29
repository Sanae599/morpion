def lit_grille(fichier):
    grille = {'A': ['.', '.', '.'], 'B': ['.', '.', '.'], 'C': ['.', '.', '.']}
    with open(fichier, 'r') as f:
        ch = f.read()
        ch = ch.strip()
        i = 0
       # print(ch)
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