"""Classe Residential, spécialisation de la classe Project"""
from model.Project import Project


class Residential(Project):

    def __init__(self, id, matrix, capacity):
        """
        Constructeur de la classe Residential

         :param: id: correspond à l'id du projet
         :param: matrix: correspond à la matrice du projet
         :param: capacity: correspond au nombre de résident que peut accueillir la Résidence
        """
        super().__init__(id, matrix)
        self.capacity = capacity
