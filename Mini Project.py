import sys
import random
import time
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView
from PyQt5.QtGui import QColor, QPen, QBrush
from PyQt5.QtCore import Qt

# Constants
DIM_LABY = 11  # Changeable size of the maze
DIM_FENETRE = 600
DIM_CASE = DIM_FENETRE // DIM_LABY
NORD, EST, SUD, OUEST = 1, 2, 3, 4
mur_oppose = {NORD: SUD, SUD: NORD, EST: OUEST, OUEST: EST}

# Initialize a cell
def initialise_case(lig, col):
    numero = lig * DIM_LABY + col
    couleur = QColor(random.randint(128, 255), random.randint(128, 255), random.randint(128, 255))
    return [numero, True, True, True, True, couleur]

# Initialize a row
def initialise_ligne(lig):
    return [initialise_case(lig, col) for col in range(DIM_LABY)]

# Initialize the maze
def initialise_laby():
    return [initialise_ligne(lig) for lig in range(DIM_LABY)]

# Draw a cell
def dessine_case(scene, case, x, y):
    numero, mur_nord, mur_est, mur_sud, mur_ouest, couleur = case
    pen = QPen(Qt.NoPen)
    brush = QBrush(couleur)
    scene.addRect(x, y, DIM_CASE, DIM_CASE, pen, brush)

    if numero >= 0:
        text_num = scene.addText(str(numero))
        text_num.setPos(x + DIM_CASE / 3, y + DIM_CASE / 4)
        text_num.setScale(DIM_CASE / 50)

    pen = QPen(Qt.black, 1 + (79 // DIM_LABY), Qt.SolidLine, Qt.RoundCap)
    if mur_nord:
        scene.addLine(x, y, x + DIM_CASE, y, pen)
    if mur_est:
        scene.addLine(x + DIM_CASE, y, x + DIM_CASE, y + DIM_CASE, pen)
    if mur_sud:
        scene.addLine(x, y + DIM_CASE, x + DIM_CASE, y + DIM_CASE, pen)
    if mur_ouest:
        scene.addLine(x, y, x, y + DIM_CASE, pen)

# Draw the entire maze
def dessine_laby(scene, laby):
    scene.clear()
    for lig in range(DIM_LABY):
        for col in range(DIM_LABY):
            x, y = col * DIM_CASE, lig * DIM_CASE
            dessine_case(scene, laby[lig][col], x, y)

# Select a base cell and its neighboring cell
def select_cases(laby):
    while True:
        l, c = random.randrange(DIM_LABY), random.randrange(DIM_LABY)
        mur_voisin = random.choice([NORD, EST, SUD, OUEST])

        if mur_voisin == NORD and l == 0: continue
        if mur_voisin == SUD and l == DIM_LABY - 1: continue
        if mur_voisin == OUEST and c == 0: continue
        if mur_voisin == EST and c == DIM_LABY - 1: continue

        l_voisin = l + (mur_voisin == SUD) - (mur_voisin == NORD)
        c_voisin = c + (mur_voisin == EST) - (mur_voisin == OUEST)

        if laby[l][c][0] != laby[l_voisin][c_voisin][0]:
            return [l, c, mur_voisin]

# Merge two cells
def agglomere_cases(selection, laby):
    l, c, mur_voisin = selection
    l_voisin = l + (mur_voisin == SUD) - (mur_voisin == NORD)
    c_voisin = c + (mur_voisin == EST) - (mur_voisin == OUEST)

    numero_base = laby[l][c][0]
    numero_voisin = laby[l_voisin][c_voisin][0]
    coul_base = laby[l][c][5]

    # Remove the common walls
    laby[l][c][mur_voisin] = False
    laby[l_voisin][c_voisin][mur_oppose[mur_voisin]] = False

    # Update all cells with the neighbor's number
    for lig in laby:
        for case in lig:
            if case[0] == numero_voisin:
                case[0] = numero_base
                case[5] = coul_base

# Main program
# Main program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = QGraphicsView()
    scene = QGraphicsScene()
    view.setScene(scene)
    view.setWindowTitle("Labyrinthe")
    view.setGeometry(100, 100, DIM_FENETRE + 4, DIM_FENETRE + 4)
    scene.setBackgroundBrush(QBrush(QColor(200, 200, 200)))
    view.show()

    laby = initialise_laby()
    nb_agglomerations = 0
    while nb_agglomerations < DIM_LABY * DIM_LABY - 1:
        dessine_laby(scene, laby)
        end_time = time.time() + 10 / DIM_LABY ** 2
        while time.time() < end_time:
            QApplication.processEvents()
        selection = select_cases(laby)
        agglomere_cases(selection, laby)
        nb_agglomerations += 1

    # Check if all cells are connected (i.e., there is only one unique cell number)
    unique_numbers = set(case[0] for ligne in laby for case in ligne)
    if len(unique_numbers) > 1:
        # Find a cell that is not connected and agglomerate it with any other cell
        unconnected_cells = [case for ligne in laby for case in ligne if case[0] != min(unique_numbers)]
        unconnected_cell = random.choice(unconnected_cells)
        connected_cell = [case for ligne in laby for case in ligne if case[0] == min(unique_numbers)][0]

        # Force a connection between the isolated cell and any cell from the main group
        l, c, mur_voisin = unconnected_cell[0], unconnected_cell[1], random.choice([NORD, EST, SUD, OUEST])
        agglomere_cases([l, c, mur_voisin], laby)

    print("Numéros présents dans le labyrinthe :",
          set(case[0] for ligne in laby for case in ligne))

    sys.exit(app.exec_())
