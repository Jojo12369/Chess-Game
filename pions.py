# Pions blanc
pion_w = {
    "nom": "pion",
    "forme": "o"
}

tour_w = {
    "nom": "tour",
    "forme": "+"
}

fou_w = {
    "nom": "fou",
    "forme": "x"
}

cavalier_w = {
    "nom": "cavalier",
    "forme": "£"
} 

reine_w = {
    "nom": "reine",
    "forme": "#"   
}

roi_w = {
    "nom": "roi",
    "forme": "¤"
}

# Couleur
couleur = 91

# Pions noir
pion_b = {
    "nom": "pion",
    "forme": f"\033[{couleur}mo\033[0m"
}

tour_b = {
    "nom": "tour",
    "forme": f"\033[{couleur}m+\033[0m"
}

fou_b = {
    "nom": "fou",
    "forme": f"\033[{couleur}mx\033[0m"
}

cavalier_b = {
    "nom": "cavalier",
    "forme": f"\033[{couleur}m£\033[0m"
} 

reine_b = {
    "nom": "reine",
    "forme": f"\033[{couleur}m#\033[0m"   
}

roi_b = {
    "nom": "roi",
    "forme": f"\033[{couleur}m¤\033[0m"
}

# Liste pion_b = pion noir et pion_w = pion blanc
pions_b = [pion_b["forme"], tour_b["forme"], fou_b["forme"], cavalier_b["forme"], reine_b["forme"], roi_b["forme"]] 
pions_w = [pion_w["forme"], tour_w["forme"], fou_w["forme"], cavalier_w["forme"], reine_w["forme"], roi_w["forme"]]