#including libraries
import JMAK
import os
import configparser
import sys
import start
import numpy as np
import data_analysis as dt


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
    
    - seed : seed which will be used to initialize random number generation seed
"""
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
except:
    #error if paramters are not integer
    print("You inserted some non integer parameters. Please modify configuration file.")
    sys.exit()

if not (dim==2 or dim==3):
    #error is dim is different from 2 or 3
    print("Dimensionality should be 2 or 3! Please modify configuration file.")
    sys.exit()

#Creation of general output directory
try:
    os.makedirs("Outputs")
except FileExistsError:
    # directory already exists
    pass


###############################################################################      
#INITIALIZATION OF SYSTEM 
###############################################################################
matrix = start.system_creation(N,dim)
t = 0 #time counter
domain_coordinates = start.generate_pos_table(N,dim) #table with coordinates of all points
number_domains = 0 #domains counter
table_filled_fraction = np.zeros((N**dim,2)) #table with filled fraction in function of time
counter_table = 0 #counter for filling previous table
filled_fraction=0

#Creation of output directory for each simulation name
try:
    os.makedirs("Outputs/"+name)
except FileExistsError:
    # directory already exists
    pass

###############################################################################      
#NUCLEATION AND GROWTH
###############################################################################

while filled_fraction <= 0.99:
    if matrix.all()==1:
        break
    if J < N**dim - J: #this expression avoid to have less free sites than J
        matrix, domain_coordinates, number_domains = JMAK.nucleation(matrix,N,dim,J,domain_coordinates,number_domains,seed)
    matrix, domain_coordinates, number_domains = JMAK.growth(matrix,N,dim,R,domain_coordinates,number_domains)
    
    filled_fraction = number_domains/N**dim
    t = t+1 #increase time after each step
    table_filled_fraction[counter_table] = [t,filled_fraction] #update filled fraction
    counter_table = counter_table+1
    print("Progression: ",round(filled_fraction*100,2),"%" )
    

###############################################################################
#DATA ANALYSIS AND PLOT
###############################################################################   
    #this firs plotting expression is inside the while 
    dt.plot_matrix(domain_coordinates, dim, filled_fraction,name)

dt.plot_JMAK(table_filled_fraction,N,dim,J,R,name) 
    
