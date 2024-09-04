def afficher_plateau(plateau_depart):

    lettres = [chr(lettre) for lettre in range(ord("A"), ord("I"))]
    pions = ["pion: o", "tour: +", "fou: x", "cavalier: £", "reine: #", "roi: ¤"] 

    for i, case in enumerate(plateau_depart, start = 0):
        print("   " + ("+---" * 9)[:-3])
        if i > 0 and i < 7:
            print(f" {8 - i}" + " | " + (" | ".join(case)) + " |     " + "".join(pions[i - 1]))
        else :
            print(f" {8 - i}" + " | " + (" | ".join(case)) + " |")

    print("   " + ("+---" * 9)[:-3])
    print("     " + "   ".join(lettres))