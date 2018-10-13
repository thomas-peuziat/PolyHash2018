from model.Building import Building


class Utility(Building):

    def __init__(self, matrix, type):
        super().__init__(matrix)
        self.type = type
