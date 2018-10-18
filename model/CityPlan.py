class CityPlan:

    def __init__(self, matrix, name, dist):
        self.matrix = matrix
        self.name_project = name
        self.dist_manhattan_max = dist

    def add(self, project, row: int, column: int):
        if project.is_placeable(self.matrix, row, column):
            project_row, project_column = project.shape

            idx_project_row = 0

            # on parcourt a partir de "row" definie jusqu'a
            # "row"+le nombre de lignes du batiments
            for num_lignes in range(row, row + project_row):
                idx_project_column = 0
                # on parcourt a partir de "column" definie jusqu'a
                # la column+ le nombre de colonnes du batiments
                for num_colonnes in range(column, column + project_column):
                    #si dans la ville, c'est égale à un point et que le project est un # alors on peut le placer
                    #sinon on laisse les points comme avant
                    if self.matrix[num_lignes,num_colonnes] == '.' and project.matrix[idx_project_row,idx_project_column] != '.':
                        self.matrix[num_lignes, num_colonnes] = project.matrix[idx_project_row, idx_project_column]
                    idx_project_column += 1
                idx_project_row += 1
            return project
        else:
            return False
