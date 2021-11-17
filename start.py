"""This is the function that initializes all the parameters for simulation
as well as the type of simulation
"""
from controls import *
import numpy as np

"""Initialization of simulation, requestion of parameters from user"""

def init_simulation():
    N=0
    n=0
    J=0
    R=0
    while True:
        print("Please provide following parameters: N, n, J, R")
        print("Choose only n=2 or n=3")
        N= input("N: ")    
        n=input("n: ")
        J=input("J: ")
        R=input("R: ")
        if not input_control([N,n,J,R]):
            break
    return [N,n,J,R]

    
"""Function that creates the matrix depending on input paramter n"""
def system_creation(params):
    
   N = params[0]
   
   if params[1] == 2:
       matrix = np.zeros((N,N))
   if params[1] == 3:
       matrix = np.zeros((N,N,N))
   
   return matrix 


"""Generates the table to store all positions about nuclei"""
def generate_pos_table(params):
    table = np.zeros((params[0]**params[1],params[1]))
    return table
        