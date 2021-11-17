#This is main file, starting point

#including libraries
import PySimpleGUI as sg
from start import *
from controls import *
import pytest
from JMAK import *
import time
import matplotlib.pyplot as plt
import os

###############################################################################
#INITIALIZATION OF PARAMETERS
###############################################################################

init_data = init_simulation() #open initialization prompt
for x in range(4):
    init_data[x] = int(init_data[x]) #convert all strings to int

###############################################################################      
#SIMULATION
###############################################################################
matrix = system_creation(init_data)
t = 0 #time counter
domain_coordinates = generate_pos_table(init_data)
number_domains = 0 #domains counter

while number_domains < init_data[0]**init_data[1]:
    
    if init_data[1] == 2:
        matrix, domain_coordinates, number_domains = nucleation_2D(matrix, init_data, domain_coordinates, number_domains)
        
    if init_data[1] == 3:
        matrix, domain_coordinates, number_domains = nucleation_3D(matrix, init_data, domain_coordinates, number_domains)
    
    t = t+1
    print("Progession: ",round(number_domains/init_data[0]**init_data[1]*100,3),"%" )
    
    
        
    
       
   
    
