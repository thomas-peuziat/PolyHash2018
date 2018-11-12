

class Project:

    def __init__(self, id, matrix):
        self.id = id
        self.matrix = matrix
        self.shape = matrix.shape

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

                # tester vers le haut
                # si notre cas ne dépasse pas les limites de la matrice
                if 0 <= case[0]-(dist-i) <= nb_row_matrix-1:
                    # si la case ne fait pas partie du batiment
                    if (case[0]-(dist-i), case[1]) not in list_coordinates_full:
                        # on ajoute les coordonnées comme étant valides
                        list_valid_coordinates.append((case[0]-(dist-i), case[1]))
                        # on retient le point_haut qui vient d'être ajouté
                        point_haut = (case[0]-(dist-i), case[1])
                        # on notifie (par un booléen) que l'on vient d'ajouter une case vers le haut
                        haut = True
                # si notre cas dépasse les limites de la matrice (cas permettant de faire les diagonales)
                elif case[0] - (dist-i) < 0:
                    j = i
                    # on fait une boucle permettant de savoir de combien de case nous avons dépassé la matrice
                    while case[0]-(dist-j) < 0:
                        cpt_decalage_haut += 1
                        j += 1
                    # on notifie (par un booléen) que l'on vient d'ajouter une case vers le haut
                    haut = True
                    # on retient le point_haut qui vient d'être ajouté
                    point_haut = (case[0] - (dist - j), case[1])



                # tester vers la droite
                # si notre cas ne dépasse pas les limites de la matrice
                if 0 <= case[1] + (dist - i) <= nb_column_matrix - 1:
                    # si la case ne fait pas partie du batiment
                    if (case[0], case[1] + (dist - i)) not in list_coordinates_full:
                            # on ajoute les coordonnées comme étant valides
                            list_valid_coordinates.append((case[0], case[1] + (dist - i)))
                            # on retient le point_droit qui vient d'être ajouté
                            point_droit = (case[0], case[1] + (dist - i))
                            # on notifie (par un booléen) que l'on vient d'ajouter une case vers la droite
                            droite = True
                # si notre cas dépasse les limites de la matrice (cas permettant de faire les diagonales)
                elif case[1] + (dist - i) > nb_column_matrix - 1:
                    j = i
                    # on fait une boucle permettant de savoir de combien de case nous avons dépassé la matrice
                    while case[1] + (dist - j) > nb_column_matrix-1:
                        cpt_decalage_droite += 1
                        j += 1
                    # on notifie (par un booléen) que l'on vient d'ajouter une case vers la droite
                    droite = True
                    # on retient le point_droit qui vient d'être ajouté
                    point_droit = (case[0], case[1] + (dist - j))

                # tester vers le bas
                # si notre cas ne dépasse pas les limites de la matrice
                if 0 <= case[0]+(dist-i) <= nb_row_matrix-1:
                    # si la case ne fait pas partie du batiment
                    if (case[0]+(dist-i), case[1]) not in list_coordinates_full:
                        # on ajoute les coordonnées comme étant valides
                        list_valid_coordinates.append((case[0]+(dist-i), case[1]))
                        # on retient le point_bas qui vient d'être ajouté
                        point_bas = (case[0]+(dist-i), case[1])
                        # on notifie (par un booléen) que l'on vient d'ajouter une case vers le bas
                        bas = True
                # si notre cas dépasse les limites de la matrice (cas permettant de faire les diagonales)
                elif case[0] + (dist - i) > nb_row_matrix-1:
                    j = i
                    # on fait une boucle permettant de savoir de combien de case nous avons dépassé la matrice
                    while case[0] + (dist - j) > nb_row_matrix - 1:
                        cpt_decalage_bas += 1
                        j += 1
                    # on notifie (par un booléen) que l'on vient d'ajouter une case vers le bas
                    bas = True
                    # on retient le point_bas qui vient d'être ajouté
                    point_bas = (case[0] + (dist - j), case[1])

                # tester vers la gauche
                # si notre cas ne dépasse pas les limites de la matrice
                if 0 <= case[1]-(dist-i) <= nb_column_matrix-1:
                    # si la case ne fait pas partie du batiment
                    if (case[0], case[1]-(dist-i)) not in list_coordinates_full:
                        # on ajoute les coordonnées comme étant valides
                        list_valid_coordinates.append((case[0], case[1]-(dist-i)))
                        # on retient le point_gauche qui vient d'être ajouté
                        point_gauche = (case[0], case[1]-(dist-i))
                        # on notifie (par un booléen) que l'on vient d'ajouter une case vers la gauche
                        gauche = True
                # si notre cas dépasse les limites de la matrice (cas permettant de faire les diagonales)
                elif case[1] - (dist - i) < 0:
                    j = i
                    # on fait une boucle permettant de savoir de combien de case nous avons dépassé la matrice
                    while case[1] - (dist - j) < 0:
                        cpt_decalage_gauche += 1
                        j += 1
                    # on notifie (par un booléen) que l'on vient d'ajouter une case vers la gauche
                    gauche = True
                    # on retient le point_gauche qui vient d'être ajouté
                    point_gauche = (case[0], case[1] - (dist-j))

                # dans le cas où nous avons ajouté un point en haut et à droite
                if haut and droite:
                    # on remplit la diagonale entre les deux points (diagonale haut droite)
                    self._diagonale_haut_droit(point_haut,point_droit,list_valid_coordinates, list_coordinates_full, matrix, cpt_decalage_haut, cpt_decalage_droite)
                # dans le cas où nous avons ajouté un point à droite et en bas
                if droite and bas:
                    # on remplit la diagonale entre les deux points (diagonale bas droite)
                    self._diagonale_droit_bas(point_droit, point_bas, list_valid_coordinates, list_coordinates_full, matrix, cpt_decalage_droite, cpt_decalage_bas)
                # dans le cas où nous avons ajouté un point en bas et à gauche
                if bas and gauche:
                    # on remplit la diagonale entre les deux points (diagonale bas gauche)
                    self._diagonale_bas_gauche(point_bas, point_gauche, list_valid_coordinates, list_coordinates_full, matrix, cpt_decalage_bas, cpt_decalage_gauche)
                # dans le cas où nous avons ajouté un point à gauche et en haut
                if gauche and haut:
                    # on remplit la diagonale entre les deux points (diagonale haut gauche)
                    self._diagonale_gauche_haut(point_gauche, point_haut, list_valid_coordinates, list_coordinates_full, matrix, cpt_decalage_gauche, cpt_decalage_haut)

        # on supprime les doublons de la liste et on return
        list_valid_coordinates = set(list_valid_coordinates)
        return list_valid_coordinates

    """
    Méthode permettant d'ajouter à la liste les diagonales entre deux points (haut et droit)
    :parameter
    point_A = point correspondant à point_haut (si dépassement des limites de la matrice, alors il a pour numéro de ligne :0)
    point_B = point correspondant à point_droit (si dépassement des limites de la matrice, alors il a pour numéro de colonnes : max(numéro de colonnes de la matrice)
    list_valid_coordinates = liste contenant les positions de la surface de manhattan
    list_coordinates_full = liste contenant les positions du bâtiment
    matrix = la matrice du cityPlan
    cpt_decalage_haut = compteur représentant de combien le point à dépasser vers le haut
    cpt_decalage_droite = compteur représentant de combien le point à dépasser vers la droite
    """
    def _diagonale_haut_droit(self, point_A, point_B, list_valid_coordinates, list_coordinates_full, matrix, cpt_decalage_haut=0, cpt_decalage_droite=0):
        # on récupère la taille de la matrice
        nb_row_matrix, nb_column_matrix = matrix.shape

        # s'il y avait un dépassement de la matrice vers le haut
        if cpt_decalage_haut != 0:
            # si le point_A avec le décalage est toujours dans la matrice
            if 0 <= point_A[0] <= nb_row_matrix - 1 and 0 <= point_A[1]+cpt_decalage_haut <= nb_column_matrix - 1:
                # si le point_A avec le décalage ne fait pas partie du batiment
                if (point_A[0], point_A[1]+cpt_decalage_haut) not in list_coordinates_full:
                    # alors on le redéfinit et on l'ajoute à la liste des positions de la surface de manhattan
                    point_A = (point_A[0], point_A[1]+cpt_decalage_haut)
                    list_valid_coordinates.append((point_A[0], point_A[1]))

        # s'il y avait un dépassement de la matrice vers la droite
        if cpt_decalage_droite != 0:
            # si le point_B avec le décalage est toujours dans la matrice
            if 0 <= point_B[0]-cpt_decalage_droite <= nb_row_matrix - 1 and 0 <= point_B[1] <= nb_column_matrix - 1:
                # si le point_B avec le décalage ne fait pas partie du batiment
                if (point_B[0]-cpt_decalage_droite, point_B[1]) not in list_coordinates_full:
                    # alors on le redéfinit et on l'ajoute à la liste des positions de la surface de manhattan
                    point_B = (point_B[0]-cpt_decalage_droite, point_B[1])
                    list_valid_coordinates.append((point_B[0], point_B[1]))

        # on complète la diagonale entre le point_A et le point_B
        # tant que le point_A est différent du point_B
        while point_A[0] != point_B[0] and point_A[1] != point_B[1]:
            # si le point_A se trouve dans la matrice
            if 0 <= point_A[0] <= nb_row_matrix - 1 and 0 <= point_A[1] <= nb_column_matrix - 1:
                # si le point_A ne fait pas partie du batiment
                if (point_A[0], point_A[1]) not in list_coordinates_full:
                    # on l'ajoute dans la liste des positions valides
                    list_valid_coordinates.append((point_A[0], point_A[1]))
            # le point_A change en prenant un ligne de plus (vers le bas) et un décalage vers la droite
            point_A = (point_A[0] + 1, point_A[1] + 1)

    """
    Méthode permettant d'ajouter à la liste les diagonales entre deux points (droit et bas)
    :parameter
    point_A = point correspondant à point_droit (si dépassement des limites de la matrice, alors il a pour numéro de colonnes : max(numéro de colonnes de la matrice)
    point_B = point correspondant à point_bas (si dépassement des limites de la matrice, alors il a pour numéro de lignes : max(numéro de lignes de la matrice)
    list_valid_coordinates = liste contenant les positions de la surface de manhattan
    list_coordinates_full = liste contenant les positions du bâtiment
    matrix = la matrice du cityPlan
    cpt_decalage_droit = compteur représentant de combien le point à dépasser vers la droite
    cpt_decalage_bas = compteur représentant de combien le point à dépasser vers le bas
    """
    def _diagonale_droit_bas(self, point_A, point_B, list_valid_coordinates, list_coordinates_full, matrix, cpt_decalage_droit=0, cpt_decalage_bas=0):
        # on récupère la taille de la matrice
        nb_row_matrix, nb_column_matrix = matrix.shape

        # s'il y avait un dépassement de la matrice vers la droite
        if cpt_decalage_droit != 0:
            # si le point_A avec le décalage est toujours dans la matrice
            if 0 <= point_A[0]+cpt_decalage_droit <= nb_row_matrix - 1 and 0 <= point_A[1] <= nb_column_matrix - 1:
                # si le point_A avec le décalage ne fait pas partie du batiment
                if (point_A[0]+cpt_decalage_droit, point_A[1]) not in list_coordinates_full:
                    # alors on le redéfinit et on l'ajoute à la liste des positions de la surface de manhattan
                    point_A = (point_A[0]+cpt_decalage_droit, point_A[1])
                    list_valid_coordinates.append((point_A[0], point_A[1]))

        # s'il y avait un dépassement de la matrice vers le bas
        if cpt_decalage_bas != 0:
            # si le point_B avec le décalage est toujours dans la matrice
            if 0 <= point_B[0] <= nb_row_matrix - 1 and 0 <= point_B[1]+cpt_decalage_bas <= nb_column_matrix - 1:
                # si le point_B avec le décalage ne fait pas partie du batiment
                if (point_B[0], point_B[1]+cpt_decalage_bas) not in list_coordinates_full:
                    # alors on le redéfinit et on l'ajoute à la liste des positions de la surface de manhattan
                    point_B = (point_B[0], point_B[1]+cpt_decalage_bas)
                    list_valid_coordinates.append((point_B[0], point_B[1]))

        # on complète la diagonale entre le point_A et le point_B
        # tant que le point_A est différent du point_B
        while point_A[0] != point_B[0] and point_A[1] != point_B[1]:
            # si le point_A se trouve dans la matrice
            if 0 <= point_A[0] <= nb_row_matrix - 1 and 0 <= point_A[1] <= nb_column_matrix - 1:
                # si le point_A ne fait pas partie du batiment
                if (point_A[0], point_A[1]) not in list_coordinates_full:
                    # on l'ajoute dans la liste des positions valides
                    list_valid_coordinates.append((point_A[0], point_A[1]))
            # le point_A change en prenant un ligne de plus (vers le bas) et un décalage vers la gauche
            point_A = (point_A[0] + 1, point_A[1] - 1)

    """
    Méthode permettant d'ajouter à la liste les diagonales entre deux points (bas et gauche)
    :parameter
    point_A = point correspondant à point_bas (si dépassement des limites de la matrice, alors il a pour numéro de lignes : max(numéro de lignes de la matrice)
    point_B = point correspondant à point_gauche (si dépassement des limites de la matrice, alors il a pour numéro de colonnes : 0)
    list_valid_coordinates = liste contenant les positions de la surface de manhattan
    list_coordinates_full = liste contenant les positions du bâtiment
    matrix = la matrice du cityPlan
    cpt_decalage_bas = compteur représentant de combien le point à dépasser vers le bas
    cpt_decalage_gauche = compteur représentant de combien le point à dépasser vers la gauche
    """
    def _diagonale_bas_gauche(self, point_A, point_B, list_valid_coordinates, list_coordinates_full, matrix, cpt_decalage_bas=0, cpt_decalage_gauche=0):
        # on récupère la taille de la matrice
        nb_row_matrix, nb_column_matrix = matrix.shape

        # s'il y avait un dépassement de la matrice vers le bas
        if cpt_decalage_bas != 0:
            # si le point_A avec le décalage est toujours dans la matrice
            if 0 <= point_A[0] <= nb_row_matrix - 1 and 0 <= point_A[1]-cpt_decalage_bas <= nb_column_matrix - 1:
                # si le point_A avec le décalage ne fait pas partie du batiment
                if (point_A[0], point_A[1]-cpt_decalage_bas) not in list_coordinates_full:
                    # alors on le redéfinit et on l'ajoute à la liste des positions de la surface de manhattan
                    point_A = (point_A[0], point_A[1]-cpt_decalage_bas)
                    list_valid_coordinates.append((point_A[0], point_A[1]))

        # s'il y avait un dépassement de la matrice vers la gauche
        if cpt_decalage_gauche != 0:
            # si le point_B avec le décalage est toujours dans la matrice
            if 0 <= point_B[0]+cpt_decalage_gauche <= nb_row_matrix - 1 and 0 <= point_B[1] <= nb_column_matrix - 1:
                # si le point_B avec le décalage ne fait pas partie du batiment
                if (point_B[0]+cpt_decalage_gauche, point_B[1]) not in list_coordinates_full:
                    # alors on le redéfinit et on l'ajoute à la liste des positions de la surface de manhattan
                    point_B = (point_B[0]+cpt_decalage_gauche, point_B[1])
                    list_valid_coordinates.append((point_B[0], point_B[1]))

        # on complète la diagonale entre le point_A et le point_B
        # tant que le point_A est différent du point_B
        while point_A[0] != point_B[0] and point_A[1] != point_B[1]:
            # si le point_A se trouve dans la matrice
            if 0 <= point_A[0] <= nb_row_matrix - 1 and 0 <= point_A[1] <= nb_column_matrix - 1:
                # si le point_A ne fait pas partie du batiment
                if (point_A[0], point_A[1]) not in list_coordinates_full:
                    # on l'ajoute dans la liste des positions valides
                    list_valid_coordinates.append((point_A[0], point_A[1]))
            # le point_A change en prenant un ligne de moins (vers le haut) et un décalage vers la gauche
            point_A = (point_A[0] - 1, point_A[1] - 1)

    """
    Méthode permettant d'ajouter à la liste les diagonales entre deux points (gauche et haut)
    :parameter
    point_A = point correspondant à point_gauche (si dépassement des limites de la matrice, alors il a pour numéro de colonnes : 0)
    point_B = point correspondant à point_haut (si dépassement des limites de la matrice, alors il a pour numéro de ligne :0)
    list_valid_coordinates = liste contenant les positions de la surface de manhattan
    list_coordinates_full = liste contenant les positions du bâtiment
    matrix = la matrice du cityPlan
    cpt_decalage_gauche = compteur représentant de combien le point à dépasser vers la gauche
    cpt_decalage_haut = compteur représentant de combien le point à dépasser vers le haut
    """
    def _diagonale_gauche_haut(self, point_A, point_B, list_valid_coordinates, list_coordinates_full, matrix, cpt_decalage_gauche=0, cpt_decalage_haut=0):
        # on récupère la taille de la matrice
        nb_row_matrix, nb_column_matrix = matrix.shape

        # s'il y avait un dépassement de la matrice vers la gauche
        if cpt_decalage_gauche != 0:
            # si le point_A avec le décalage est toujours dans la matrice
            if 0 <= point_A[0]-cpt_decalage_gauche <= nb_row_matrix - 1 and 0 <= point_A[1] <= nb_column_matrix - 1:
                # si le point_A avec le décalage ne fait pas partie du batiment
                if (point_A[0]-cpt_decalage_gauche, point_A[1]) not in list_coordinates_full:
                    # alors on le redéfinit et on l'ajoute à la liste des positions de la surface de manhattan
                    point_A =(point_A[0]-cpt_decalage_gauche, point_A[1])
                    list_valid_coordinates.append((point_A[0], point_A[1]))

        # s'il y avait un dépassement de la matrice vers le haut
        if cpt_decalage_haut != 0:
            # si le point_B avec le décalage est toujours dans la matrice
            if 0 <= point_B[0] <= nb_row_matrix - 1 and 0 <= point_B[1]-cpt_decalage_haut <= nb_column_matrix - 1:
                # si le point_B avec le décalage ne fait pas partie du batiment
                if (point_B[0], point_B[1]-cpt_decalage_haut) not in list_coordinates_full:
                    # alors on le redéfinit et on l'ajoute à la liste des positions de la surface de manhattan
                    point_B = (point_B[0], point_B[1]-cpt_decalage_haut)
                    list_valid_coordinates.append((point_B[0], point_B[1]))

        # on complète la diagonale entre le point_A et le point_B
        # tant que le point_A est différent du point_B
        while point_A[0] != point_B[0] and point_A[1] != point_B[1]:
            # si le point_A se trouve dans la matrice
            if 0 <= point_A[0] <= nb_row_matrix - 1 and 0 <= point_A[1] <= nb_column_matrix - 1:
                # si le point_A ne fait pas partie du batiment
                if (point_A[0], point_A[1]) not in list_coordinates_full:
                    # on l'ajoute dans la liste des positions valides
                    list_valid_coordinates.append((point_A[0], point_A[1]))
            # le point_A change en prenant un ligne de moins (vers le haut) et un décalage vers la droite
            point_A = (point_A[0] - 1, point_A[1] + 1)
