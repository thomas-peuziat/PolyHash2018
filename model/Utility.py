"""Classe Utility, spécialisation de la classe Project"""
from model.Project import Project


class Utility(Project):

    def __init__(self, id, matrix, type):
        """
        Constructeur de la classe Utility

         :param: id: correspond à l'id du projet
         :param: matrix: correspond à la matrice du projet
         :param: type: correspond au type (ou numéro) du projet utilitaire
         """
        super().__init__(id, matrix)
        self.type = type
