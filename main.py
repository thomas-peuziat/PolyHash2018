from utils import parser
from utils import solver


filename = "f_different_footprints"
cityplan, building_dict = parser.parse(filename)

cityplan, list_building_placed = solver.random_solver(cityplan, building_dict, 1000000)

parser.textify(list_building_placed, filename)

# Se place dans data/output/
parser.imgify(cityplan, list_building_placed, filename)