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
		print("\n\n\n")
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
						print(city.matrix[numLignes,numColonnes])
						if(city.matrix[numLignes,numColonnes]=='#'):
							return False
				return True
		except:
			return False
		
		
matriceVille=np.array([['.','.','.'],['#','#','#'],['.','.','.'],['#','#','#'],['.','.','.'],['#','#','#'],['.','.','.'],['.','.','.'],['.','.','.'],['.','.','.']])
c=CityPlan.CityPlan(matriceVille,"Lyon",4)
print(c.matrix)

matBuild=np.array([['.','#','#'],['#','#','#'],['#','.','#']])
b=Building(matBuild)

print(b.isPlaceable(c,0,2))
print(b.matrix)
