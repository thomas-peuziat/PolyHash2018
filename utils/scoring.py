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

    for resid in residential_list:                                                  # Pour chaque résidence
        rowTop_resid = resid[1]
        colTop_resid = resid[2]

        for util in utilitaires_list:                                                   # Pour chaque utilitaire
            rowTop_util = util[1]
            colTop_util = util[2]
            print(colTop_resid)
            print(colTop_util)
            # print(xTop_util)
            # print(yTop_util)

            resid_tmp =[]
            util_tmp = []
            if colTop_resid < colTop_util:                  #Le batiment résidentiel est sous le batiment utilitaire

                ligne_resid = rowTop_resid
                ligne_util = rowTop_util
                for cases in resid[3]:
                    ligne = cases[0]
                    # print("ligne : " + str(ligne))
                    col = cases[1]
                    if int(ligne_resid) == int(ligne):
                        max = [ligne, col]
                    else:
                        # print("ligne resid : " + str(ligne_resid))
                        resid_tmp.append(max)
                        ligne_resid = ligne
                        # print("ligne resid after : " + str(ligne_resid))
                resid_tmp.append(max)

                first_tour = True
                for cases in util[3]:
                    ligne = cases[0]
                    print("ligne :" + str(ligne))
                    # print("ligne : " + str(ligne))
                    col = cases[1]
                    if first_tour:
                        min = [ligne, col]
                        util_tmp.append(min)
                        first_tour = False

                    if int(ligne_util) == int(ligne):
                        print()
                        # min = [ligne, col]
                        # print("add : " + str(min))
                        # util_tmp.append(min)
                    elif int(ligne_util) != int(ligne):
                        # print("ligne resid : " + str(ligne_resid))

                        ligne_util = ligne
                        min = [ligne, col]
                        print("add : " + str(min))
                        util_tmp.append(min)
                        # print("ligne resid after : " + str(ligne_resid))

                print(resid_tmp)
                print(util_tmp)

            # elif rowTop_resid < rowTop_util:                                    # Le batiment utilitaire est sous le batiment résidentiel
            # else: # Mêmes coordonnées X, donc on regarde le y
            #     if colTop_resid > colTop_util:  # Le batiment résidentiel est à droite du batiment utilitaire
            # #     # ne garder que les coordonnées de la tranche la plus proche
            #     elif colTop_resid < colTop_util: #de
            # # Le batiment utilitaire est à droite du batiment résidentiel

    # for util in lines:
    #     util_number_project = line.split()[0]
    #     if util_number_project == 1 #isUtilitaireProject(util_number_project):                #Batiment utilitaire





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
            x_top = line.split()[1]
            y_top = line.split()[2]
            # print("X top : " + x_top)
            # print("Y top : " + y_top)

            ##TODO: Récupération du plan du building
            eg_building_plan = [[".", "#"], ["#", "#"], ["#", "#"]]             #example
            adapted_coordinates = coordinates_adaptation(eg_building_plan, x_top, y_top)

            if int(project_number) == 0:                                     #Batiments utilitaire
                print("utilitaire ajouté")
                utils.append([project_number, x_top, y_top, adapted_coordinates])
            else:
                print("residentiel ajouté")
                resid.append([project_number, x_top, y_top, adapted_coordinates])
    return utils, resid



def coordinates_adaptation(buildingPlan, xTop, yTop):
    list_coordinates = []
    indexX = 0
    for line in buildingPlan:
        indexY = 0
        for col in line:
            if col == "#":
                list_coordinates.append([indexX, indexY])
            indexY += 1
        indexX += 1

    for cases in list_coordinates:
        cases[0] += int(xTop)
        cases[1] += int(yTop)
    # print(list_coordinates)

    return list_coordinates




chemin = "/home/killian/Documents/Polytech/ProjetAlgo/polyhash2018/data/output/test.out"

scoring(chemin)