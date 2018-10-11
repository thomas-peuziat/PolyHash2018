# PARSER
# ------
#
# Passerelle entre les fichiers de donnees (dans polyhash/data/) et le reste du programme.
#
# Le parser peut traiter des fichiers formatés en entrée et va fournir des fichiers formatés en
# sorti, voir https://hashcode.withgoogle.com/2018/tasks/hashcode2018_final_task.pdf categorie "Input data set"
# et "Submissions"
#

#TODO : More description

#from os import getcwd

def parse(path=""):
    with open(path, 'r') as input_file:
        input_file = open(path, 'r')

        grid_string = input_file.readline()         # Ex: "4 7 2 3\n"
        grid = grid_string.splitlines()[0].split()  # ['4', '7', '2', '3']
        for i in range(len(grid)):                  # [4, 7, 2, 3]
            grid[i] = int(grid[i])

        #TODO : grid -> PlanVille

        building_project_list = []
        while 'le fichier contient des lignes non analysees':
            building_description_string = input_file.readline()                         # "R 3 2 25\n"

            if building_description_string == '':   # Verifie si on est arrive en fin de ligne
                break

            building_description = building_description_string.splitlines()[0].split()  # ['R', '3', '2', '25']
            for i in range(len(building_description)-1, 0, -1):                         # ['R', 3, 2, 25]
                building_description[i] = int(building_description[i])

            building_plan_string = []
            building_plan = []
            for i in range(building_description[1]):
                building_plan_string.append(input_file.readline())                      # ['.#\n', '##\n', '.#\n']
                building_plan.append(list(building_plan_string[i].splitlines()[0]))     # [['.', '#'], ['#', '#'], ['.', '#']]

            building_project = []
            building_project.append(building_description)
            building_project.append(building_plan)
            building_project_list.append(building_project)

        #TODO : building_project_list -> dict(Building)
    print(grid)
    print(building_project_list)
    return grid, building_project_list

#TODO : relative path
#chemin = getcwd() #+ "/data/input/a_example.in"


chemin = "/home/thomas/PolyHash2018/polyhash2018/data/input/a_example.in"

parse(chemin)