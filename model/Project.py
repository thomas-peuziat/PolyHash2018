

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
                haut = False
                bas = False
                droite = False
                gauche = False

                point_haut = None
                point_droit = None
                point_bas = None
                point_gauche = None

                cpt_decalage_haut = 0
                cpt_decalage_droite = 0
                cpt_decalage_bas = 0
                cpt_decalage_gauche = 0

                #tester vers le haut
                if 0 <= case[0]-(dist-i) <= nb_row_matrix-1:
                    if (case[0]-(dist-i), case[1]) not in list_coordinates_full:
                        matrix[(case[0]-(dist-i), case[1])]='#'
                        list_valid_coordinates.append((case[0]-(dist-i), case[1]))
                        point_haut=(case[0]-(dist-i), case[1])
                        haut=True
                elif case[0] - (dist-i) < 0:
                    j=i
                    while case[0]-(dist-j) < 0:
                        cpt_decalage_haut+=1
                        j+=1
                    haut=True
                    point_haut = (case[0] - (dist - j), case[1])

                # tester vers la droite
                if 0 <= case[1] + (dist - i) <= nb_column_matrix - 1:
                        if (case[0], case[1] + (dist - i)) not in list_coordinates_full:
                            matrix[case[0], case[1] + (dist - i)]='#'
                            list_valid_coordinates.append((case[0], case[1] + (dist - i)))
                            point_droit=(case[0], case[1] + (dist - i))
                            droite=True
                elif case[1] + (dist - i) > nb_column_matrix -1:
                    j=i
                    while case[1] + (dist - j) > nb_column_matrix-1:
                        cpt_decalage_droite+=1
                        j+=1
                    droite = True
                    point_droit = (case[0], case[1] + (dist - j))

                #tester vers le bas
                #si notre cas ne dépasse pas les limites de la matrice
                if 0 <= case[0]+(dist-i) <= nb_row_matrix-1:
                    #si la case n'est pas déjà présente dans notre liste
                    if (case[0]+(dist-i), case[1]) not in list_coordinates_full:
                        matrix[(case[0]+(dist-i), case[1])]='#'
                        list_valid_coordinates.append((case[0]+(dist-i), case[1]))
                        point_bas = (case[0]+(dist-i), case[1])
                        bas=True
                elif case[0] + (dist - i) > nb_row_matrix-1:
                    j=i
                    while case[0] + (dist - j) > nb_row_matrix -1:
                        cpt_decalage_bas+=1
                        j+=1
                    bas = True
                    point_bas = (case[0] + (dist - j), case[1])

                #tester vers la gauche
                if 0 <= case[1]-(dist-i) <= nb_column_matrix-1:
                    if (case[0], case[1]-(dist-i)) not in list_coordinates_full:
                        matrix[(case[0], case[1]-(dist-i))]='#'
                        list_valid_coordinates.append((case[0], case[1]-(dist-i)))
                        point_gauche = (case[0], case[1]-(dist-i))
                        gauche=True
                elif case[1] - (dist - i) < 0:
                    j=i
                    while case[1] - (dist - j) < 0:
                        cpt_decalage_gauche+=1
                        j+=1
                    gauche = True
                    point_gauche = (case[0], case[1] - (dist-j))


                if haut and droite:
                    #diagonale haut droite
                    self._diagonale_haut_droit(point_haut,point_droit,list_valid_coordinates, list_coordinates_full, matrix, cpt_decalage_haut, cpt_decalage_droite)
                if droite and bas:
                    #diagonale bas droite
                    self._diagonale_droit_bas(point_droit, point_bas, list_valid_coordinates, list_coordinates_full, matrix, cpt_decalage_droite, cpt_decalage_bas)
                if bas and gauche:
                    #diagonale bas gauche
                    self._diagonale_bas_gauche(point_bas, point_gauche, list_valid_coordinates, list_coordinates_full, matrix, cpt_decalage_bas, cpt_decalage_gauche)
                if gauche and haut:
                    #diagonale haut gauche
                    self._diagonale_gauche_haut(point_gauche, point_haut, list_valid_coordinates, list_coordinates_full, matrix, cpt_decalage_gauche, cpt_decalage_haut)

        return list_valid_coordinates


    def _diagonale_haut_droit(self, point_A, point_B, list_valid_coordinates, list_coordinates_full, matrix, cpt_decalage_haut=0, cpt_decalage_droite=0):
        nb_row_matrix, nb_column_matrix = matrix.shape

        if(cpt_decalage_haut!=0):
            if 0 <= point_A[0] <= nb_row_matrix - 1 and 0 <= point_A[1]+cpt_decalage_haut <= nb_column_matrix - 1:
                if (point_A[0], point_A[1]+cpt_decalage_haut) not in list_coordinates_full:
                    point_A =(point_A[0], point_A[1]+cpt_decalage_haut)
                    matrix[point_A[0], point_A[1]]='#'
                    list_valid_coordinates.append((point_A[0], point_A[1]))

        if(cpt_decalage_droite!=0):
            if 0 <= point_B[0]-cpt_decalage_droite <= nb_row_matrix - 1 and 0 <= point_B[1] <= nb_column_matrix - 1:
                if (point_B[0]-cpt_decalage_droite, point_B[1]) not in list_coordinates_full:
                    point_B = (point_B[0]-cpt_decalage_droite, point_B[1])
                    matrix[point_B[0],point_B[1]]='#'
                    list_valid_coordinates.append((point_B[0], point_B[1]))

        while point_A[0] != point_B[0] and point_A[1] != point_B[1]:
            if 0 <= point_A[0] <= nb_row_matrix - 1 and 0 <= point_A[1] <= nb_column_matrix - 1:
                if (point_A[0], point_A[1]) not in list_coordinates_full:
                    matrix[point_A[0], point_A[1]] = '#'
            point_A = (point_A[0] + 1, point_A[1] + 1)



    def _diagonale_droit_bas(self, point_A, point_B, list_valid_coordinates, list_coordinates_full, matrix, cpt_decalage_droit=0, cpt_decalage_bas=0):
        nb_row_matrix, nb_column_matrix = matrix.shape

        if (cpt_decalage_droit != 0):
            if 0 <= point_A[0]+cpt_decalage_droit <= nb_row_matrix - 1 and 0 <= point_A[1] <= nb_column_matrix - 1:
                if (point_A[0]+cpt_decalage_droit, point_A[1]) not in list_coordinates_full:
                    point_A = (point_A[0]+cpt_decalage_droit, point_A[1])
                    matrix[point_A[0], point_A[1]] = '#'
                    list_valid_coordinates.append((point_A[0], point_A[1]))

        if (cpt_decalage_bas != 0):
            if 0 <= point_B[0] <= nb_row_matrix - 1 and 0 <= point_B[1]+cpt_decalage_bas <= nb_column_matrix - 1:
                if (point_B[0], point_B[1]+cpt_decalage_bas) not in list_coordinates_full:
                    point_B = (point_B[0], point_B[1]+cpt_decalage_bas)
                    matrix[point_B[0], point_B[1]] = '#'
                    list_valid_coordinates.append((point_B[0], point_B[1]))

        while point_A[0] != point_B[0] and point_A[1] != point_B[1]:
            if 0 <= point_A[0] <= nb_row_matrix - 1 and 0 <= point_A[1] <= nb_column_matrix - 1:
                if (point_A[0], point_A[1]) not in list_coordinates_full:
                    matrix[point_A[0], point_A[1]] = '#'
            point_A = (point_A[0] + 1, point_A[1] - 1)

    def _diagonale_bas_gauche(self, point_A, point_B, list_valid_coordinates, list_coordinates_full, matrix, cpt_decalage_bas=0, cpt_decalage_gauche=0):
        nb_row_matrix, nb_column_matrix = matrix.shape

        if (cpt_decalage_bas != 0):
            if 0 <= point_A[0] <= nb_row_matrix - 1 and 0 <= point_A[1]-cpt_decalage_bas <= nb_column_matrix - 1:
                if (point_A[0], point_A[1]-cpt_decalage_bas) not in list_coordinates_full:
                    point_A = (point_A[0], point_A[1]-cpt_decalage_bas)
                    matrix[point_A[0], point_A[1]] = '#'
                    list_valid_coordinates.append((point_A[0], point_A[1]))

        if (cpt_decalage_gauche != 0):
            if 0 <= point_B[0]+cpt_decalage_gauche <= nb_row_matrix - 1 and 0 <= point_B[1] <= nb_column_matrix - 1:
                if (point_B[0]+cpt_decalage_gauche, point_B[1]) not in list_coordinates_full:
                    point_B = (point_B[0]+cpt_decalage_gauche, point_B[1])
                    matrix[point_B[0], point_B[1]] = '#'
                    list_valid_coordinates.append((point_B[0], point_B[1]))

        while point_A[0] != point_B[0] and point_A[1] != point_B[1]:
            if 0 <= point_A[0] <= nb_row_matrix - 1 and 0 <= point_A[1] <= nb_column_matrix - 1:
                if (point_A[0], point_A[1]) not in list_coordinates_full:
                    matrix[point_A[0], point_A[1]] = '#'
            point_A = (point_A[0] - 1, point_A[1] - 1)

    def _diagonale_gauche_haut(self, point_A, point_B, list_valid_coordinates, list_coordinates_full, matrix, cpt_decalage_gauche=0, cpt_decalage_haut=0):
        nb_row_matrix, nb_column_matrix = matrix.shape

        if(cpt_decalage_gauche!=0):
            if 0 <= point_A[0]-cpt_decalage_gauche <= nb_row_matrix - 1 and 0 <= point_A[1] <= nb_column_matrix - 1:
                if (point_A[0]-cpt_decalage_gauche, point_A[1]) not in list_coordinates_full:
                    point_A =(point_A[0]-cpt_decalage_gauche, point_A[1])
                    matrix[point_A[0], point_A[1]]='#'
                    list_valid_coordinates.append((point_A[0], point_A[1]))

        if(cpt_decalage_haut!=0):
            if 0 <= point_B[0] <= nb_row_matrix - 1 and 0 <= point_B[1]-cpt_decalage_haut <= nb_column_matrix - 1:
                if (point_B[0], point_B[1]-cpt_decalage_haut) not in list_coordinates_full:
                    point_B = (point_B[0], point_B[1]-cpt_decalage_haut)
                    matrix[point_B[0],point_B[1]]='#'
                    list_valid_coordinates.append((point_B[0], point_B[1]))

        while point_A[0] != point_B[0] and point_A[1] != point_B[1]:
            if 0 <= point_A[0] <= nb_row_matrix - 1 and 0 <= point_A[1] <= nb_column_matrix - 1:
                if (point_A[0], point_A[1]) not in list_coordinates_full:
                    matrix[point_A[0], point_A[1]] = '#'
            point_A = (point_A[0] - 1, point_A[1] + 1)