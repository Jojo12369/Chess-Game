from pions import pion_b

from conversion import conversion

def deplacement_pion_noir(plateau, x, y, cases_possibles, pions_w):
    choix = []

    def ajouter_option(nx, ny):
        conversion(x, y, cases_possibles)
        nombre = 8 - nx
        lettre = chr(ny + 65)
        option = f"{lettre}{nombre}"
        if option not in choix:
            choix.append(option)
    
    if plateau[x][y] == pion_b["forme"]:
        # Déplacement de deux cases si le pion n'a pas bougé
        if x == 1 and plateau[2][y] == " " and plateau[3][y] == " ":
            ajouter_option(3, y)
        
        # Déplacement d'une case en avant
        if x >= 1 and plateau[x + 1][y] == " ":
            ajouter_option(x + 1, y)

        # Captures diagonales
        if x >= 1:
            if y >= 1 and plateau[x + 1][y - 1] in pions_w:
                ajouter_option(x + 1, y - 1)
            if y <= 6 and plateau[x + 1][y + 1] in pions_w:
                ajouter_option(x + 1, y + 1)
                
    return choix