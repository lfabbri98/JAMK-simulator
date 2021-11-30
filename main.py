#including libraries
import JMAK
import os
import start
import numpy as np
import data_analysis as dt


###############################################################################
#INITIALIZATION OF PARAMETERS
###############################################################################

"""
Description of parameters:
    
    - N : length of the side of the matrix
    
    - dim : dimensionality of the process, can be 2 or 3
    
    - J : number of new nuclei that are generated inside the matrix for each time step
    
    - R : number of new nuclei that are growth in all directions around each nucleus
    
    - name : name of simulation, will be used for outputs
    
    - seed : seed which will be used to initialize random number generation seed
"""

#initialization of parameters in input through dedicated function
N,dim,J,R,seed,name = start.import_parameters()

#initialization of internal parameters
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

while filled_fraction <= 0.999:

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

    #this first plotting expression is inside the while to plot matrix screenshot
    #many times
    dt.plot_matrix(domain_coordinates, dim, filled_fraction,name)

dt.plot_JMAK(table_filled_fraction,N,dim,J,R,name) 
    
