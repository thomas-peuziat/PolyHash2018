"""SOLVER : Contient un certain nombre de fonctions permettant le remplissage plus ou moins optimisé d'un CityPlan
avec des replica de Project

"""

import random
from model.CityPlan import CityPlan


def random_solver(cityplan: CityPlan, project_list: list, error_max: int):
    if error_max >= 0:
        error = error_max
        len_project_list = len(project_list)
        row_max, column_max = cityplan.matrix.shape
        replica_list = []

        random_idx = random.randint(0, len_project_list - 1)
        random_pos = (random.randint(0, row_max - 1), random.randint(0, column_max - 1))
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

        print("Random solver for :", cityplan.name_project, "\n -------------")
        print("Replica count :", len(replica_list), '\n -------------')
        print("You can check the output in polyhash2018/data/output/" + cityplan.name_project + ".out")

        print(" -------------")

        return cityplan, replica_list
