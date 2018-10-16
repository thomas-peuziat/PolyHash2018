from model.Building import Building


class Utility(Building):

    def __init__(self, id, matrix, id_building, pos_row, pos_column, type):
        super().__init__(id, matrix, id_building, pos_row, pos_column)
        self.type = type
