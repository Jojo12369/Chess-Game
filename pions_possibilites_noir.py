from deplacement_tour import deplacement_tour
from deplacement_pion_noir import deplacement_pion_noir
from deplacement_fou import deplacement_fou
from deplacement_cavalier import deplacement_cavalier
from deplacement_roi import deplacement_roi
from pions import pions_b, pions_w

def pions_possibilites_noir(plateau):
    
    cases_possibles = []

    # coordonées: 'x: 0, y: 0'
    for x in range(8):
        for y in range(8):
            if plateau[x][y] in pions_b:
                # print(f"pion: '{plateau[x][y]}', coordonées: [{x}, {y}]")
                     
                deplacement_pion_noir(plateau, x, y, cases_possibles, pions_w)
                deplacement_tour(plateau, x, y, cases_possibles, pions_w)
                deplacement_fou(plateau, x, y, cases_possibles, pions_w)
                deplacement_cavalier(plateau, x, y, cases_possibles, pions_w)
                deplacement_roi(plateau, x, y, cases_possibles, pions_w)
                
    return cases_possibles