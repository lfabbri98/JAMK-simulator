import numpy as np
  
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
        