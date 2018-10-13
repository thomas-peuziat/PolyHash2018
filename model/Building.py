import numpy as np


class Building:

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




