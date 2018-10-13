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


def scoring(path=""):
    with open(path, 'r') as input_file:
        input_file = open(path, 'r')
        buildings_number = input_file.readline()                    #get the number of buidings placed in the city

        lines = input_file.readlines()                              #read the other line from the second
        input_file.close()
        for line in lines:
            project_number = line.split()[0]                        #get the number of the building project
            print("Number project : " + project_number)
            #TODO: créer une méthode bool isResidentialProject(value)
            if int(project_number) == 0: #isResidentialProject(numberProject()):
                ## Get top left coordinates
                x_top = line.split()[1]
                y_top = line.split()[2]
                print("X top : " + x_top)
                print("Y top : " + y_top)

                ##TODO: Récupération du plan du building
                eg_building_plan = [[".", "#"], ["#", "#"], ["#", "#"]]             #example
                list_coordonates =[]
                indexX = 0
                for line in eg_building_plan:
                    indexY = 0
                    for col in line:
                        if col == "#":
                            list_coordonates.append([indexX, indexY])
                        indexY += 1
                    indexX += 1

                print(list_coordonates)

                for cases in list_coordonates:
                    cases[0] += int(x_top)
                    cases[1] += int(y_top)
                print(list_coordonates)

                ##TODO: Calculer la distance de Manhattan la plus courte
                








chemin = "/home/killian/Documents/Polytech/ProjetAlgo/polyhash2018/data/output/test.out"

scoring(chemin)