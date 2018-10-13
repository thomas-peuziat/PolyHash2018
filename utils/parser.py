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


def parse(filename) -> (CityPlan, dict):
    """
    Extrait les données d'un fichier formaté, situé dans le dossier "[...]/polyhash2018/data/input/"

    :param filename: Nom du fichier (sans extension)
    :return: Données utilisables (CityPlan et project_dict)
    :rtype: (CityPlan, dict)

    :Example:
        parse("a_example")
    """

    path = os.path.join(os.path.pardir, 'data', 'input', filename + '.in')
    with open(path, 'r') as input_file:
        grid_string = input_file.readline()  # Ex: "4 7 2 3\n"
        grid = grid_string.splitlines()[0].split()  # ['4', '7', '2', '3']
        for i in range(len(grid)):  # [4, 7, 2, 3]
            grid[i] = int(grid[i])

        city_plan = CityPlan(np.full((grid[0], grid[1]), '.'), filename, grid[2])

        id_project = 0

        # project_dict : [R|U].ligne.colonne.[capacite|type].id
        project_dict = {}
        while 'le fichier contient des lignes non analysees':
            description_string = input_file.readline()  # "R 3 2 25\n"

            if description_string == '':  # Verifie si on est arrive en fin de ligne
                break

            description = description_string.splitlines()[0].split()  # ['R', '3', '2', '25']
            plan_string = []
            plan = []
            for i in range(int(description[1])):
                plan_string.append(input_file.readline())  # ['.#\n', '##\n', '.#\n']
                plan.append(list(plan_string[i].splitlines()[0]))  # [['.', '#'], ['#', '#'], ['.', '#']]

            if description[0] == 'R':
                project = Residential(plan, int(description[3]))
                key = "R." + description[1] + '.' + description[2] + '.' + description[3] + '.' + str(id_project)
                project_dict[key] = project
                id_project += 1
            elif description[0] == 'U':
                project = Utility(plan, int(description[3]))
                key = "U." + description[1] + '.' + description[2] + '.' + description[3] + '.' + str(id_project)
                project_dict[key] = project
                id_project += 1

    return city_plan, project_dict


def textify(building_list, filename):
    """
    Créer un fichier de sortie, situé dans le dossier "[...]/polyhash2018/data/output/", grâce aux données en entrées

    :param building_list: Liste de projets placés (bâtiments)
    :param filename: Nom de sortie du fichier (sans extension)

    :Example:
        building_list = [3, [[0, [0, 0]], [0, [5, 5]], [1, [3, 8]]]]
        ...
        textify(building_list, "a_example")
    """

    path = os.path.join(os.path.pardir, 'data', 'output', filename + '.out')
    with open(path, 'w') as output_file:
        output_file.write(str(building_list[0]) + '\n')

        # [3, [[0, [0, 0]], [0, [5, 5]], [1, [3, 8]]]]
        # Correspond à :
        # [len_building_list, [building_list]]
        # building_list = [building]
        # building = [id_project, [top_left_row, top_left_column]]
        for i in range(building_list[0]):
            output_file.write(str(building_list[1][i][0]) + ' ' + str(building_list[1][i][1][0]) + ' ' +
                              str(building_list[1][i][1][1]) + '\n')

# cityplan, dict = parse("a_example")
# print(cityplan.nameProject, cityplan.distManhattanMax, cityplan.nbProjectPlaced)
# print(dict)
# cityplan.addTo(dict["R.3.2.25.0"], 0, 0)
# print(cityplan.matrix)
