class CityPlan:

    def __init__(self, matrix, name, dist):
        self.matrix = matrix
        self.nameProject = name
        self.distManhattanMax = dist
        self.nbProjectPlaced = 0

    def add(self, building, row: int, column: int) -> bool:
        if building.is_placeable(self, row, column):
            building_row, building_column = building.matrix.shape

            idx_building_row = 0

            # on parcourt a partir de "row" definie jusqu'a
            # "row"+le nombre de lignes du batiments
            for numLignes in range(row, row + building_row):
                idx_building_column = 0
                # on parcourt a partir de "column" definie jusqu'a
                # la column+ le nombre de colonnes du batiments
                for numColonnes in range(column, column + building_column):
                    self.matrix[numLignes, numColonnes] = building.matrix[idx_building_row, idx_building_column]
                    idx_building_column += 1
                idx_building_row += 1
            return building
        else:
            return False
