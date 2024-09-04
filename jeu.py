from initialise_plateau import initialiser_plateau
from choix_possibilites import choix_possibilites
from cases_possibilites import cases_possibilites
from pions_evolution import pions_evolution

def jeu():
    
    # Initialisation de nos variables et du plateau
    plateau_depart = [[" " for _ in range(8)]for _ in range(8)]
    tour = 0
    
    plateau = initialiser_plateau(plateau_depart)
    
    while True:
        
        joueur = tour % 2
            
        case = cases_possibilites(plateau, joueur)
        choix_case = choix_possibilites(plateau, case)
        
        x = 8 - int(case[1])
        y = int(ord(case[0])) - 65
        
        i = 8 - int(choix_case[1])
        j = int(ord(choix_case[0])) - 65
        
        plateau[i][j] = plateau[x][y]
        plateau[x][y] = " "
                
        pions_evolution(plateau)
        
        tour += 1