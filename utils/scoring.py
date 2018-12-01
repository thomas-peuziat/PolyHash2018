# Scoring
#
#
#
# Permet de calculer le score d'un output
#
#
#
#
# Ce scoring va permettre d'analyser le fichier d'une entrée formatée afin d'en déduire
# le score de notre implémentation du Google HashCode 2018

from model import Utility
import os.path
import time


def scoring_from_replica_list(replica_list, cityplan, project_list):
    """
     Calcul le score d'une map à partir de la liste des répliques placées sur cette carte

     :param: replica_list : Liste des répliques placées
     :param: cityplan : Objet CityPlan modélisant la carte de travail
     :param: project_list : Liste des projets (bâtiments) associés à la carte
     :return: Résultat du score de la carte
     :rtype: Entier

    """
    utility_list = []
    residential_list = []
    for replica in replica_list:
        project_number = replica[0]  # get the number of the building project
        ## Get top left coordinates
        row_top = replica[1][0]
        col_top = replica[1][1]

        plan = project_list[int(project_number)].matrix
        adapted_coordinates = _coordinates_adaptation(plan, row_top, col_top)

        if type(project_list[int(project_number)]) is Utility.Utility:  # Batiments utilitaire
            utility_list.append([project_number, row_top, col_top, adapted_coordinates])
        else:
            residential_list.append([project_number, row_top, col_top, adapted_coordinates])
    return _scoring(utility_list, residential_list, cityplan, project_list, replica_list)


def scoring_from_output(filename, cityplan, project_list):
    """
     Calcul le score d'une map à partir de son fichier d'un ficier de sortie

     :param: filename : Nom du fichier (sans extensions)
     :param: cityplan : Objet CityPlan modélisant la carte de travail
     :param: project_list : Liste des projets (bâtiments) associés à la carte
     :return: Résultat du score de la carte
     :rtype: Entier

     :Example:
            scoring_from_output("a_example", cityplan, project_list)
    """
    utilitaires_list, residential_list = _output_parser(filename, project_list)
    return _scoring(utilitaires_list, residential_list, cityplan, project_list)


def _scoring(utilitaires_list, residential_list, cityplan, project_list, replica_list=None):
    """
     Fonction appelée pour le calcul du score via replica_list ou project_list

     :param: utilitaires_list: Liste des utilitaires placés sur la map
     :param: residential_list : Liste des résidences placées sur la map
     :param: cityplan : Objet CityPlan modélisant la carte de travail
     :param: project_list : Liste des projets (bâtiments) associés à la carte
     :param: replica_list : Liste des répliques placées
     :return: Le score de la map
     :rtype: Entier

    """
    begin_time = time.time()
    tested_residential = 0
    score = 0
    len_residential_list = len(residential_list)

    print("...Scoring starting...")
    print("Number of residential replica :", len_residential_list)
    print("Number of utilities replica :", len(utilitaires_list))

    for residence in residential_list:
        if (tested_residential % 500) == 0 and tested_residential != 0:
            _affichage_score(tested_residential, len_residential_list, score, begin_time)

        all_resid = residence[3]
        number_project = residence[0]
        types = []
        manhattan_residence_area = project_list[int(number_project)].get_manhattan_surface(
            int(cityplan.dist_manhattan_max), cityplan.matrix, all_resid)

        for coordinates in manhattan_residence_area:
            if str(cityplan.matrix[coordinates]) != ".":
                building = project_list[replica_list[int(cityplan.matrix[coordinates])][0]]
                if type(building) is Utility.Utility:
                    if not (building.type in types):
                        types.append(building.type)
                        score += int(project_list[int(number_project)].capacity)

        tested_residential += 1

    print(" =-=-=-=-=-= =-=-=-=-=-=")
    print("Final score :", score)
    print("--- %s seconds ---" % (time.time() - begin_time))
    print(" =-=-=-=-=-= =-=-=-=-=-=")
    return score


def _distance_manhattan(tab_resid, tab_utils):
    """
     Calcul la distance de manhattan entre un bâtiment résidentiel et un bâtiment utilitaire

     :param: tab_resid : Tableau des coordonnées du bâtiment résidentiel
     :param: tab_utils : Tableau des coordonnées du bâtiment utilitaire
     :return: La distance minimale entre une résidence et un utilitaire
     :rtype: Entier

    """
    min = 999
    for coor_resid in tab_resid:
        for coord_util in tab_utils:
            dist = abs(int(coor_resid[0]) - int(coord_util[0])) + abs(int(coor_resid[1]) - int(coord_util[1]))
            if dist < min:
                min = dist

    return min


def _output_parser(filename, project_list):
    """
     Extrait les bâtiments placés dans le fichier de sortie pour les ajouter à leur liste respective

     :param: filename: Nom du fichier (sans extension)
     :param: project_list : Liste des projets (bâtiments) associés à la carte
     :return: La liste des bâtiments résidentiels et utilitaires
     :rtype: utils : Liste de coordonnées
     :rtype: resid : Liste de coordonnées

    """
    path = os.path.join(os.path.curdir, 'data', 'output', filename + '.out')
    with open(path, 'r') as input_file:
        buildings_number = input_file.readline()  # get the number of buildings placed in the city

        lines = input_file.readlines()  # read the other line from the second
        utils = []
        resid = []

        for line in lines:
            project_number = line.split()[0]  # get the number of the building project
            ## Get top left coordinates
            row_top = line.split()[1]
            col_top = line.split()[2]

            plan = project_list[int(project_number)].matrix
            adapted_coordinates = _coordinates_adaptation(plan, row_top, col_top)

            if type(project_list[int(project_number)]) is Utility.Utility:  # Batiments utilitaire
                utils.append([project_number, row_top, col_top, adapted_coordinates])
            else:
                resid.append([project_number, row_top, col_top, adapted_coordinates])
    return utils, resid


def _coordinates_adaptation(buildingPlan, rowTop, colTop):
    """
     Permet de détermier les coordonnées d'un bâtiment tels quelles sont lorsque celui-ci est sur la map

     :param: buildingPlan : Plan du bâtiment
     :param: rowTop : ligne top_left du bâtiment sur la map
     :param: colTop : colonne top_left du bâtiment sur la map
     :return: Liste des coordonnées complètes d'un bâtiment

    """
    list_coordinates = []
    indexRow = 0
    for line in buildingPlan:
        indexCol = 0
        for col in line:
            if col != ".":
                list_coordinates.append([indexRow, indexCol])
            indexCol += 1
        indexRow += 1

    for cases in list_coordinates:
        cases[0] += int(rowTop)
        cases[1] += int(colTop)

    return list_coordinates


"""
        Optimisation des cases sur lesquelles il faut réellement calculer la distance de Manhattan
        Par exemple sur deux batiments sont l'un à coté de l'autre, il est inutile de calculer la distance de Manhattan des deux extrémitées

"""


def building_score(cityplan, row, col, project_list, project_number, replica_list):
    """
     Calcul du score d'un bâtiment particulier

     :param: cityplan : Objet CityPlan modélisant la carte de travail
     :param: row : ligne top_left du bâtiment sur la map
     :param: col : colonne top_left du bâtiment sur la map
     :param: project_list : Liste des projets (bâtiments) associés à la carte
     :param: project_number : Numéro de projet du bâtiment
     :param: replica_list : Liste des répliques placées
     :return: Score du bâtiment
     :rtype: Entier

    """
    plan = project_list[int(project_number)].matrix
    adapted_coordinates = _coordinates_adaptation(plan, row, col)
    score = 0
    types = []
    manhattan_residence_area = project_list[int(project_number)].get_manhattan_surface(
        int(cityplan.dist_manhattan_max), cityplan.matrix, adapted_coordinates)

    for coordinates in manhattan_residence_area:
        if str(cityplan.matrix[coordinates]) != ".":
            building = project_list[int(replica_list[int(cityplan.matrix[coordinates])][0])]
            if type(building) is Utility.Utility:
                if not (building.type in types):
                    types.append(building.type)
                    score += int(project_list[int(project_number)].capacity)

    return score


def _affichage_score(tested_replica, len_list, score, begin_time, is_residential=True):
    """
     Affichage des informations lors du calcul du score

     :param: tested_replica : Nombre de répliques déjà testées
     :param: len_list : Nombre de répliques déjà testées
     :param: score : Score actuel
     :param: begin_time : Heure du début du calcul du score
     :param: is_residential : Nature du bâtiment (résidentiel ou utilitaire)
     :return: Informations
     :rtype: String

    """
    print(" ------- " + "{0:.2f}".format(tested_replica / len_list * 100) + '%')
    if is_residential:
        print("Residential tested :", tested_replica, "(of " + str(len_list) + ")")
        print("Points per residential :", "{0:.2f}".format(score / tested_replica))
        print("Approximated final score :", "{0:.2f}".format((score / tested_replica) * len_list))
        print("Approximated waiting time: %i s" % (((time.time() - begin_time) *
                                                    1 // (tested_replica / len_list)) - (
                                                           time.time() - begin_time)))
        print("Partial scoring :", score)

    else:
        print("Replica tested :", tested_replica, "(of " + str(len_list) + ")")
