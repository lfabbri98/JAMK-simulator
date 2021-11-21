#This is main file, starting point

#including libraries
from start import *
from controls import *
from JMAK import *
from data_analysis import *

###############################################################################
#INITIALIZATION OF PARAMETERS
###############################################################################

init_data, name = init_simulation() #open initialization prompt
for x in range(4):
    init_data[x] = int(init_data[x]) #convert all strings to int

###############################################################################      
#SIMULATION
###############################################################################
matrix = system_creation(init_data)
t = 0 #time counter
domain_coordinates = generate_pos_table(init_data) #table with coordinates of all points
number_domains = 0 #domains counter
table_filled_fraction = np.zeros((init_data[0]**init_data[1],2)) #table with filled fraction in function of time
counter_table = 0 #counter for filling previous table

while number_domains/init_data[0]**init_data[1] < 1:
    
    #2D case
    if init_data[1] == 2:
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
    plot_matrix(domain_coordinates, init_data,number_domains/init_data[0]**init_data[1],name)
plot_JMAK(table_filled_fraction,counter_table,init_data,name)
    
       
   
    
