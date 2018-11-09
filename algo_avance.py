from utils import solver, parser, scoring
from model import Project, Utility, Residential

all_buildings_scores = []
all_cityplans = []

# Génération d'une population aléatoire
for i in range(0, 1):
    filename = "b_short_walk"
    error_max = 10
    cityplan, project_list = parser.parse(filename)  # Génère un CityPlan vide et une liste de Project
    cityplan, replica_list = solver._advanced_random_solver(cityplan, project_list, error_max)  # Rempli le CityPlan et renvoi une liste de Replica
    score = scoring.scoring_from_replica_list(replica_list, cityplan, project_list)
    all_cityplans.append(cityplan) # Ajout des différents cityplans dans le cas d'une génération avec plusieurs populations


    # Lecture des repliques placées dans la map
    for building in replica_list:
        project_number = int(building[0])
        if type(project_list[project_number]) is Residential.Residential:
            row = building[1][0]
            col = building[1][1]
            building_score = scoring.building_score(cityplan, row, col, project_list, project_number, replica_list) # Calcul des scores de chaque batiments
            all_buildings_scores.append([building_score, (row,col), project_number, i]) # Ajout des scores de chaque batiments

            # TODO: Calcul de la surface occupée
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
                    if type(building) is Utility.Utility:
                        if not (project_number in id_utility_list):
                            id_utility_list.append(project_number)
                            building_coordinates = scoring._coordinates_adaptation(building.matrix, replica_list[project_number][1][0], replica_list[project_number][1][1])
                            for coor in building_coordinates:
                                cases_configuration.append(coor)

            # Calcul de l'espace utilisée par la configuration
            if cases_configuration != []:
                cases_configuration.sort(key=lambda x: (x[0], x[1]))
                print(cases_configuration)
                row_top = int(cases_configuration[0][0])
                row_bottom = int(cases_configuration[len(cases_configuration) - 1][0])

                cases_configuration.sort(key=lambda x: (x[1], x[0]))
                print(cases_configuration)
                col_top = int(cases_configuration[0][1])
                col_bottom = int(cases_configuration[len(cases_configuration) - 1][1])

                taille = [row_bottom - row_top + 1, col_bottom - col_top + 1]
                print(taille)
                taille_reelle = taille[0] * taille[1]
                print(taille_reelle)
                densite = building_score / taille_reelle
                print(densite)

                all_buildings_scores.append([densite, (row, col), project_number, i])  # Ajout des scores de chaque batiments

# Triage des scores par ordre décroissant de la densitées
all_buildings_scores.sort(reverse=True)
print(all_buildings_scores)
buildings_with_points = []

# Suppression des résidences qui rapportent zéro points
for i in range(0, len(all_buildings_scores)):
    if int(all_buildings_scores[i][0]) != 0:
        buildings_with_points.append(all_buildings_scores[i])

print(buildings_with_points)
print(int(0.10*len(buildings_with_points)))

# Sélection des 10% meilleurs batiments par rapport à leur densitées
for builds in range(0, int(0.10*len(buildings_with_points))):
    project_number = builds[2]
    build_row = builds[1][0]
    build_col = builds[1][1]
    plan = project_list[project_number].matrix
    adapted_coordinates = scoring._coordinates_adaptation(plan, build_row, build_col)

    used_surface = project_list[project_number].get_manhattan_surface(int(all_cityplans[int(builds[3])].dist_manhattan_max), all_cityplans[int(builds[3])].matrix,
                                                                      adapted_coordinates)
    new_liste = list(used_surface)
    # new_liste.sort(key=lambda x: (x[0], x[1]))
    # print(new_liste)

    id_utility_list = []
    for cases in new_liste:
        if str(cityplan.matrix[cases]) != ".":
            building = project_list[int(replica_list[int(all_cityplans[int(builds[3])].matrix[cases])][0])]
            if type(building) is Utility.Utility:
                if not (building.type in id_utility_list):
                    id_utility_list.append(building.type)
                    score += int(project_list[int(project_number)].capacity)





print(all_buildings_scores[0][0])
