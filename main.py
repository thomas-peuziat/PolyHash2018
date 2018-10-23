from utils import parser
from utils import solver
from utils import scoring


def random_solver_solution(filename, trials_max, error_max):
    old_score = 0
    trials_count = 0

    cityplan_vide, project_list = parser.parse(filename)  # Génère un CityPlan vide et une liste de Project

    while trials_count < trials_max:
        cityplan = None
        replica_list = None

        cityplan, replica_list = solver.random_solver(cityplan_vide, project_list, error_max)  # Rempli le CityPlan et renvoi une liste de Replica
        score = scoring.scoring_from_replica_list(replica_list, cityplan, project_list)
        trials_count += 1

        if score > old_score:
            old_score = score
            parser.imgify(cityplan, project_list, replica_list, filename)
            parser.textify(replica_list, filename)

    print(" ~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~")
    print("Best score for", filename, "with", trials_max, "trials is :", old_score)
    print("You can find the output in polyhash2018/data/output")
    print(" ~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~")


filename = "e_precise_fit"

random_solver_solution(filename, 1, 7)
