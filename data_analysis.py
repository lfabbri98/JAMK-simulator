import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def poly1(x,A,B):
    """
    Function used as fitting function for linear fit

    Parameters
    ----------
    x : float
        variable of linear function
    A : float
        intercept
    B : float
        slope

    Returns
    -------
    float
        linear function evulated in point x

    """
    return A+B*x

def plot_JMAK(table,N,dim,J,R,name):
    """
    Function that plots JMAK kinetic for the specific case with parameters
    N,dim,J,R and performs a linear fit on the central part of the curve.

    Parameters
    ----------
    table : array of int
        table of two columns with filling percentage of matrix in function of time
    N : int
        side length of matrix
    dim : int
        dimensionality of process
    J : int
        how many nuclei are placed in the matrix per unit time
    R : int
       growth velocity of already nucleated domains
    name : str
        string with name of simulation

    Graphical output
    -------
    Plot of JMAK kinetic and save in relative folder; fit parameters shown on console

    """
    #selecting only values different from 0 and 1 not to have problems with log
    table = table[table[:,1]!=0]
    table = table[table[:,1]!=1]
    #plotting
    plt.figure()
    plt.plot(table[:,0],table[:,1])
    plt.xlabel("Time (steps)")
    plt.ylabel("$\eta$")
    plt.grid();
    plt.title("Simulated JMAK kinetic for N="+str(N)+", n="+str(dim)+", J="+str(J)+", R="+str(R))
    plt.savefig('./Outputs/'+name+'/'+name+'-JMAK.png')
    plt.close()
    
    #fitting
    median_table = int(len(table)/2)
    #fit only central part of kinetic since it's where border effects are negligible
    #take a 20% tolerance from center of kinetic
    right_side_data = int(median_table + 20/100 * len(table))
    left_side_data = int(median_table - 20/100 * len(table))
    
    try:
        #defining fit array from equations of kinetic
        X = np.log(table[left_side_data:right_side_data,0])
        Y = np.log(-np.log(1-table[left_side_data:right_side_data,1]))
        #fit central part with a linear function as it should be 
        popt, pcov = curve_fit(poly1,X,Y)
        #print parameters of fit in console
        print("Fitted with linear model A+B*x")
        errors = np.sqrt(np.diag(pcov))
        print("A = "+str(popt[0])+" +- "+str(errors[0]))
        print("B = "+str(popt[1])+" +- "+str(errors[1]))
    except:
        print("Combination of parameters lead to a very borderline case. It has not been possible to fit data because simulation was too fast.")
        pass

def plot_matrix(table_positions, dim, fraction,name):
    """
    Function that plots and saves a screenshot of the matrix 

    Parameters
    ----------
    table_positions : array of int
        table with positions of all nuclei
    dim : int
        dimensionality of the process
    fraction : float
        filling fraction of matrix, goes from 0 to 1
    name : str
        string which corresponds to name of simulation

    Graphical output
    -------
    A plot produced with matplotlib is saved for different percentages. Maximum 
    one for each percent.

    """
    if dim == 3:
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.scatter(table_positions[:,0],table_positions[:,1], table_positions[:,2],color='blue')
    
    if dim == 2:       
        plt.scatter(table_positions[:,0],table_positions[:,1],color='blue')
    
    #fraction is rounded at 0 digits so figures with same percentage are overwritten
    #leading to a single figure for every % at most.
    frac = round(fraction*100) 
    plt.title("Matrix at "+str(frac)+" %")
    plt.savefig('./Outputs/'+name+'/'+name+'-MATRIX-'+str(frac)+'.png')
    plt.close()
