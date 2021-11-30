import numpy as np
import sys
import os
import configparser
  
def system_creation(side_length,dim):
    """  
    Parameters
    ----------
    side_length : int
        lenght of matrix side that will be created, has name N in main
    dim : int
        dimensionality of system (2D or 3D)

    Returns
    -------
    matrix : matrix of int with all positions empty (=0)

    """
   
    if dim == 2:
       matrix = np.zeros((side_length,side_length), dtype = int)
    if dim == 3:
       matrix = np.zeros((side_length,side_length,side_length), dtype = int)
   
    return matrix 


def generate_pos_table(side_length, dimension):
    """

    Parameters
    ----------
    side_length : int
        length of matrix side, used because there will be maximum side_lenght^dim nuclei
    dimension : int
        dimension of the process (dim in main)

    Returns
    -------
    table : matrix of int
        matrix where coordinates of nuclei in matrix will be stored

    """
    table = np.zeros((side_length**dimension,dimension), dtype = int)
    return table

def import_parameters():
    """
    Function that initialize parameters of simulation using library configparser.
    Parameters are taken from file config.txt and controls on input type are 
    then performed

    Returns
    -------
    N : int
       side length of the matrix
    dim : int
        dimensionality of the process, can be only 2 or 3
    J : int
        nucleation rate -> how many nuclei are generated in the matrix for each time instant
    R : int
        growth velocity -> how many new nuclei are created around a selected
        nucleus for each time instant
    seed : int
        custom seed for random numbers generator
    name : str
        name of simulation, it will be used to name store folder

    """

    #call configparser to import parameters from file config.txt
    config = configparser.ConfigParser()
    config.read('config.txt')
    
    #get variables from file
    N = config.get('settings','SideLength')
    dim = config.get('settings','Dimension')
    J = config.get('settings','NucleationRate')
    R = config.get('settings','GrowthVelocity')
    seed = config.get('generator','Seed')
    name = config.get('name','SimulationName')

    #Controls on input 
    try:
        N = int(N)
        dim = int(dim)
        J = int(J)
        R = int(R)
        seed = int(seed)
    except ValueError:
        #error if paramters are not integer
        print("You inserted some non integer parameters. Please modify configuration file.")
        sys.exit()

    if not (dim==2 or dim==3):
        #error is dim is different from 2 or 3
        print("Dimensionality should be 2 or 3! Please modify configuration file.")
        sys.exit()
        
    return N,dim,J,R,seed,name