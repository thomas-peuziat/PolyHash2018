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

#from itertools import islice


def scoring(path):
    utilitaires_list = []
    residential_list = []

    utilitaires_list, residential_list = outputParser(path)

    print(utilitaires_list)
    print(residential_list)

    ##TODO: Calculer la distance de Manhattan la plus courte

    for resid in residential_list:
        print(resid[0])
    # for util in lines:
    #     util_number_project = line.split()[0]
    #     if util_number_project == 1 #isUtilitaireProject(util_number_project):                #Batiment utilitaire





def outputParser(path):
    with open(path, 'r') as input_file:
        input_file = open(path, 'r')
        buildings_number = input_file.readline()                    #get the number of buidings placed in the city

        lines = input_file.readlines()                              #read the other line from the second
        input_file.close()
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