

class Project:

    def __init__(self, id, matrix):
        self.id = id
        self.matrix = matrix
        self.shape = matrix.shape
        self.list_pos_replica = []

    # acces aux valeurs de la matrice la ligne puis la colonne
    """
    Fonction permettant de savoir si on peut placer une matrice dans une autre
    param :
    destination_matrix : la matrice dans laquelle on veut se placer
    row : numéro de la ligne où l'on veut placer notre projet
    column : numéro de la colonne où l'on veut placer notre projet

    return : True si c'est possible de le placer et Fakse sinon
    """
    def is_placeable(self, destination_matrix, row: int, column: int) -> bool:
        try:
            idx_project_row = 0
            idx_project_column = 0
            if destination_matrix[row, column] != '.' and self.matrix[idx_project_row, idx_project_column] != '.':
                return False
            else:

                project_row, project_column = self.shape
                # on parcourt a partir de row definie jusqu'a
                # la row + le nombre de lignes du batiments
                for num_lignes in range(row, row + project_row):
                    idx_project_column = 0
                    
                    # on parcourt a partir de la column definie jusqu'a
                    # la column + le nombre de colonnes du batiments
                    for num_colonnes in range(column, column + project_column):
                        if destination_matrix[num_lignes, num_colonnes] != '.' and self.matrix[idx_project_row, idx_project_column] != '.':
                            return False
                        idx_project_column += 1
                    idx_project_row += 1

                return True
        except IndexError:
            return False
