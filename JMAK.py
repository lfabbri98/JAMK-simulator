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

def growth_2D(matrix, params, positions_nuclei, num_nuclei):
    if is_all_full(matrix,params):
        return [matrix, positions_nuclei, num_nuclei]
    for q in range(0,num_nuclei):
        for w in range(-params[3], params[3]+1):
            for s in range(-params[3], params[3]+1):
                x = positions_nuclei[q,0] + w
                y = positions_nuclei[q,1] + s
                #controls for segmentantion fault
                if x>params[0]:
                    x = abs(params[0]-x)
                if x<0:
                    x = params[0] - abs(1-x)
                if y>params[0]:
                    y = abs(params[0]-y)
                if y<0:
                    y = params[0] - abs(1-y)    
                
                if matrix[int(x)-1,int(y)-1] == 0:
                    matrix[int(x)-1,int(y)-1] = 1
                    positions_nuclei[num_nuclei] = [x,y]
                    num_nuclei = num_nuclei+1
    return [matrix, positions_nuclei, num_nuclei]

def growth_3D(matrix, params, positions_nuclei, num_nuclei):
    if is_all_full(matrix,params):
        return [matrix, positions_nuclei, num_nuclei]
    for q in range(0,num_nuclei):
        for w in range(-params[3], params[3]+1):
            for s in range(-params[3], params[3]+1):
                for t in range(-params[3], params[3]+1):
                    
                    x = positions_nuclei[q,0] + w
                    y = positions_nuclei[q,1] + s
                    z = positions_nuclei[q,2] + t
                #controls for segmentantion fault
                if x>params[0]:
                    x = abs(params[0]-x)
                if x<0:
                    x = params[0] - abs(1-x)
                if y>params[0]:
                    y = abs(params[0]-y)
                if y<0:
                    y = params[0] - abs(1-y)  
                if z>params[0]:
                    z = abs(params[0]-z)
                if z<0:
                    z = params[0] - abs(1-z)  
                
                if matrix[int(x)-1,int(y)-1, int(z)-1] == 0:
                    matrix[int(x)-1,int(y)-1,int(z)-1] = 1
                    positions_nuclei[num_nuclei] = [x,y,z]
                    num_nuclei = num_nuclei+1
    return [matrix, positions_nuclei, num_nuclei]


 
    