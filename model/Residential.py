from model.Building import Building


class Residential(Building):

    def __init__(self, id, matrix, id_building, pos_row, pos_column, capacity):
        super().__init__(id, matrix, id_building, pos_row, pos_column)
        self.capacity = capacity
