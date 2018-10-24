"""SOLVER : Contient un certain nombre de fonctions permettant le remplissage plus ou moins optimisé d'un CityPlan
avec des replica de Project

"""

import random
from model.CityPlan import CityPlan
from model.Residential import Residential
from model.Utility import Utility


def random_solver(cityplan: CityPlan, project_list: list, error_max: int):
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

        print("Replica count :", len(replica_list), '\n -------------')
        print("You can check the output in polyhash2018/data/output/" + cityplan.name_project + ".out")
        print(" -------------")

        return cityplan, replica_list


def advanced_random_solver(cityplan: CityPlan, project_list: list, error_max: int, residential_ratio, utilities_ratio):
    if error_max >= 0:
        len_project_list = len(project_list)
        row_max, column_max = cityplan.matrix.shape
        replica_list = []
        current_residential_ratio = residential_ratio
        current_utilities_ratio = utilities_ratio

        print("Advanced random solver for :", cityplan.name_project, "\n -------------")
        while error_max > 0:
            random_idx = random.randint(0, len_project_list - 1)
            random_pos = (random.randint(0, row_max - 1), random.randint(0, column_max - 1))

            if (type(project_list[random_idx]) == Residential) and current_residential_ratio > 0:
                # print("Res:", current_residential_ratio)
                if cityplan.add(project_list[random_idx], random_pos[0], random_pos[1]):
                    project_list[random_idx].list_pos_replica.append((random_pos[0], random_pos[1]))
                    replica = [random_idx, (random_pos[0], random_pos[1])]
                    replica_list.append(replica)
                    current_residential_ratio -= 1
                else:
                    error_max -= 1
            elif (type(project_list[random_idx]) == Utility) and current_utilities_ratio > 0:
                # print("Uti:", current_utilities_ratio)
                if cityplan.add(project_list[random_idx], random_pos[0], random_pos[1]):
                    project_list[random_idx].list_pos_replica.append((random_pos[0], random_pos[1]))
                    replica = [random_idx, (random_pos[0], random_pos[1])]
                    replica_list.append(replica)
                    current_utilities_ratio -= 1
                else:
                    error_max -= 1
            elif current_utilities_ratio == 0 and current_residential_ratio == 0:
                current_utilities_ratio = utilities_ratio
                current_residential_ratio = residential_ratio

        print("Replica count :", len(replica_list), '\n -------------')
        print("You can check the output in polyhash2018/data/output/" + cityplan.name_project + ".out")
        print(" -------------")

        return cityplan, replica_list
