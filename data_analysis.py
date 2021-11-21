import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import time

def plot_JMAK(table,counter_table,params,name):
    #import of table and date to save figure
    table = table[table[:,1]!=0]
    assert len(table) == counter_table
    #plotting
    plt.figure()
    plt.plot(table[:,0],table[:,1])
    plt.xlabel("Time (steps)")
    plt.ylabel("$\eta$")
    plt.grid();
    plt.title("Simulated JMAK kinetic for N="+str(params[0])+", n="+str(params[1])+", J="+str(params[2])+", R="+str(params[3]))
    plt.savefig('./Outputs/'+name+'/'+name+'-JMAK.png')

def plot_matrix(table_positions, params, fraction,name):
    if params[1] == 3:
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.scatter(table_positions[:,0],table_positions[:,1], table_positions[:,2],color='blue')
    
    if params[1] == 2:       
        plt.scatter(table_positions[:,0],table_positions[:,1],color='blue')
        
    frac = round(fraction*100) 
    plt.title("Matrix at "+str(frac)+" %")
    plt.savefig('./Outputs/'+name+'/'+name+'-MATRIX-'+str(frac)+'.png')