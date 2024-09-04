from pions import pions_w, pions_b, pion_w, pion_b, fou_b, fou_w, reine_b, reine_w, tour_b, tour_w, cavalier_b, cavalier_w
from clear import clear
from afficher_plateau import afficher_plateau

def texte(plateau, pions):
    clear()
    afficher_plateau(plateau)
    print()
    print(f"1. {pions[0]}")
    print(f"2. {pions[1]}")
    print(f"3. {pions[2]}")
    print(f"4. {pions[3]}")
    print()

def pions_evolution(plateau):
    
    liste_choix = ["1", "2", "3", "4"]
    
    for i in range(8):
        if plateau[0][i] == pion_w["forme"]:
            
            pions = [reine_w["forme"], cavalier_w["forme"], tour_w["forme"], fou_w["forme"]]
            
            texte(plateau, pions)
            choix_pion = input("Choix du pion : ")
            
            while choix_pion not in liste_choix:
                
                texte(plateau, pions)
                choix_pion = input("Erreur, choix du pion : ")
            
            match choix_pion:
                case "1":
                    plateau[0][i] = reine_w["forme"]
                case "2":
                    plateau[0][i] = cavalier_w["forme"]
                case "3":
                    plateau[0][i] = tour_w["forme"]
                case "4":
                    plateau[0][i] = fou_w["forme"]
            return  
        
        
        if plateau[7][i] == pion_b["forme"]:
            
            pions = [reine_b["forme"], cavalier_b["forme"], tour_b["forme"], fou_b["forme"]]
            
            texte(plateau, pions)
            choix_pion = input("Choix du pion : ")
            
            while choix_pion not in liste_choix:
                
                texte(plateau, pions)
                choix_pion = input("Erreur, choix du pion : ")
            
            match choix_pion:
                case "1":
                    plateau[7][i] = reine_b["forme"]
                case "2":
                    plateau[7][i] = cavalier_b["forme"]
                case "3":
                    plateau[7][i] = tour_b["forme"]
                case "4":
                    plateau[7][i] = fou_b["forme"]
            return 