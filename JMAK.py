import numpy as np
from numpy import random

def nucleation(matrix, N, dim, J, positions_nuclei, num_nuclei = 0, seed = 1):
    """
    
    This function performs a nucleation cycle on the matrix, updating all
    relative parameters such as the number of nuclei and table of positions
    
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
        #generate randomly a position to nucleate in the matrix
        new_position = random.randint(0,N,dim)
        new_position = tuple(new_position) #cast to tuple to do a correct indexing 
        if matrix[new_position] == 1: #if domain is already full, skip it
            continue
        #if position is empty, fill it
        matrix[new_position] = 1
        #add position to nuclei list
        positions_nuclei[num_nuclei] = new_position
        num_cycled = num_cycled+1
        num_nuclei = num_nuclei+1

    return matrix, positions_nuclei, num_nuclei

def growth(matrix,N,dim,R,positions_nuclei, num_nuclei):
    """
    Function that performs growth process of domains depending on growth 
    velocity R

    Parameters
    ----------
    matrix : array of int
        matrix of the system
    N : int
        side length of matrix, used to avoid seg. fault
    dim : int
        dimensionality of the process (2D/3D)
    R : int
        growth velocity represents how many new nuclei are added around a
        selected domain each time step
    positions_nuclei : array of int
        table with positions into matrix of all nuclei
    num_nuclei : int
        number of total present nuclei

    Returns
    -------
    matrix : array of int
        matrix of the system after growth process
    positions_nuclei : array of int
        table with positions of nuclei after growth, new nuclei have been added
    num_nuclei : int
        number of new nuclei after growth

    """
    
    #repeat growth of domain for each nucleus in matrix
    for x in range(0,num_nuclei):
        #select current position of single nucleus to grow around it
        current_position = positions_nuclei[x]
        change_position = current_position
        #repeat the step for all dimensions
        for i in range(0,dim):
            #repeat for each value between -R and R
            for j in range(-R,R+1):
                change_position = np.array(change_position)
                change_position[i] = (current_position[i] + j)%N
                change_position = tuple(change_position)
                #if cell is empty then fill it and add change_position to position_nuclei table
                if matrix[change_position] == 0:
                    matrix[change_position] = 1
                    positions_nuclei[num_nuclei] = change_position
                    num_nuclei = num_nuclei+1
                    
    return matrix, positions_nuclei, num_nuclei

 
    