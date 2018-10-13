import numpy as np
from CityPlan import CityPlan
from Building import Building
from Utility import Utility
from Residential import Residential

###### MAIN pour les tests######

#definition de la ville
matriceVille=np.array([['.','.','.'],['#','#','#'],['.','.','.'],['#','#','#'],['.','.','.'],['#','#','#'],['.','.','.'],['.','.','.'],['.','.','.'],['.','.','.']])
c=CityPlan(matriceVille,"Lyon",4)
print(c.matrix)

#definition des batiments
matBuild=np.array([['.','#','#'],['#','#','#'],['#','.','#']])
resi=Residential(matBuild,25)

#print("residential placeable en 0,2 ? ",resi.isPlaceable(c,0,6))
print("\n")
utili=Utility(matBuild,5)
print(utili.matrix)
print("\n")

#ajout d'un utilitaire dans la ville
c.add(utili, 0, 6)
print(c.matrix)
