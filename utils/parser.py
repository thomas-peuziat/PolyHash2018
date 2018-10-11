"""PARSER : Passerelle entre les fichiers de données (dans polyhash/data/) et le reste du programme.

Le parser peut traiter des fichiers formatés en entrée et va fournir des fichiers formatés en
sorti, voir https://hashcode.withgoogle.com/2018/tasks/hashcode2018_final_task.pdf categorie "Input data set"
et "Submissions"

"""

import os.path  # Utile pour la compatibilite format de path entre OS


def parse(filename):
    """
    Extrait les données d'un fichier formaté, situé dans le dossier "[...]/polyhash2018/data/input/"

    :param filename: Nom du fichier (sans extension)
    :return: Données utilisables

    :Example:
        parse("a_example")
    """

    path = os.path.join(os.path.pardir, 'data', 'input', filename + '.in')
    with open(path, 'r') as input_file:
        grid_string = input_file.readline()  # Ex: "4 7 2 3\n"
        grid = grid_string.splitlines()[0].split()  # ['4', '7', '2', '3']
        for i in range(len(grid)):  # [4, 7, 2, 3]
            grid[i] = int(grid[i])

        # TODO : grid -> PlanVille

        project_list = []
        while 'le fichier contient des lignes non analysees':
            description_string = input_file.readline()  # "R 3 2 25\n"

            if description_string == '':  # Verifie si on est arrive en fin de ligne
                break

            description = description_string.splitlines()[0].split()  # ['R', '3', '2', '25']
            for i in range(len(description) - 1, 0, -1):  # ['R', 3, 2, 25]
                description[i] = int(description[i])

            plan_string = []
            plan = []
            for i in range(description[1]):
                plan_string.append(input_file.readline())  # ['.#\n', '##\n', '.#\n']
                plan.append(
                    list(plan_string[i].splitlines()[0]))  # [['.', '#'], ['#', '#'], ['.', '#']]

            project = [description, plan]
            project_list.append(project)

        # TODO : project_list -> dict(Building)
    return grid, project_list

def textify(building_list, filename):
    """
    Créer un fichier de sortie, situé dans le dossier "[...]/polyhash2018/data/output/", grâce aux données en entrées

    :param building_list: Liste de projets placés (bâtiments)
    :param filename: Nom de sortie du fichier (sans extension)

    :Example:
        building_list = []
        ...
        textify(building_list, "a_example")
    """
    # list_len = len(building_list)
    #
    # path = os.path.join(os.path.pardir, 'data', 'output', filename + '.out')
    # with open(path, 'w') as output_file:
    #     output_file.write(str(list_len) + '\n')

        #for i in range(list_len):
            #ID building
            #Row top left corner
            #column top left corner


# liste = [3, 3, 4]
# textify(liste, "testother")