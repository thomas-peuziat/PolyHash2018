

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

    #matrix = city_plan
    def get_manhattan_surface(self, dist, matrix):
        #Exemple avec utili
        #list_coordinates_full = [(3,2),(4,1),(4,2),(5,1),(5,3)]

        #Exemple avec resi
        list_coordinates_full = [(1,4),(2,3),(2,4),(3,3),(3,5)]
        list_coordinates_empty = []
        nb_row_matrix, nb_column_matrix = matrix.shape

        for i in range (dist):
            for case in list_coordinates_full:
                if(0<=case[0]+(dist-i)<=nb_row_matrix and matrix[case[0]+(dist-i),case[1]]=='.' and (case[0]+(dist-i),case[1]) not in list_coordinates_empty):
                    list_coordinates_empty.append((case[0]+(dist-i),case[1]))
                    matrix[case[0]+(dist-i)][case[1]]='#'

                if (0<=case[0]-(dist-i)<=nb_row_matrix and matrix[case[0]-(dist-i), case[1]]=='.' and (case[0]-(dist-i),case[1]) not in list_coordinates_empty):
                    list_coordinates_empty.append((case[0]-(dist-i),case[1]))
                    matrix[case[0] - (dist - i)][case[1]] = '#'

                if (0<=case[1]+(dist-i)<=nb_column_matrix and matrix[case[0], case[1]+(dist-i)]=='.' and (case[0],case[1]+(dist-i)) not in list_coordinates_empty):
                    list_coordinates_empty.append((case[0],case[1]+(dist-i)))
                    matrix[case[0]][case[1]+(dist-i)] = '#'

                if (0<=case[1]-(dist-i)<=nb_column_matrix and matrix[case[0], case[1]-(dist-i)]=='.' and (case[0],case[1]-(dist-i)) not in list_coordinates_empty):
                    list_coordinates_empty.append((case[0],case[1]-(dist-i)))
                    matrix[case[0]][case[1]-(dist-i)] = '#'

                if(i>0):
                    diff=dist-i
                    #bas droite
                    if(0<=case[0]+i<=nb_row_matrix and 0<=case[1]+diff<=nb_column_matrix):
                        if(matrix[case[0]+i, case[1]+diff]=='.'):
                            list_coordinates_empty.append((case[0]+i, case[1]+diff))
                            matrix[case[0] + i, case[1] + diff]='#'

                    #bas gauche
                    if(0<=case[0]+i<=nb_row_matrix and 0<=case[1]-diff<=nb_column_matrix):
                        if(matrix[case[0]+i, case[1]-diff]=='.'):
                            list_coordinates_empty.append((case[0]+i, case[1]-diff))
                            matrix[case[0] + i, case[1] - diff]='#'

                    #haut droite
                    if (0 <= case[0] + diff <= nb_row_matrix and 0 <= case[1] + i <= nb_column_matrix):
                        if (matrix[case[0] + diff, case[1] + i] == '.'):
                            list_coordinates_empty.append((case[0] + diff, case[1] + i))
                            matrix[case[0] + diff, case[1] + i] = '#'

                    #haut gauche
                    if (0 <= case[0] - diff <= nb_row_matrix and 0 <= case[1] + i <= nb_column_matrix):
                        if (matrix[case[0] - diff, case[1] + i] == '.'):
                            list_coordinates_empty.append((case[0] - diff, case[1] + i))
                            matrix[case[0] - diff, case[1] + i] = '#'
        print(list_coordinates_empty)
        print(len(list_coordinates_empty))