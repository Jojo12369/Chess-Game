from pions import cavalier_w, cavalier_b

from conversion import conversion

def deplacement_cavalier(plateau, x, y, cases_possibles, pions_b):
    choix = []
    mouvements = [
        (-2, -1), (-2, +1), (-1, -2), (-1, +2),
        (+1, -2), (+1, +2), (+2, -1), (+2, +1)
    ]

    if plateau[x][y] in {cavalier_w["forme"], cavalier_b["forme"]}:
        for dx, dy in mouvements:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8:
                if plateau[nx][ny] == " " or plateau[nx][ny] in pions_b:
                    conversion(x, y, cases_possibles)
                    
                    nombre = 8 - nx
                    lettre = chr(ny + 65)
                    option = f"{lettre}{nombre}"
                    
                    if option not in choix:
                        choix.append(option)
                
    return choix