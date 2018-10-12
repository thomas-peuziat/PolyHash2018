
class CityPlan:

	def __init__(self, matrix, name, dist):
		self.matrix = matrix
		self.nameProject = name
		self.distManhattanMax = dist
		self.nbProjectPlaced = 0
	
	def addTo(self, building, posX, posY):
		if(building.isPlaceable(self, posX, posY)):
			lignes, colonnes = building.matrix.shape

			#on parcourt a partir de la posY definie jusqu'a 
			#la posY+le nombre de lignes du batiments
			for numLignes in range(posY,posY+lignes):
				#on parcourt a partir de la posX definie jusqu'a 
				#la posX+ le nombre de colonnes du batiments
				for numColonnes in range(posX,posX+colonnes):
					#TODO ajouter dans la ville
					self.matrix[numLignes,numColonnes]=building
