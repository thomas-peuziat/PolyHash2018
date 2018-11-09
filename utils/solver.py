"""SOLVER : Contient un certain nombre de fonctions permettant le remplissage plus ou moins optimisé d'un CityPlan
avec des replica de Project

"""

import random
from model.CityPlan import CityPlan
from model.Residential import Residential
from model.Utility import Utility
from utils import parser
from utils import scoring
import os.path
import time


def _random_solver(cityplan: CityPlan, project_list: list, error_max: int):
    if error_max >= 0:
        error = error_max
        len_project_list = len(project_list)
        row_max, column_max = cityplan.matrix.shape
        replica_list = []

        random_idx = random.randint(0, len_project_list - 1)
        random_pos = (random.randint(0, row_max - 1), random.randint(0, column_max - 1))

        print("Random solver for :", cityplan.name_project, "\n -------------")
        while error > 0:
            id_replica = len(replica_list)
            if cityplan.add(project_list[random_idx], random_pos[0], random_pos[1], id_replica):
                error = error_max

                project_list[random_idx].list_pos_replica.append((random_pos[0], random_pos[1]))
                replica = [random_idx, (random_pos[0], random_pos[1])]
                replica_list.append(replica)

                random_idx = random.randint(0, len_project_list - 1)
                random_pos = (random.randint(0, row_max - 1), random.randint(0, column_max - 1))
            else:
                error -= 1
                random_pos = (random.randint(0, row_max - 1), random.randint(0, column_max - 1))

        _print_solver(len(replica_list))

        return cityplan, replica_list


def random_solver_solution(filename, trials_max, error_max):
    max_score = 0
    trials_count = 0
    path_out = os.path.join(os.path.curdir, 'data', 'output')

    while trials_count < trials_max:
        if not os.path.exists(path_out):
            os.makedirs(path_out)
        cityplan, project_list = parser.parse(filename)  # Génère un CityPlan vide et une liste de Project
        cityplan, replica_list = _random_solver(cityplan, project_list, error_max)  # Rempli le CityPlan et renvoi une liste de Replica
        score = scoring.scoring_from_replica_list(replica_list, cityplan, project_list)
        trials_count += 1

        if score >= max_score:
            max_score = score
            parser.imgify(filename, cityplan, project_list, replica_list)
            parser.textify(replica_list, filename)

    _print_solution(filename, trials_max, max_score)


def _advanced_random_solver(cityplan: CityPlan, project_list: list, error_max: int):
    if error_max >= 0:
        error = 0
        len_project_list = len(project_list)
        row_max, column_max = cityplan.matrix.shape
        replica_list = []


        while error < error_max:
            random_idx = random.randint(0, len_project_list - 1)
            random_pos = (random.randint(0, row_max - 1), random.randint(0, column_max - 1))

            id_replica = len(replica_list)
            if cityplan.add(project_list[random_idx], random_pos[0], random_pos[1], id_replica):
                project_list[random_idx].list_pos_replica.append((random_pos[0], random_pos[1]))
                replica = [random_idx, (random_pos[0], random_pos[1])]
                replica_list.append(replica)
            else:
                error += 1

            if not(error % (error_max/10)) and error_max > 100 and error > 0:
                print(". ", end='')

        _print_solver(len(replica_list))

        return cityplan, replica_list


def advanced_random_solver_solution(filename, trials_max, error_max):
    max_score = 0
    trials_count = 0
    path_out = os.path.join(os.path.curdir, 'data', 'output')

    while trials_count < trials_max:
        if not os.path.exists(path_out):
            os.makedirs(path_out)
        cityplan, project_list = parser.parse(filename)  # Génère un CityPlan vide et une liste de Project

        print("Advanced random solver for :", cityplan.name_project)
        print("...")

        cityplan, replica_list = _advanced_random_solver(cityplan, project_list, error_max)  # Rempli le CityPlan et renvoi une liste de Replica
        score = scoring.scoring_from_replica_list(replica_list, cityplan, project_list)
        trials_count += 1

        if score >= max_score:
            max_score = score
            parser.imgify(filename, cityplan, project_list, replica_list)
            parser.textify(replica_list, filename)

    _print_solution(filename, trials_max, max_score)


def _print_solver(len_replica_list):
    print("\nReplica count :", len_replica_list, '\n -------------')


def _print_solution(filename, trials_max, max_score):
    print(" ~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~")
    print("Best score for", filename, "with", trials_max, "trials is :", max_score)
    print("You can find the output in polyhash2018/data/output")
    print(" ~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~")


def elitist_solver_solution(filename, error_max, nb_generation):
    all_buildings_scores = []
    all_cityplans = []

    # Génération d'une population aléatoire
    for i in range(0, nb_generation):
        cityplan, project_list = parser.parse(filename)  # Génère un CityPlan vide et une liste de Project

        print("Elitist solver for :", cityplan.name_project)
        print("...")

        cityplan, replica_list = _advanced_random_solver(cityplan, project_list,
                                                                error_max)  # Rempli le CityPlan et renvoi une liste de Replica

        all_cityplans.append(
            cityplan)  # Ajout des différents cityplans dans le cas d'une génération avec plusieurs populations

        begin_time = time.time()
        tested_replica = 0
        len_replica_list = len(replica_list)
        # score correspond au score total d'une génération
        score_total = 0

        # Lecture des repliques placées dans la map
        for building in replica_list:
            project_number = int(building[0])
            if type(project_list[project_number]) is Residential:
                if (tested_replica % 500) == 0 and tested_replica != 0:
                    scoring._affichage_score(tested_replica, len_replica_list, score_total, begin_time, False)

                row = building[1][0]
                col = building[1][1]
                building_score = scoring.building_score(cityplan, row, col, project_list, project_number,
                                                        replica_list)  # Calcul des scores de chaque batiments
                score_total += building_score

                all_buildings_scores.append(
                    [building_score, (row, col), project_number, i])  # Ajout des scores de chaque batiments

                plan = project_list[project_number].matrix
                adapted_coordinates = scoring._coordinates_adaptation(plan, row, col)

                used_surface = project_list[project_number].get_manhattan_surface(
                    int(cityplan.dist_manhattan_max), cityplan.matrix,
                    adapted_coordinates)
                new_liste = list(used_surface)
                # new_liste.sort(key=lambda x: (x[0], x[1]))
                # print(new_liste)

                # Récupération de toutes les cases remplies pour notre configuration
                id_utility_list = []
                cases_configuration = []
                for cases in new_liste:
                    if str(cityplan.matrix[cases]) != ".":
                        building = project_list[int(replica_list[project_number][0])]
                        if type(building) is Utility:
                            if not (project_number in id_utility_list):
                                id_utility_list.append(project_number)
                                building_coordinates = scoring._coordinates_adaptation(building.matrix,
                                                                                       replica_list[project_number][1][
                                                                                           0],
                                                                                       replica_list[project_number][1][
                                                                                           1])
                                for coor in building_coordinates:
                                    cases_configuration.append(coor)

                # Calcul de l'espace utilisée par la configuration
                if cases_configuration != []:
                    cases_configuration.sort(key=lambda x: (x[0], x[1]))
                    row_top = int(cases_configuration[0][0])
                    row_bottom = int(cases_configuration[len(cases_configuration) - 1][0])

                    cases_configuration.sort(key=lambda x: (x[1], x[0]))
                    col_top = int(cases_configuration[0][1])
                    col_bottom = int(cases_configuration[len(cases_configuration) - 1][1])

                    taille = [row_bottom - row_top + 1, col_bottom - col_top + 1]
                    taille_reelle = taille[0] * taille[1]
                    densite = building_score / taille_reelle

                    all_buildings_scores.append(
                        [densite, (row, col), project_number, i])  # Ajout des scores de chaque batiments
            tested_replica += 1

        print(" =-=-=-=-=-= =-=-=-=-=-=")
        print("Total score Generation 1 ???????????????? :", score_total)
        print("--- %s seconds ---" % (time.time() - begin_time))
        print(" =-=-=-=-=-= =-=-=-=-=-=")



        # Triage des scores par ordre décroissant de la densitées
    all_buildings_scores.sort(reverse=True)
    buildings_with_points = []

    # Suppression des résidences qui rapportent zéro points
    for i in range(0, len(all_buildings_scores)):
        if int(all_buildings_scores[i][0]) != 0:
            buildings_with_points.append(all_buildings_scores[i])


    print(all_buildings_scores[0][0])