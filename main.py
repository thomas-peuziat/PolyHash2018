from utils import parser
from utils import solver


filename = "c_going_green"
cityplan, project_list = parser.parse(filename)

cityplan, replica_list = solver.random_solver(cityplan, project_list, 100)

parser.textify(replica_list, filename)

# Se place dans data/output/
parser.imgify(cityplan, replica_list, filename)