from coup_possible import coup_possible
from afficher_plateau import afficher_plateau
from clear import clear

def texte(plateau, choix):
    clear()
    afficher_plateau(plateau)
    print()
    print(choix)
    print()

def choix_possibilites(plateau, case):
    
    choix = coup_possible(plateau, case) 
    texte(plateau, choix)
    
    choix_case = input("Choix de la case : ")
    
    while choix_case not in choix:
        texte(plateau, choix)
        choix_case = input("Erreur, choix de la case : ")
        
    return choix_case