from Building import Building


class Residential(Building):

    def __init__(self, matrix, capacity):
        super().__init__(matrix)
        self.capacity = capacity
