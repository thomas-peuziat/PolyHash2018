"""CityPlan : classe permettant de modéliser une ville"""


class CityPlan:

    def __init__(self, matrix, name, dist):
        """
        Constructeur de la classe CityPlan

         :param: matrix: correspond à la matrice de la CityPlan
         :param: name: correspond au nom de la CityPlan (généralement le nom du fichier sans l'extension)
         :param: dist: correspond à la distance de manhattan

         :Example:
            mon_cityPlan = CityPlan(matrix, "a_example", 3)
        """
        self.matrix = matrix
        self.name_project = name
        self.dist_manhattan_max = dist

    def add(self, project, row: int, column: int, id_replica):
        """
        add permet d'ajouter un projet dans un cityPlan

         :param: project: correspond à la matrice que l'on veut ajouter à la cityplan
         :param: row: correspond au numéro de ligne où on veut ajouter le projet
         :param: column: correspond au numéro de colonne où on veut ajouter le projet
         :param: id_replica: correspond au numéro du replica que l'on veut ajouter
         :return: le projet qui vient d'être placé / False si on n'a pas pu le placer
         :rtype: (numpy.array ou booléen)

         :Example:
            cityplan.add(mon_projet, ligne, colonne, id)
        """
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
                        self.matrix[num_lignes, num_colonnes] = id_replica
                        #project.matrix[idx_project_row, idx_project_column]
                    idx_project_column += 1
                idx_project_row += 1
            return project
        else:
            return False
