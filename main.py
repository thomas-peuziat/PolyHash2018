from utils import parser
from utils import solver
from utils import scoring


def random_solver_solution(filename, trials_max, error_max):
    max_score = 0
    trials_count = 0

    while trials_count < trials_max:
        cityplan, project_list = parser.parse(filename)  # Génère un CityPlan vide et une liste de Project
        cityplan, replica_list = solver.random_solver(cityplan, project_list, error_max)  # Rempli le CityPlan et renvoi une liste de Replica
        # score = scoring.scoring_from_output(replica_list, cityplan, project_list)
        score = scoring.scoring_from_replica_list(replica_list, cityplan, project_list)
        trials_count += 1

        if score >= max_score:
            max_score = score
            parser.imgify(filename, cityplan, project_list)
            parser.textify(replica_list, filename)

    print(" ~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~")
    print("Best score for", filename, "with", trials_max, "trials is :", max_score)
    print("You can find the output in polyhash2018/data/output")
    print(" ~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~")


filename = "a_example"
random_solver_solution(filename, 100, 100)
