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


#
# final = 0
# point = 0
# non_point = 0
# for scores in all_buildings_scores:
#     if int(scores[0]) != 0:
#         point += 1
#     else:
#         non_point += 1
#     final += int(scores[0])
# print(point)
# print(non_point)



# 2102670








# ====================================================================== SCORING ===========================================================================


# Scoring
# #
# #
# #
# # Permet de calculer le score d'un output
# #
# #
# #
# #
# # Ce scoring va permettre d'analyser le fichier d'une entrée formatée afin d'en déduire
# # le score de notre implémentation du Google HashCode 2018
#
#
# # [3, 1] ---> ligne 3 colonne 1
# # from itertools import islice
# from model import CityPlan
# from model import Residential
# from model import Utility
# import os.path
# import time
#
#
# def scoring_from_replica_list(replica_list, cityplan, project_list):
#     utility_list = []
#     residential_list = []
#     for replica in replica_list:
#         # print("replica :" + str(replica[0]))
#         project_number = int(replica[0])  # get the number of the building project
#         # print("Number_project :" + str(project_number))
#         ## Get top left coordinates
#         row_top = replica[1][0]
#         col_top = replica[1][1]
#
#         plan = project_list[int(project_number)].matrix
#         adapted_coordinates = _coordinates_adaptation(plan, row_top, col_top)
#         # for coor in adapted_coordinates:
#         #     if int(coor[0]) >= 1000 or int(coor[1]) >= 1000:
#         #         print(adapted_coordinates)
#
#         if type(project_list[project_number]) is Utility.Utility:  # Batiments utilitaire
#             utility_list.append([project_number, row_top, col_top, adapted_coordinates])
#         else:
#             residential_list.append([project_number, row_top, col_top, adapted_coordinates])
#     return _scoring(utility_list, residential_list, cityplan, project_list, replica_list)
#
#
# def scoring_from_output(filename, cityplan, project_list):
#     utilitaires_list, residential_list = _output_parser(filename, project_list)
#     return _scoring(utilitaires_list, residential_list, cityplan, project_list)
#
#
# def _scoring(utilitaires_list, residential_list, cityplan, project_list, replica_list):
#     begin_time = time.time()
#     tested_residential = 0
#     score = 0
#     len_residential_list = len(residential_list)
#
#     print("...Scoring starting...")
#     print("Number of residential replica :", len_residential_list)
#     print("Number of utilities replica :", len(utilitaires_list))
#
#     ## -------------------------------------------------------
#     ## -------------- Méthode non optimisées -----------------
#     ## -------------------------------------------------------
#     # for residence in residential_list:
#     #     if (tested_residential % 100) == 0 and tested_residential != 0:
#     #         print(" ------- " + "{0:.2f}".format(tested_residential/len_residential_list*100) + '%')
#     #         print("Residential tested :", tested_residential, "(of " + str(len_residential_list) + ")")
#     #         print("Partial scoring :", score)
#     #         print("Points per residential :", "{0:.2f}".format(score / tested_residential))
#     #         print("Approximated final score :", "{0:.2f}".format((score / tested_residential) * len_residential_list))
#     #
#     #     all_resid = residence[3]
#     #     number_project = residence[0]
#     #     types = []
#     #     for utilitaires in utilitaires_list:
#     #         all_utils = utilitaires[3]
#     #         util_project = utilitaires[0]
#     #         distance = _distance_manhattan(all_resid, all_utils)
#     #         if distance <= int(cityplan.dist_manhattan_max):
#     #             if not (project_list[int(util_project)].type in types):
#     #                 score += int(project_list[int(number_project)].capacity)
#     #                 types.append(project_list[int(util_project)].type)
#     #     tested_residential += 1
#
#     ## -------------------------------------------------------
#     ## ---------------- Méthode optimisées -------------------
#     ## -------------------------------------------------------
#
#     for residence in residential_list:
#         # print(residence)
#         if (tested_residential % 500) == 0 and tested_residential != 0:
#             print(" ------- " + "{0:.2f}".format(tested_residential / len_residential_list * 100) + '%')
#             print("Residential tested :", tested_residential, "(of " + str(len_residential_list) + ")")
#             print("Partial scoring :", score)
#             print("Points per residential :", "{0:.2f}".format(score / tested_residential))
#             print("Approximated final score :", "{0:.2f}".format((score / tested_residential) * len_residential_list))
#             print("Approximated waiting time: %i s" % (((time.time() - begin_time) *
#                                                           1 // (tested_residential / len_residential_list)) - (
#                                                                      time.time() - begin_time)))
#
#         all_resid = residence[3]
#         number_project = int(residence[0])
#         types = []
#         manhattan_residence_area = project_list[number_project].get_manhattan_surface(
#             int(cityplan.dist_manhattan_max), cityplan.matrix, all_resid)
#         # print(manhattan_residence_area)
#         for coordinates in manhattan_residence_area:
#             if str(cityplan.matrix[coordinates]) != ".":
#                 # print(str(cityplan.matrix[coordinates]))
#                 building = project_list[int(replica_list[int(cityplan.matrix[coordinates])][0])]
#                 if type(building) is Utility.Utility:
#                     if not (building.type in types):
#                         types.append(building.type)
#                         score += int(project_list[number_project].capacity)
#
#         tested_residential += 1
#
#     print(" =-=-=-=-=-= =-=-=-=-=-=")
#     print("Final score :", score)
#     print("--- %s seconds ---" % (time.time() - begin_time))
#     print(" =-=-=-=-=-= =-=-=-=-=-=")
#     return score
#
#
# def _distance_manhattan(tab_resid, tab_utils):
#     min = 999
#     for coor_resid in tab_resid:
#         for coord_util in tab_utils:
#             dist = abs(int(coor_resid[0]) - int(coord_util[0])) + abs(int(coor_resid[1]) - int(coord_util[1]))
#             if dist < min:
#                 min = dist
#
#     return min
#
#
# def _output_parser(filename, project_list):
#     path = os.path.join(os.path.curdir, 'data', 'output', filename + '.out')
#     with open(path, 'r') as input_file:
#         buildings_number = input_file.readline()  # get the number of buildings placed in the city
#
#         lines = input_file.readlines()  # read the other line from the second
#         utils = []
#         resid = []
#
#         for line in lines:
#             project_number = line.split()[0]  # get the number of the building project
#             ## Get top left coordinates
#             row_top = line.split()[1]
#             col_top = line.split()[2]
#
#             ##TODO: Récupération du plan du building
#             plan = project_list[int(project_number)].matrix
#             adapted_coordinates = _coordinates_adaptation(plan, row_top, col_top)
#
#             if type(project_list[int(project_number)]) is Utility.Utility:  # Batiments utilitaire
#                 utils.append([project_number, row_top, col_top, adapted_coordinates])
#             else:
#                 resid.append([project_number, row_top, col_top, adapted_coordinates])
#     return utils, resid
#
#
# def _coordinates_adaptation(buildingPlan, rowTop, colTop):
#     list_coordinates = []
#     indexRow = 0
#     for line in buildingPlan:
#         indexCol = 0
#         for col in line:
#             if col != ".":
#                 list_coordinates.append([indexRow, indexCol])
#             indexCol += 1
#         indexRow += 1
#
#     for cases in list_coordinates:
#         cases[0] += int(rowTop)
#         cases[1] += int(colTop)
#
#     return list_coordinates
#
#
# """
#         Optimisation des cases sur lesquelles il faut réellement calculer la distance de Manhattan
#         Par exemple sur deux batiments sont l'un à coté de l'autre, il est inutile de calculer la distance de Manhattan des deux extrémitées
#
# """
#
# # def coordinates_optimisation(list_residence, list_utilitaire):
# # for resid in residential_list:                                                  # Pour chaque résidence
# #     colTop_resid = resid[2]
# #     rowTop_resid = resid[1]
# #
# #     for util in utilitaires_list:                                                   # Pour chaque utilitaire
# #         colTop_util = util[2]
# #         rowTop_util = util[1]
# #         print(rowTop_resid)
# #         print(rowTop_util)
# #         # print(xTop_util)
# #         # print(yTop_util)
# #
# #         resid_tmp =[]
# #         util_tmp = []
# #         if colTop_resid < colTop_util:                  #Le batiment résidentiel est à gauche batiment utilitaire
# #
# #
# #             ligne_resid = rowTop_resid
# #             ligne_util = rowTop_util
# #             for cases in resid[3]:                                      #Sélection de la tranche gauche du batiment résidentiel
# #                 ligne = cases[0]
# #                 print("ligne : " + str(ligne))
# #                 col = cases[1]
# #                 if int(ligne_resid) == int(ligne):
# #                     max = [ligne, col]
# #                 else:
# #                     print("ligne resid : " + str(ligne_resid))
# #                     resid_tmp.append(max)
# #                     ligne_resid = ligne
# #                     print("ligne resid after : " + str(ligne_resid))
# #             resid_tmp.append(max)
# #
# #             first_tour = True
# #             for cases in util[3]:                                          #Sélection de la tranche droite du batiment utilitaire
# #                 ligne = cases[0]
# #                 print("ligne :" + str(ligne))
# #                 # print("ligne : " + str(ligne))
# #                 col = cases[1]
# #                 if first_tour:
# #                     min = [ligne, col]
# #                     util_tmp.append(min)
# #                     first_tour = False
# #
# #                 if int(ligne_util) != int(ligne):
# #                     # print("ligne resid : " + str(ligne_resid))
# #
# #                     ligne_util = ligne
# #                     min = [ligne, col]
# #                     print("add : " + str(min))
# #                     util_tmp.append(min)
# #                     # print("ligne resid after : " + str(ligne_resid))
# #
# #             print(resid_tmp)
# #             print(util_tmp)
# #
# #         elif colTop_resid > colTop_util:                                    # Le batiment utilitaire est sous le batiment résidentiel
# #
# #             ligne_resid = rowTop_resid
# #             ligne_util = rowTop_util
# #
# #             first_tour = True
# #             for cases in resid[3]:
# #                 ligne = cases[0]
# #                 print("ligne :" + str(ligne))
# #                 # print("ligne : " + str(ligne))
# #                 col = cases[1]
# #                 if first_tour:
# #                     min = [ligne, col]
# #                     resid_tmp.append(min)
# #                     first_tour = False
# #
# #                 if int(ligne_resid) != int(ligne):
# #                     # print("ligne resid : " + str(ligne_resid))
# #
# #                     ligne_resid = ligne
# #                     min = [ligne, col]
# #                     print("add : " + str(min))
# #                     resid_tmp.append(min)
# #                     # print("ligne resid after : " + str(ligne_resid))
# #
# #             for cases in util[3]:
# #                 ligne = cases[0]
# #                 # print("ligne : " + str(ligne))
# #                 col = cases[1]
# #                 if int(ligne_util) == int(ligne):
# #                     max = [ligne, col]
# #                 else:
# #                     # print("ligne resid : " + str(ligne_resid))
# #                     util_tmp.append(max)
# #                     ligne_util = ligne
# #                     # print("ligne resid after : " + str(ligne_resid))
# #             util_tmp.append(max)
# #
# #             print(resid_tmp)
# #             print(util_tmp)
# #
# #         else: # Mêmes coordonnées X, donc on regarde le y
# #                 if rowTop_resid < rowTop_util:                  #Le batiment résidentiel est à gauche batiment utilitaire
# #
# #                     ligne_resid = rowTop_resid
# #                     ligne_util = rowTop_util
# #                     for cases in resid[3]:                                      #Sélection de la tranche gauche du batiment résidentiel
# #                         ligne = cases[0]
# #                         print("ligne : " + str(ligne))
# #                         col = cases[1]
# #                         if int(ligne_resid) == int(ligne):
# #                             max = [ligne, col]
# #                         else:
# #                             print("ligne resid : " + str(ligne_resid))
# #                             resid_tmp.append(max)
# #                             ligne_resid = ligne
# #                             print("ligne resid after : " + str(ligne_resid))
# #                     resid_tmp.append(max)
# #
# #                     first_tour = True
# #                     for cases in util[3]:                                          #Sélection de la tranche droite du batiment utilitaire
# #                         ligne = cases[0]
# #                         print("ligne :" + str(ligne))
# #                         # print("ligne : " + str(ligne))
# #                         col = cases[1]
# #                         if first_tour:
# #                             min = [ligne, col]
# #                             util_tmp.append(min)
# #                             first_tour = False
# #
# #                         if int(ligne_util) != int(ligne):
# #                             # print("ligne resid : " + str(ligne_resid))
# #
# #                             ligne_util = ligne
# #                             min = [ligne, col]
# #                             print("add : " + str(min))
# #                             util_tmp.append(min)
# #                             # print("ligne resid after : " + str(ligne_resid))
# #
# #                     print(resid_tmp)
# #                     print(util_tmp)
# #
# #                 elif rowTop_resid > rowTop_util:                                    # Le batiment utilitaire est sous le batiment résidentiel
# #
# #                     ligne_resid = rowTop_resid
# #                     ligne_util = rowTop_util
# #
# #                     first_tour = True
# #                     for cases in resid[3]:
# #                         ligne = cases[0]
# #                         print("ligne :" + str(ligne))
# #                         # print("ligne : " + str(ligne))
# #                         col = cases[1]
# #                         if first_tour:
# #                             min = [ligne, col]
# #                             resid_tmp.append(min)
# #                             first_tour = False
# #
# #                         if int(ligne_resid) != int(ligne):
# #                             # print("ligne resid : " + str(ligne_resid))
# #
# #                             ligne_resid = ligne
# #                             min = [ligne, col]
# #                             print("add : " + str(min))
# #                             resid_tmp.append(min)
# #                             # print("ligne resid after : " + str(ligne_resid))
# #
# #                     for cases in util[3]:
# #                         ligne = cases[0]
# #                         # print("ligne : " + str(ligne))
# #                         col = cases[1]
# #                         if int(ligne_util) == int(ligne):
# #                             max = [ligne, col]
# #                         else:
# #                             # print("ligne resid : " + str(ligne_resid))
# #                             util_tmp.append(max)
# #                             ligne_util = ligne
# #                             # print("ligne resid after : " + str(ligne_resid))
# #                     util_tmp.append(max)
# #
# #                     print(resid_tmp)
# #                     print(util_tmp)
#
#
# # # Le batiment utilitaire est à droite du batiment résidentiel
#
#
# # chemin = "/home/killian/Documents/Polytech/ProjetAlgo/polyhash2018/data/output/test.out"
# #
# # scoring(chemin)
#
# ##TODO: Regarder le type des utilitaires pour el calcul du score
#
# ##TODO: Optimisation périmètre de recherche
#
# ##TODO: Optimisaion des cases sur lesquelles calculer la distance
#
#
# def building_score(cityplan, row, col, project_list, project_number, replica_list):
#     plan = project_list[int(project_number)].matrix
#     adapted_coordinates = _coordinates_adaptation(plan, row, col)
#     score = 0
#     types = []
#     manhattan_residence_area = project_list[int(project_number)].get_manhattan_surface(
#         int(cityplan.dist_manhattan_max), cityplan.matrix, adapted_coordinates)
#
#     for coordinates in manhattan_residence_area:
#         if str(cityplan.matrix[coordinates]) != ".":
#             building = project_list[int(replica_list[int(cityplan.matrix[coordinates])][0])]
#             if type(building) is Utility.Utility:
#                 if not (building.type in types):
#                     types.append(building.type)
#                     score += int(project_list[int(project_number)].capacity)
#
#     return score


