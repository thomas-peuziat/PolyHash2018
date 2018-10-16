from model.Project import Project


class Utility(Project):

    def __init__(self, id, matrix, type):
        super().__init__(id, matrix)
        self.type = type
