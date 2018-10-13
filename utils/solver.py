import random
from model.CityPlan import CityPlan


def random_solver(cityplan: CityPlan, building_dict: dict):
    error_max = 100
    len_building_dict = len(building_dict)
    list_building = list(building_dict.values())
    row_max, column_max = cityplan.matrix.shape
    list_placed_building = []

    while error_max > 0:
        random_idx = random.randint(0, len_building_dict-1)
        random_row = random.randint(0, row_max-1)
        random_column = random.randint(0, column_max-1)
        if cityplan.add(list_building[random_idx], random_row, random_column):
            list_building[random_idx].row = random_row
            list_building[random_idx].column = random_column
            list_building[random_idx].placed = True
            for key in building_dict:
                if building_dict[key] == list_building[random_idx]:
                    id_project = int(key.split('.')[4])
                    building = [id_project, [list_building[random_idx].row, list_building[random_idx].column]]
                    list_placed_building.append(building)
        else:
            error_max -= 1

    print("Random solver for :", cityplan.nameProject)
    print(cityplan.matrix)
    return cityplan, list_placed_building

