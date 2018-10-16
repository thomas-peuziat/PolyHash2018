

class Project:

    def __init__(self, id, matrix):
        self.id = id
        self.matrix = matrix
        self.shape = matrix.shape
        self.list_pos_replica = []

    # acces aux valeurs de la matrice la ligne puis la colonne
    def is_placeable(self, city, row: int, column: int) -> bool:  # TODO: Modifier en fonction de la nouvelle classe
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