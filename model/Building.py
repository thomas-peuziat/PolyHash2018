import numpy as np


class Building:

    def __init__(self, matrix):
        self.row = None
        self.column = None
        self.matrix = matrix
        self.placed = False

    # acces aux valeurs de la matrice la ligne puis la colonne
    def is_placeable(self, city, row: int, column: int) -> bool:
        try:
            if city.matrix[row, column] == '#':
                return False
            else:
                building_row, building_column = self.matrix.shape

                # on parcourt a partir de row definie jusqu'a
                # la row+le nombre de lignes du batiments
                for numLignes in range(row, row + building_row):
                    # on parcourt a partir de la posX definie jusqu'a
                    # la posX+ le nombre de colonnes du batiments
                    for numColonnes in range(column, column + building_column):
                        if city.matrix[numLignes, numColonnes] == '#':
                            return False
                return True
        except IndexError:
            return False

# fin classe Building
