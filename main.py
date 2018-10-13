from utils import parser
from utils import solver


filename = "c_going_green"
cityplan, building_dict = parser.parse(filename)

for p in building_dict.values():
    print(p.matrix)
    print("---------------")

cityplan, list_building_placed = solver.random_solver(cityplan, building_dict)
print(list_building_placed)

parser.textify(list_building_placed, filename)
