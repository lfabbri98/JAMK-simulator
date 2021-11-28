#This is main file, starting point

#including libraries
from controls import *
from JMAK import *
from data_analysis import *
import os
import configparser
import sys


###############################################################################
#INITIALIZATION OF PARAMETERS
###############################################################################
config = configparser.ConfigParser()
config.read('config.txt')

"""
Description of parameters:
    
    - N : length of the side of the matrix
    
    - dim : dimensionality of the process, can be 2 or 3
    
    - J : number of new nuclei that are generated inside the matrix for each time step
    
    - R : number of new nuclei that are growth in all directions around each nucleus
    
    - name : name of simulation, will be used for outputs
"""
N = config.get('settings','N')
dim = config.get('settings','dimension')
J = config.get('settings','J')
R = config.get('settings','R')
name = config.get('name','simName')

#Controls on input 
try:
    N = int(N)
    dim = int(dim)
    J = int(J)
    R = int(R)
except:
    #error if paramters are not integer
    print("You inserted some non integer parameters.")
    sys.exit()

if not (dim==2 or dim==3):
    #error is dim is different from 2 or 3
    print("Dimensionality should be 2 or 3!")
    sys.exit()

#Creation of general output directory
try:
    os.makedirs("Outputs")
except FileExistsError:
    # directory already exists
    pass

"""
###############################################################################      
#SIMULATION
###############################################################################
matrix = system_creation(init_data)
t = 0 #time counter
domain_coordinates = generate_pos_table(init_data) #table with coordinates of all points
number_domains = 0 #domains counter
table_filled_fraction = np.zeros((init_data[0]**init_data[1],2)) #table with filled fraction in function of time
counter_table = 0 #counter for filling previous table

#Creation of output directory for each simulation
try:
    os.makedirs("Outputs/"+name)
except FileExistsError:
    # directory already exists
    pass


while number_domains/init_data[0]**init_data[1] <= 0.99:
    
    #2D case
    if init_data[1] == 2:
        #this expression avoid to have less free sites than J, otherwise we have a problem!
        if init_data[2] < init_data[0]**init_data[1] - number_domains:
            matrix, domain_coordinates, number_domains = nucleation_2D(matrix, init_data, domain_coordinates, number_domains)
        matrix, domain_coordinates, number_domains = growth_2D(matrix, init_data, domain_coordinates, number_domains)
        
    #3D case
    elif init_data[1] == 3:
        if init_data[2] < init_data[0]**init_data[1] - number_domains:
            matrix, domain_coordinates, number_domains = nucleation_3D(matrix, init_data, domain_coordinates, number_domains)
        matrix, domain_coordinates, number_domains = growth_3D(matrix, init_data, domain_coordinates, number_domains)
        
    t = t+1 #increase time after each step
    table_filled_fraction[counter_table] = [t,number_domains/init_data[0]**init_data[1]] #update filled fraction
    counter_table = counter_table+1
    print("Progression: ",round(number_domains/init_data[0]**init_data[1]*100,2),"%" )

###############################################################################
#DATA ANALYSIS AND PLOT
###############################################################################   
    #this firs plotting expression is inside the while 
    plot_matrix(domain_coordinates, init_data,number_domains/init_data[0]**init_data[1],name)
plot_JMAK(table_filled_fraction,counter_table,init_data,name)
    
    """   
   
    
