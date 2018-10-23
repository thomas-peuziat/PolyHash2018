

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


    """
    Fonction permettant de retourner une liste de position représentant la surface couverte par (le batiment + la distance de manhattan)
    :parameter
    dist = la distance de manhattan
    matrix = la matrice du CityPlan
    list_coordinates_full = les positions remplies par le batiment
    """
    def get_manhattan_surface(self, dist, matrix, list_coordinates_full):
        list_valid_coordinates = []
        nb_row_matrix, nb_column_matrix = matrix.shape

        for i in range(dist):

            for case in list_coordinates_full:
                haut=False
                base=False
                droite=False
                gauche=False

                point_haut=None
                point_droit=None

                #tester vers le haut
                if 0 <= case[0]-(dist-i) <= nb_row_matrix-1:
                    if matrix[case[0]-(dist-i), case[1]] == '.':
                        if (case[0]-(dist-i), case[1]) not in list_valid_coordinates:
                            list_valid_coordinates.append((case[0]-(dist-i), case[1]))
                            matrix[case[0] - (dist - i)][case[1]] = '#'
                            point_haut=(case[0]-(dist-i), case[1])
                            haut=True

                # tester vers la droite
                if 0 <= case[1] + (dist - i) <= nb_column_matrix - 1:
                    if matrix[case[0], case[1] + (dist - i)] == '.':
                        if (case[0], case[1] + (dist - i)) not in list_valid_coordinates:
                            list_valid_coordinates.append((case[0], case[1] + (dist - i)))
                            matrix[case[0]][case[1] + (dist - i)] = '#'
                            point_droit=(case[0], case[1] + (dist - i))
                            droite=True

                #tester vers le bas
                #si notre cas ne dépasse pas les limites de la matrice
                if 0 <= case[0]+(dist-i) <= nb_row_matrix-1:
                    #si la case testée est un point (=> la case est libre)
                    if matrix[case[0]+(dist-i), case[1]] == '.':
                        #si la case n'est pas déjà présente dans notre liste
                        if (case[0]+(dist-i), case[1]) not in list_valid_coordinates:
                            list_valid_coordinates.append((case[0]+(dist-i), case[1]))
                            matrix[case[0]+(dist-i)][case[1]] = '#'
                            bas=True

                #tester vers la gauche
                if 0 <= case[1]-(dist-i) <= nb_column_matrix-1:
                    if matrix[case[0], case[1]-(dist-i)] == '.':
                        if (case[0], case[1]-(dist-i)) not in list_valid_coordinates:
                            list_valid_coordinates.append((case[0], case[1]-(dist-i)))
                            matrix[case[0]][case[1]-(dist-i)] = '#'
                            gauche=True


                print("\n",case,'\n', matrix,list_valid_coordinates,"\n")

                if haut and droite:
                    #diagonale haut droite
                    #print(point_haut,'\n',point_droit,'\n')
                    self._diagonale_haut_droit(point_haut,point_droit,list_valid_coordinates, matrix)

                # if droite and bas:
                #     #diagonale bas droite
                #
                # if bas and gauche:
                #     #diagonale bas gauche
                #
                # if haut and gauche:
                #     #diagonale haut gauche


        return list_valid_coordinates


    def _diagonale_haut_droit(self, point_A, point_B, list_valid_coordinates, matrix):
        nb_row_matrix, nb_column_matrix = matrix.shape


        while point_A[0] != point_B[0] and point_A[1] != point_B[1]:
            point_A = (point_A[0]+1, point_A[1]+1)

            if 0 <= point_A[0]<= nb_row_matrix - 1 and 0 <= point_A[1] <= nb_column_matrix - 1:
                if matrix[point_A[0], point_A[1]] == '.':
                    if (point_A[0], point_A[1]) not in list_valid_coordinates:
                        matrix[point_A[0], point_A[1]] = '#'
    #TODO si une surface dépasse de la matrice, on perd des diagonales -- y remédier
        return ""
