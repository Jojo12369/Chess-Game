from pions import tour_b, tour_w, reine_b, reine_w
from conversion import conversion

def deplacement_tour(plateau, x, y, cases_possibles, pions_b):
     
    choix = []

    if plateau[x][y] in {tour_w["forme"], reine_w["forme"], tour_b["forme"], reine_b["forme"]}:
        mouvements = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dx, dy in mouvements:
            nx, ny = x + dx, y + dy
            while 0 <= nx < 8 and 0 <= ny < 8:
                if plateau[nx][ny] == " " or plateau[nx][ny] in pions_b:
                    conversion(x, y, cases_possibles)
                    nombre = 8 - nx
                    lettre = chr(ny + 65)
                    option = f"{lettre}{nombre}"
                    if option not in choix:
                        choix.append(option)
                    if plateau[nx][ny] in pions_b:
                        break
                else:
                    break
                nx += dx
                ny += dy

    return choix