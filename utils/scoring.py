#Scoring
#
#
#
#Permet de calculer le score d'un output
#
#
#
#
# Ce scoring va permettre d'analyser le fichier d'une entrée formatée afin d'endéduire
# le score de notre implémentation du Google HashCode 2018



# [3, 1] ---> ligne 3 colonne 1
#from itertools import islice


def scoring(path):
    utilitaires_list = []
    residential_list = []

    utilitaires_list, residential_list = outputParser(path)

    print(utilitaires_list)
    print(residential_list)

    ##TODO: Calculer la distance de Manhattan la plus courte

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

    all_resid = []
    all_utils = []
    for residence in residential_list:
        all_resid = residence[3]
        for utilitaires in utilitaires_list:
            all_utils = utilitaires[3]

            distance = distance_manhattan(all_resid, all_utils)
            print("distance = " + str(distance) + " resid :" + str(all_resid) + " utils :" + str(all_utils))

    print(all_resid)
    print(all_utils)




def distance_manhattan(tab_resid, tab_utils):
    min = 999
    for coor_resid in tab_resid:
        for coord_util in tab_utils:
            dist = abs(int(coor_resid[0]) - int(coord_util[0])) + abs(int(coor_resid[1]) - int(coord_util[1]))
            if dist < min:
                min = dist


    return min



def outputParser(path):
    with open(path, 'r') as input_file:
        input_file = open(path, 'r')
        buildings_number = input_file.readline()                    #get the number of buildings placed in the city

        lines = input_file.readlines()                              #read the other line from the second
        utils = []
        resid = []

        for line in lines:
            project_number = line.split()[0]                        #get the number of the building project
            ## Get top left coordinates
            row_top = line.split()[1]
            col_top = line.split()[2]
            # print("X top : " + x_top)
            # print("Y top : " + y_top)

            ##TODO: Récupération du plan du building
            eg_building_plan = [[".", "#"], ["#", "#"], ["#", "#"]]             #example
            adapted_coordinates = coordinates_adaptation(eg_building_plan, row_top, col_top)

            if int(project_number) == 0:                                     #Batiments utilitaire
                print("utilitaire ajouté")
                utils.append([project_number, row_top, col_top, adapted_coordinates])
            else:
                print("residentiel ajouté")
                resid.append([project_number, row_top, col_top, adapted_coordinates])
    return utils, resid



def coordinates_adaptation(buildingPlan, rowTop, colTop):
    list_coordinates = []
    indexRow = 0
    for line in buildingPlan:
        indexCol = 0
        for col in line:
            if col == "#":
                list_coordinates.append([indexRow, indexCol])
            indexCol += 1
        indexRow += 1

    for cases in list_coordinates:
        cases[0] += int(rowTop)
        cases[1] += int(colTop)
    # print(list_coordinates)

    return list_coordinates




chemin = "/home/killian/Documents/Polytech/ProjetAlgo/polyhash2018/data/output/test.out"

scoring(chemin)