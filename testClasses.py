import numpy as np
from model.CityPlan import CityPlan
from model.Utility import Utility
from model.Residential import Residential

###### MAIN pour les tests######

#definition de la ville
matriceVille = np.array(
    [['.', '.', '.','.','.','.','.','.','.','.'], ['3', '3', '3', '3', '.', '4', '4', '4', '4', '4'], ['.', '.', '.','.','.','.','.','.','.','.'],['.', '.', '.','.','.','.','.','.','.','.'],['.', '.', '.','.','.','.','.','.','.','.'],['.', '.', '.','.','.','.','.','.','.','.'],['.', '.', '.','.','.','.','.','.','.','.'],['.', '.', '.','.','.','.','.','.','.','.'],['.', '.', '.','.','.','.','.','.','.','.'],['.', '.', '.','.','.','.','.','.','.','.']])
c = CityPlan(matriceVille, "Lyon", 4)
#print(c.matrix)

 # definition des batiments
matBuild = np.array([['.', '1', '.'], ['1', '1', '.'], ['1', '.', '1']])
matBuild2 = np.array([['1', '1', '1'], ['1', '1', '1'], ['1', '1', '1']])
resi = Residential(0,matBuild2, 25)

#print("residential placeable en 1,3 ? ",resi.is_placeable(c.matrix,1,3))
#print("residential placeable en 3,1 ? ",resi.is_placeable(c.matrix,3,1))
#print("residential placeable en 1,4 ? ",resi.is_placeable(c.matrix,1,4))
print("ajout residential en 1,3 ",c.add(resi, 4, 2))

print("\n")
matBuild2 = np.array([['.', '2', '.'], ['2', '2', '.'], ['2', '.', '2']])

utili = Utility(0,matBuild2, 5)
#print(utili.matrix)
#print("\n")

#ajout d'un utilitaire dans la ville
#print("ajout utili")
#c.add(utili, 3,1)

# Exemple avec utili
#list_coordinates_full_utili = [(3,2),(4,1),(4,2),(5,1),(5,3)]
#utili.get_manhattan_surface(2, c.matrix, list_coordinates_full_utili)

# Exemple avec resi
list_coordinates_full_resi = [(4, 2), (4, 3), (4, 4), (5, 2), (5, 3), (5, 4), (6, 2), (6, 3), (6, 4)]
resi.get_manhattan_surface(5, c.matrix, list_coordinates_full_resi)
print(c.matrix)

