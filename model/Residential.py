from model.Project import Project


class Residential(Project):

    def __init__(self, id, matrix, capacity):
        super().__init__(id, matrix)
        self.capacity = capacity
