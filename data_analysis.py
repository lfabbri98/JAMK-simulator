import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import time

def plot_JMAK(table):
    date = time.strftime("%Y-%m-%d-%H-%M-%S")
    table = table[table[:,1]!=0]
    plt.figure()
    plt.plot(table[:,0],table[:,1])
    plt.xlabel("Time (steps)")
    plt.ylabel("$\eta$")
    plt.grid();
    plt.title("Simulated JMAK kinetic")
    plt.savefig('./Outputs/'+date+'.png')
    