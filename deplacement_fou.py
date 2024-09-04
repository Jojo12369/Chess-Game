from pions import fou_b, fou_w, reine_b, reine_w

from conversion import conversion

def deplacement_fou(plateau, x, y, cases_possibles, pions_b):
    choix = []

    if plateau[x][y] in {fou_w["forme"], reine_w["forme"], fou_b["forme"], reine_b["forme"]}:
        directions = [(-1, -1), (-1, +1), (+1, -1), (+1, +1)]
        
        for dx, dy in directions:
            i, j = x, y
            while 0 <= i + dx < 8 and 0 <= j + dy < 8:
                i += dx
                j += dy
                if plateau[i][j] == " " or plateau[i][j] in pions_b:
                    conversion(x, y, cases_possibles)
                    nombre = 8 - i
                    lettre = chr(j + 65)
                    option = f"{lettre}{nombre}"
                    if option not in choix:
                        choix.append(option)
                    if plateau[i][j] in pions_b:
                        break
                else:
                    break

    return choix