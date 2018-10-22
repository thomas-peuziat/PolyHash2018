"""PARSER : Passerelle entre les fichiers de données (dans polyhash/data/) et le reste du programme.

Le parser peut traiter des fichiers formatés en entrée et va fournir des fichiers formatés en
sorti, voir https://hashcode.withgoogle.com/2018/tasks/hashcode2018_final_task.pdf categorie "Input data set"
et "Submissions"

"""

import os.path  # Utile pour la compatibilite format de path entre OS
import numpy as np
from model.CityPlan import CityPlan
from model.Residential import Residential
from model.Utility import Utility
import scipy.misc as smp


def parse(filename) -> (CityPlan, list):
    """
    Extrait les données d'un fichier formaté, situé dans le dossier "[...]/polyhash2018/data/input/"

    :param filename: Nom du fichier (sans extension)
    :return: Données utilisables (CityPlan et project_tab)
    :rtype: (CityPlan, list)

    :Example:
        parse("a_example")
    """

    path = os.path.join(os.path.curdir, 'data', 'input', filename + '.in')
    with open(path, 'r') as input_file:

        #### CityPlan
        grid_string = input_file.readline()  # Ex: "4 7 2 3\n"
        grid = grid_string.splitlines()[0].split()  # ['4', '7', '2', '3']
        for i in range(len(grid)):  # [4, 7, 2, 3]
            grid[i] = int(grid[i])

        city_plan = CityPlan(np.full((grid[0], grid[1]), '.'), filename, grid[2])

        #### Project
        id_project = 0
        project_tab = []
        while 'le fichier contient des lignes non analysees':
            description_string = input_file.readline()  # "R 3 2 25\n"

            if description_string == '':  # Verifie si on est arrive en fin de ligne
                break

            description = description_string.splitlines()[0].split()  # ['R', '3', '2', '25']
            plan_string = []
            plan = []
            plan_np = None
            project = None
            for i in range(int(description[1])):
                plan_string.append(input_file.readline())  # ['.#\n', '##\n', '.#\n']
                plan.append(list(plan_string[i].splitlines()[0]))  # [['.', '#'], ['#', '#'], ['.', '#']]
                plan_np = np.asarray(plan, dtype=np.dtype('U5')) # https://docs.scipy.org/doc/numpy-1.15.1/reference/arrays.dtypes.html#string-dtype-note
                for idx_row, val_row in enumerate(plan_np):
                    for idx_column, val_element in enumerate(val_row):
                        if val_element == '#':
                            plan_np[idx_row][idx_column] = str(id_project)
            if description[0] == 'R':
                project = Residential(id_project, plan_np, int(description[3]))
            elif description[0] == 'U':
                project = Utility(id_project, plan_np, int(description[3]))

            project_tab.append(project)
            id_project += 1

    return city_plan, project_tab


def textify(replica_list, filename):
    """
    Créer un fichier de sortie, situé dans le dossier "[...]/polyhash2018/data/output/", grâce aux données en entrées

    :param replica_list: Liste des projets placés (liste des répliques de projets réalisées)
    :param filename: Nom de sortie du fichier (sans extension)

    :Example:
        replica_list = [[0, [0, 0]], [0, [5, 5]], [1, [3, 8]]]
        ...
        textify(replica_list, "a_example")
    """

    path = os.path.join(os.path.curdir, 'data', 'output', filename + '.out')
    with open(path, 'w') as output_file:
        output_file.write(str(len(replica_list)) + '\n')

        # [3, [[0, [0, 0]], [0, [5, 5]], [1, [3, 8]]]]
        # Correspond à :
        # [len_replica_list, [replica_list]]
        # replica_list = [replica]
        # replica = [id_project, [top_left_row, top_left_column]]

        for replica_idx in range(len(replica_list)):
            output_file.write(str(replica_list[replica_idx][0]) + ' ' + str(replica_list[replica_idx][1][0]) + ' ' +
                              str(replica_list[replica_idx][1][1]) + '\n')


def imgify(cityplan, project_list, replica_list, filename):
    """
        Créer une image représentant le plan final, situé dans le dossier "[...]/polyhash2018/data/output/", grâce aux données en entrées

        :param cityplan: Objet CityPlan
        :param replica_list: Liste des projets placés (liste des répliques de projets réalisées)
        :param filename: Nom de sortie du fichier (sans extension)

        :Example:
            cityplan = CityPlan( ...
            replica_list = [3, [[0, [0, 0]], [0, [5, 5]], [1, [3, 8]]]]
            ...
            imgify(cityplan, replica_list, "a_example")
        """

    # TODO : afficher en couleurs les batiments
    path = os.path.join(os.path.curdir, 'data', 'output', filename + '.png')

    row_max, column_max = cityplan.matrix.shape
    data = np.zeros((row_max, column_max, 3), dtype=np.uint8)

    for replica in replica_list:
        position = replica[1]
        project = project_list[replica[0]]
        color = [255, 255, 255]

        if type(project) == Residential:
            color = [255, 0, 0]
        elif type(project) == Utility:
            color = [0, 180, 0]

        for idx_row, val_row in enumerate(project.matrix):
            for idx_column, val_element in enumerate(val_row):
                real_row_position = idx_row + position[0]
                real_column_position = idx_column + position[1]
                if val_element != '.':
                    data[real_row_position][real_column_position] = color
                else:
                    data[real_row_position][real_column_position] = [0, 0, 0]

    img = smp.toimage(data)
    img.save(path)
    # img.show()
