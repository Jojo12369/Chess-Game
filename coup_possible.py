from deplacement_cavalier import deplacement_cavalier
from deplacement_fou import deplacement_fou
from deplacement_pion_blanc import deplacement_pion_blanc
from deplacement_pion_noir import deplacement_pion_noir
from deplacement_roi import deplacement_roi
from deplacement_tour import deplacement_tour
from pions import pions_b, pions_w, pion_w, tour_w, fou_w, roi_w, reine_w, cavalier_w, pion_b, tour_b, fou_b, roi_b, reine_b, cavalier_b

def coup_possible(plateau, case):
    
    x = 8 - int(case[1])
    y = int(ord(case[0])) - 65
    
    cases_possibles = []
    
    # print(plateau[x][y])
    
    if plateau[x][y] in {cavalier_w["forme"], cavalier_b["forme"]}:
        choix = deplacement_cavalier(plateau, x, y, cases_possibles, pions_b) if plateau[x][y] == "£" else deplacement_cavalier(plateau, x, y, cases_possibles, pions_w)
        
    if plateau[x][y] == pion_w["forme"]:
        choix = deplacement_pion_blanc(plateau, x, y, cases_possibles, pions_b)
    
    if plateau[x][y] == pion_b["forme"]:
        choix = deplacement_pion_noir(plateau, x, y, cases_possibles, pions_w)
        
    if plateau[x][y] in {fou_w["forme"], fou_b["forme"]}:
        choix = deplacement_fou(plateau, x, y, cases_possibles, pions_b) if plateau[x][y] == "x" else deplacement_fou(plateau, x, y, cases_possibles, pions_w)
        
    if plateau[x][y] in {tour_w["forme"], tour_b["forme"]}:
        choix = deplacement_tour(plateau, x, y, cases_possibles, pions_b) if plateau[x][y] == "+" else deplacement_tour(plateau, x, y, cases_possibles, pions_w)
        
    if plateau[x][y] in {reine_w["forme"], reine_b["forme"]}:
        choix_1 = deplacement_tour(plateau, x, y, cases_possibles, pions_b) if plateau[x][y] == "#" else deplacement_tour(plateau, x, y, cases_possibles, pions_w)
        choix_2 = deplacement_fou(plateau, x, y, cases_possibles, pions_b) if plateau[x][y] == "#" else deplacement_fou(plateau, x, y, cases_possibles, pions_w)
        
        choix = list(set(choix_1 + choix_2))

    if plateau[x][y] in {roi_w["forme"], roi_b["forme"]}:    
        choix = deplacement_roi(plateau, x, y, cases_possibles, pions_b) if plateau[x][y] == "¤" else deplacement_roi(plateau, x, y, cases_possibles, pions_w)
        
    print(choix)
        
    return choix