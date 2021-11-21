import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import time

def poly1(x,A,B):
    return A+B*x

def plot_JMAK(table,counter_table,params,name):
    #import of table and date to save figure
    table = table[table[:,1]!=0]
    table = table[table[:,1]!=1]
    #plotting
    plt.figure()
    plt.plot(table[:,0],table[:,1])
    plt.xlabel("Time (steps)")
    plt.ylabel("$\eta$")
    plt.grid();
    plt.title("Simulated JMAK kinetic for N="+str(params[0])+", n="+str(params[1])+", J="+str(params[2])+", R="+str(params[3]))
    plt.savefig('./Outputs/'+name+'/'+name+'-JMAK.png')
    plt.close()
    
    #fitting
    median_table = int(counter_table/2)
    X = np.log(table[:,0])
    Y = np.log(-np.log(1-table[:,1]))
    popt, pcov = curve_fit(poly1,X,Y)
    print("Fitted with linear model A+B*x")
    errors = np.sqrt(np.diag(pcov))
    print("A = "+str(popt[0])+" +- "+str(errors[0]))
    print("B = "+str(popt[1])+" +- "+str(errors[1]))


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
    plt.close()
    