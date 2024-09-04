from pions import pion_w, tour_w, fou_w, cavalier_w, reine_w, roi_w, pion_b, tour_b, fou_b, cavalier_b, reine_b, roi_b

def initialiser_plateau(plateau):

    # Tour
    for i in range(2):
        plateau[0][i * 7] = tour_b["forme"]
        plateau[7][i * 7] = tour_w["forme"]

    # Cavalier
    for i in range(2):
        plateau[0][(i + 1) + 4 * i] = cavalier_b["forme"]
        plateau[7][(i + 1) + 4 * i] = cavalier_w["forme"]

    # Cavalier
    for i in range(2):
        plateau[0][(i + 2) + 2 * i] = fou_b["forme"]
        plateau[7][(i + 2) + 2 * i] = fou_w["forme"]

    # Dame
    plateau[0][3] = reine_b["forme"]
    plateau[7][3] = reine_w["forme"]

    # Roi
    plateau[0][4] = roi_b["forme"]
    plateau[7][4] = roi_w["forme"]

    # Pion
    for i in range(8):
        plateau[1][i] = pion_b["forme"]
        plateau[6][i] = pion_w["forme"]

    return plateau