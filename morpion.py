# Créer une grille vide avec lignes A, B, C et colonnes 1, 2, 3
grille = {
    "A1": " ", "A2": " ", "A3": " ",
    "B1": " ", "B2": " ", "B3": " ",
    "C1": " ", "C2": " ", "C3": " "
}

#verson réelle

def verifier_victoire(plateau, joueur):
    for ligne in plateau:
        if all(cellule == joueur for cellule in ligne):
            return True

    for col in range(3):
        if all(plateau[ligne][col] == joueur for ligne in range(3)):
            return True

    if all(plateau[i][i] == joueur for i in range(3)):
        return True
    if all(plateau[i][2 - i] == joueur for i in range(3)):
        return True

    return False

def morpion():
    plateau = [[" " for _ in range(3)] for _ in range(3)]
    joueur_courant = "X"

    for tour in range(9):
        afficher_plateau(plateau)
        print(f"Au tour du joueur {joueur_courant}")

        while True:
            try:
                ligne = int(input("Choisis une ligne (0, 1, 2) : "))
                colonne = int(input("Choisis une colonne (0, 1, 2) : "))
                if plateau[ligne][colonne] == " ":
                    plateau[ligne][colonne] = joueur_courant
                    break
                else:
                    print("Case déjà occupée, choisis-en une autre.")
            except (ValueError, IndexError):
                print("Entrée invalide, essaie encore.")

        if verifier_victoire(plateau, joueur_courant):
            afficher_plateau(plateau)
            print(f"Le joueur {joueur_courant} a gagné !")
            return

        joueur_courant = "O" if joueur_courant == "X" else "X"

    afficher_plateau(plateau)
    print("Match nul !")


if __name__ == "__main__":
    morpion()

afficher_grille(grille)