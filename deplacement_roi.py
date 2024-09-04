from pions import roi_b, roi_w
from conversion import conversion

def deplacement_roi(plateau, x, y, cases_possibles, pions_b):
    
    choix = []
    mouvements = [
        (+1, -1), (+1, +1), (-1, -1), (-1, +1), 
        (+1, 0),  (-1, 0),  (0, -1),  (0, +1)
    ]
    
    if plateau[x][y] in {roi_w["forme"], roi_b["forme"]}:
        
        for dx, dy in mouvements:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8:
                if plateau[nx][ny] == " " or plateau[nx][ny] == pions_b:
                    # print(f"roi bas gauche: [{nx}, {ny}]")
                    conversion(x, y ,cases_possibles)
                
                    nombre = 8 - (nx)
                    lettre = chr((ny) + 65)
                    option = str(f"{lettre}{nombre}")
                    
                    if option not in choix:
                        choix.append(option)
            
    return choix