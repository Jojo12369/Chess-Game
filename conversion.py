def conversion(x, y ,cases_possibles):
    nombre = 8 - x
    lettre = chr(y + 65)
    option = str(f"{lettre}{nombre}")
    
    if option not in cases_possibles:
        cases_possibles.append(option)