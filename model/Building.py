import numpy as np
from model.Project import Project


class Building(Project):

    def __init__(self, id, matrix, id_building, pos_row, pos_column):
        super().__init__(id, matrix)
        self.pos_row = None
        self.pos_column = None
        self.id_building = id_building

    # acces aux valeurs de la matrice la ligne puis la colonne
    def is_placeable(self, city, row: int, column: int) -> bool:    #TODO: Modifier en fonction de la nouvelle classe
        try:
            if city.matrix[row, column] == '#':
                return False
            else:

                building_row, building_column = self.matrix.shape

                # on parcourt a partir de pos_row definie jusqu'a
                # la pos_row+le nombre de lignes du batiments
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
