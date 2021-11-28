import numpy as np
from numpy import random

def nucleation(matrix, N, dim, J, seed, positions_nuclei, num_nuclei):
    """

    Parameters
    ----------
    matrix : array of int
        matrix of the system
    N : int
        side length of matrix
    dim : int
        dimensionality of the process
    J : int
        nucleation rate, how many new nuclei are generated in the matrix at each
        time step
    seed : int
        seed for random number generation
    positions_nuclei : array of int
        stores the positions of all nucleated domains
    num_nuclei : int
        number of total nuclei in the matrix

    Returns
    -------
    matrix : array of int
        matrix of the system after nucleation process
    positions_nuclei : array of int
       stores the positions of all nucleated domains with in addition the new
       nucleated ones
    num_nuclei : int
        number of total nuclei in the matrix after nucleation

    """
    random.seed(seed)
    num_cycled=0
    while num_cycled < J:
        new_position = random.randint(0,N,dim)
        if matrix[tuple(new_position)] == 1: 
            continue
        matrix[tuple(new_position)] = 1
        positions_nuclei[num_nuclei] = new_position
        num_cycled = num_cycled+1
        num_nuclei = num_nuclei+1

    return matrix, positions_nuclei, num_nuclei

"""
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
    return matrix, positions_nuclei, num_nuclei

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
    return matrix, positions_nuclei, num_nuclei
"""

 
    