import numpy as np
import CityPlan

class Building():
	
	def __init__(self, matrix):
		self.posX=None
		self.posY=None
		self.matrix = matrix
		self.placed=False
		
	#acces aux valeurs de la matrice la ligne puis la colonne
	#X=colonne / Y = ligne
	def isPlaceable(self, city, posX, posY):
		try:
			if(city.matrix[posY,posX]=='#'):
				return False
			else:
				lignes, colonnes = self.matrix.shape
			
				#on parcourt a partir de la posY definie jusqu'a 
				#la posY+le nombre de lignes du batiments
				for numLignes in range(posY,posY+lignes):
					#on parcourt a partir de la posX definie jusqu'a 
					#la posX+ le nombre de colonnes du batiments
					for numColonnes in range(posX,posX+colonnes):
						if(city.matrix[numLignes,numColonnes]=='#'):
							return False
				return True
		except:
			return False

#fin classe Building

class Residential(Building):

	def __init__(self, matrix, capacity):
		Building.__init__(self, matrix)
		self.capacity = capacity

"""Exemple de methode de la sous classe
	def afficherMatrix(self):
		print(self.matrix)		
"""
#fin classe Residential

class Utility(Building):
	
	def __init__(self, matrix, Type):
		Building.__init__(self, matrix)
		self.Type = Type


#fin classe Utility


###### MAIN pour les tests######

#definition de la ville
matriceVille=np.array([['.','.','.'],['#','#','#'],['.','.','.'],['#','#','#'],['.','.','.'],['#','#','#'],['.','.','.'],['.','.','.'],['.','.','.'],['.','.','.']])
c=CityPlan.CityPlan(matriceVille,"Lyon",4)
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
c.add(utili, 0, 2)
print(c.matrix)
