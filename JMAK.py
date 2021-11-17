import numpy as np
import random 
from controls import *


def nucleation_2D(matrix, params, positions_nuclei, num_nuclei):
    internal_matrix = matrix
    num_cycled=0
    while num_cycled < params[1]:
        new_position_1 = random.randint(0,params[0]-1)
        new_position_2 = random.randint(0,params[0]-1)
        if internal_matrix[new_position_1, new_position_2] == 1:
            if is_all_full(internal_matrix, params):
                break
            continue
        internal_matrix[new_position_1, new_position_2] = 1
        positions_nuclei[num_nuclei] = [new_position_1, new_position_2]
        num_cycled = num_cycled+1
        num_nuclei = num_nuclei+1

    return [internal_matrix, positions_nuclei, num_nuclei]

def nucleation_3D(matrix, params, positions_nuclei, num_nuclei):
    internal_matrix = matrix
    num_cycled=0
    while num_cycled < params[1]:
        new_position_1 = random.randint(0,params[0]-1)
        new_position_2 = random.randint(0,params[0]-1)
        new_position_3 = random.randint(0,params[0]-1)
        if internal_matrix[new_position_1, new_position_2,new_position_3] == 1:
            if is_all_full(internal_matrix, params):
                break
            continue
        internal_matrix[new_position_1, new_position_2, new_position_3] = 1
        positions_nuclei[num_nuclei] = [new_position_1, new_position_2, new_position_3]
        num_cycled = num_cycled+1
        num_nuclei = num_nuclei+1

    return [internal_matrix, positions_nuclei, num_nuclei]

 
    