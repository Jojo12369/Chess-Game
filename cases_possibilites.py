from pions_possibilites_blanc import pions_possibilites_blanc
from pions_possibilites_noir import pions_possibilites_noir
from afficher_plateau import afficher_plateau
from clear import clear

def texte(plateau, cases_possibles):
    clear()
    afficher_plateau(plateau)
    print()
    print(cases_possibles)
    print()

def cases_possibilites(plateau, joueur):
    
    if joueur == 0:
        cases_possibles = pions_possibilites_blanc(plateau)
    if joueur == 1:
        cases_possibles = pions_possibilites_noir(plateau)
    texte(plateau, cases_possibles)
    
    case = input("Choix de la case : ")
    
    while case not in cases_possibles:
        texte(plateau, cases_possibles)
        case = input("Erreur, choix de la case : ")
        
    return case