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
            print(line)








chemin = "/home/killian/Documents/Polytech/ProjetAlgo/polyhash2018/data/input/a_example.in"

scoring(chemin)