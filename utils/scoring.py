# Scoring
#
#
#
# Permet de calculer le score d'un output
#
#
#
#
# Ce scoring va permettre d'analyser le fichier d'une entrée formatée afin d'endéduire
# le score de notre implémentation du Google HashCode 2018


# [3, 1] ---> ligne 3 colonne 1
# from itertools import islice
from model import CityPlan
from model import Residential
from model import Utility
import os.path


def scoring_from_replica_list(replica_list, cityplan, project_list):
    utilitaires_list = []
    residential_list = []
    for replica in replica_list:
        project_number = replica[0]  # get the number of the building project
        ## Get top left coordinates
        row_top = replica[1][0]
        col_top = replica[1][1]

        plan = project_list[int(project_number)].matrix
        adapted_coordinates = _coordinates_adaptation(plan, row_top, col_top)

        if type(project_list[int(project_number)]) is Utility.Utility:  # Batiments utilitaire
            utilitaires_list.append([project_number, row_top, col_top, adapted_coordinates])
        else:
            residential_list.append([project_number, row_top, col_top, adapted_coordinates])
    return _scoring(utilitaires_list, residential_list, cityplan, project_list)


def scoring_from_output(filename, cityplan, project_list):
    utilitaires_list, residential_list = _output_parser(filename, project_list)
    return _scoring(utilitaires_list, residential_list, cityplan, project_list)


def _scoring(utilitaires_list, residential_list, cityplan, project_list):
    tested_residential = 0
    score = 0
    len_residential_list = len(residential_list)

    print("...Scoring starting...")
    print("Number of residential replica :", len_residential_list)
    print("Number of utilities replica :", len(utilitaires_list))

    for residence in residential_list:
        if (tested_residential % 100) == 0 and tested_residential != 0:
            print(" ------- " + "{0:.2f}".format(tested_residential/len_residential_list*100) + '%')
            print("Residential tested :", tested_residential, "(of " + str(len_residential_list) + ")")
            print("Partial scoring :", score)
            print("Points per residential :", "{0:.2f}".format(score / tested_residential))
            print("Approximated final score :", "{0:.2f}".format((score / tested_residential) * len_residential_list))

        all_resid = residence[3]
        number_project = residence[0]
        types = []
        for utilitaires in utilitaires_list:
            all_utils = utilitaires[3]
            util_project = utilitaires[0]
            distance = _distance_manhattan(all_resid, all_utils)
            if distance <= int(cityplan.dist_manhattan_max):
                if not (project_list[int(util_project)].type in types):
                    score += int(project_list[int(number_project)].capacity)
                    types.append(project_list[int(util_project)].type)
        tested_residential += 1

    print(" =-=-=-=-=-= =-=-=-=-=-=")
    print("Final score :", score)
    print(" =-=-=-=-=-= =-=-=-=-=-=")
    return score


def _distance_manhattan(tab_resid, tab_utils):
    min = 999
    for coor_resid in tab_resid:
        for coord_util in tab_utils:
            dist = abs(int(coor_resid[0]) - int(coord_util[0])) + abs(int(coor_resid[1]) - int(coord_util[1]))
            if dist < min:
                min = dist

    return min


def _output_parser(filename, project_list):
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

            ##TODO: Récupération du plan du building
            plan = project_list[int(project_number)].matrix
            adapted_coordinates = _coordinates_adaptation(plan, row_top, col_top)

            if type(project_list[int(project_number)]) is Utility.Utility:  # Batiments utilitaire
                utils.append([project_number, row_top, col_top, adapted_coordinates])
            else:
                resid.append([project_number, row_top, col_top, adapted_coordinates])
    return utils, resid


def _coordinates_adaptation(buildingPlan, rowTop, colTop):
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

# def coordinates_optimisation(list_residence, list_utilitaire):
# for resid in residential_list:                                                  # Pour chaque résidence
#     colTop_resid = resid[2]
#     rowTop_resid = resid[1]
#
#     for util in utilitaires_list:                                                   # Pour chaque utilitaire
#         colTop_util = util[2]
#         rowTop_util = util[1]
#         print(rowTop_resid)
#         print(rowTop_util)
#         # print(xTop_util)
#         # print(yTop_util)
#
#         resid_tmp =[]
#         util_tmp = []
#         if colTop_resid < colTop_util:                  #Le batiment résidentiel est à gauche batiment utilitaire
#
#
#             ligne_resid = rowTop_resid
#             ligne_util = rowTop_util
#             for cases in resid[3]:                                      #Sélection de la tranche gauche du batiment résidentiel
#                 ligne = cases[0]
#                 print("ligne : " + str(ligne))
#                 col = cases[1]
#                 if int(ligne_resid) == int(ligne):
#                     max = [ligne, col]
#                 else:
#                     print("ligne resid : " + str(ligne_resid))
#                     resid_tmp.append(max)
#                     ligne_resid = ligne
#                     print("ligne resid after : " + str(ligne_resid))
#             resid_tmp.append(max)
#
#             first_tour = True
#             for cases in util[3]:                                          #Sélection de la tranche droite du batiment utilitaire
#                 ligne = cases[0]
#                 print("ligne :" + str(ligne))
#                 # print("ligne : " + str(ligne))
#                 col = cases[1]
#                 if first_tour:
#                     min = [ligne, col]
#                     util_tmp.append(min)
#                     first_tour = False
#
#                 if int(ligne_util) != int(ligne):
#                     # print("ligne resid : " + str(ligne_resid))
#
#                     ligne_util = ligne
#                     min = [ligne, col]
#                     print("add : " + str(min))
#                     util_tmp.append(min)
#                     # print("ligne resid after : " + str(ligne_resid))
#
#             print(resid_tmp)
#             print(util_tmp)
#
#         elif colTop_resid > colTop_util:                                    # Le batiment utilitaire est sous le batiment résidentiel
#
#             ligne_resid = rowTop_resid
#             ligne_util = rowTop_util
#
#             first_tour = True
#             for cases in resid[3]:
#                 ligne = cases[0]
#                 print("ligne :" + str(ligne))
#                 # print("ligne : " + str(ligne))
#                 col = cases[1]
#                 if first_tour:
#                     min = [ligne, col]
#                     resid_tmp.append(min)
#                     first_tour = False
#
#                 if int(ligne_resid) != int(ligne):
#                     # print("ligne resid : " + str(ligne_resid))
#
#                     ligne_resid = ligne
#                     min = [ligne, col]
#                     print("add : " + str(min))
#                     resid_tmp.append(min)
#                     # print("ligne resid after : " + str(ligne_resid))
#
#             for cases in util[3]:
#                 ligne = cases[0]
#                 # print("ligne : " + str(ligne))
#                 col = cases[1]
#                 if int(ligne_util) == int(ligne):
#                     max = [ligne, col]
#                 else:
#                     # print("ligne resid : " + str(ligne_resid))
#                     util_tmp.append(max)
#                     ligne_util = ligne
#                     # print("ligne resid after : " + str(ligne_resid))
#             util_tmp.append(max)
#
#             print(resid_tmp)
#             print(util_tmp)
#
#         else: # Mêmes coordonnées X, donc on regarde le y
#                 if rowTop_resid < rowTop_util:                  #Le batiment résidentiel est à gauche batiment utilitaire
#
#                     ligne_resid = rowTop_resid
#                     ligne_util = rowTop_util
#                     for cases in resid[3]:                                      #Sélection de la tranche gauche du batiment résidentiel
#                         ligne = cases[0]
#                         print("ligne : " + str(ligne))
#                         col = cases[1]
#                         if int(ligne_resid) == int(ligne):
#                             max = [ligne, col]
#                         else:
#                             print("ligne resid : " + str(ligne_resid))
#                             resid_tmp.append(max)
#                             ligne_resid = ligne
#                             print("ligne resid after : " + str(ligne_resid))
#                     resid_tmp.append(max)
#
#                     first_tour = True
#                     for cases in util[3]:                                          #Sélection de la tranche droite du batiment utilitaire
#                         ligne = cases[0]
#                         print("ligne :" + str(ligne))
#                         # print("ligne : " + str(ligne))
#                         col = cases[1]
#                         if first_tour:
#                             min = [ligne, col]
#                             util_tmp.append(min)
#                             first_tour = False
#
#                         if int(ligne_util) != int(ligne):
#                             # print("ligne resid : " + str(ligne_resid))
#
#                             ligne_util = ligne
#                             min = [ligne, col]
#                             print("add : " + str(min))
#                             util_tmp.append(min)
#                             # print("ligne resid after : " + str(ligne_resid))
#
#                     print(resid_tmp)
#                     print(util_tmp)
#
#                 elif rowTop_resid > rowTop_util:                                    # Le batiment utilitaire est sous le batiment résidentiel
#
#                     ligne_resid = rowTop_resid
#                     ligne_util = rowTop_util
#
#                     first_tour = True
#                     for cases in resid[3]:
#                         ligne = cases[0]
#                         print("ligne :" + str(ligne))
#                         # print("ligne : " + str(ligne))
#                         col = cases[1]
#                         if first_tour:
#                             min = [ligne, col]
#                             resid_tmp.append(min)
#                             first_tour = False
#
#                         if int(ligne_resid) != int(ligne):
#                             # print("ligne resid : " + str(ligne_resid))
#
#                             ligne_resid = ligne
#                             min = [ligne, col]
#                             print("add : " + str(min))
#                             resid_tmp.append(min)
#                             # print("ligne resid after : " + str(ligne_resid))
#
#                     for cases in util[3]:
#                         ligne = cases[0]
#                         # print("ligne : " + str(ligne))
#                         col = cases[1]
#                         if int(ligne_util) == int(ligne):
#                             max = [ligne, col]
#                         else:
#                             # print("ligne resid : " + str(ligne_resid))
#                             util_tmp.append(max)
#                             ligne_util = ligne
#                             # print("ligne resid after : " + str(ligne_resid))
#                     util_tmp.append(max)
#
#                     print(resid_tmp)
#                     print(util_tmp)


# # Le batiment utilitaire est à droite du batiment résidentiel


# chemin = "/home/killian/Documents/Polytech/ProjetAlgo/polyhash2018/data/output/test.out"
#
# scoring(chemin)

##TODO: Regarder le type des utilitaires pour el calcul du score

##TODO: Optimisation périmètre de recherche

##TODO: Optimisaion des cases sur lesquelles calculer la distance
