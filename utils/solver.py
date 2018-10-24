"""SOLVER : Contient un certain nombre de fonctions permettant le remplissage plus ou moins optimisé d'un CityPlan
avec des replica de Project

"""

import random
from model.CityPlan import CityPlan
from utils import parser
from utils import scoring
import os.path


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
            if cityplan.add(project_list[random_idx], random_pos[0], random_pos[1]):
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
            parser.imgify(filename, cityplan, project_list)
            parser.textify(replica_list, filename)

    _print_solution(filename, trials_max, max_score)


def _advanced_random_solver(cityplan: CityPlan, project_list: list, error_max: int):
    if error_max >= 0:
        error = 0
        len_project_list = len(project_list)
        row_max, column_max = cityplan.matrix.shape
        replica_list = []

        print("Advanced random solver for :", cityplan.name_project)
        print("...")
        while error < error_max:
            random_idx = random.randint(0, len_project_list - 1)
            random_pos = (random.randint(0, row_max - 1), random.randint(0, column_max - 1))

            if cityplan.add(project_list[random_idx], random_pos[0], random_pos[1]):
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
        cityplan, replica_list = _advanced_random_solver(cityplan, project_list, error_max)  # Rempli le CityPlan et renvoi une liste de Replica
        score = scoring.scoring_from_replica_list(replica_list, cityplan, project_list)
        trials_count += 1

        if score >= max_score:
            max_score = score
            parser.imgify(filename, cityplan, project_list)
            parser.textify(replica_list, filename)

    _print_solution(filename, trials_max, max_score)


def _print_solver(len_replica_list):
    print("\nReplica count :", len_replica_list, '\n -------------')


def _print_solution(filename, trials_max, max_score):
    print(" ~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~")
    print("Best score for", filename, "with", trials_max, "trials is :", max_score)
    print("You can find the output in polyhash2018/data/output")
    print(" ~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~")
