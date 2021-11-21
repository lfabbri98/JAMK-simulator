# Simulation of a phase transition from Metal+H to metal hydride

## Introduction

This is a program that simulates the phase transformation from a system composed by a metal and molecular hydrogen to a metal hydride system. 
The model is based on simultaneous nucleation and growth. 
This kind of process can be nicely described by Johnson-Mehl-Avrami-Kolmogorov kinetics (JMAK kinetics) which have the following analytical behaviour:

![equation1](https://github.com/lfabbri98/Images/blob/main/eq1.png)

where **eta** is the fraction of transformed domain, **n** is a parameter that depends on dimensionality (1D/2D/3D) and **k** is a constant. 
Further information on JMAK kinetics can be found in [1], [2].

## System and model

The user is asked to provide four different parameters: 
matrix dimension N, dimensionality of the process n, nucleation rate J, growth velocity R. The phase transition is modelled as happening on a matrix that will be as big as N, 
depending on dimensionality n. For example, if one chooses N=1000 and n=2 then a bidimensional matrix with 1000x1000 cells will be created. Each cell can be empty or filled 
with a single hydrogen atom. At each instant of time J new domains will be created randomly inside the matrix 
(domains’ positions will be generated according to a uniform distribution) and already present domains will grow in each direction with velocity R. So if, for example, R=2 then each domain will grow of 2 hydrogen atoms in each direction per unit time. 
The case considered is only the one with constant R and constant nucleation rate J. This means that expected d is d = 1+n.

## Usage

To start the program simply run file **main.py**.
**Attention! All parameters must be integers. The program is provided of a control on user input. Be aware that non-integer parameters have no physical meaning.**

After the simulation (it can require much time, depending on your input paramters)
a plot of JMAK kinetic is saved into the folder *Outputs*, named with date and time of execution.

**PLEASE BE SURE TO CREATE THE FOLDER *Outputs* BEFORE RUNNING THE PROGRAM**

Output files will be saved in two different ways:

- *name-JMAK.png* for JMAK kinetics

- *name-MATRIX-fillin_percentage.png* for screenshots of matrix taken during execution

## Structure of the project

This project is divided into many files:

- **main.py** : starting file, it contains the instructions to run all the simulation.

- **start.py** : contains the function *init_simulation* that initializes the parameters through a graphical user interface. It also contains the function *system_creation* which is responsible for the creation of the matrix.

- **controls.py** : it contains many control functions such as *input_control* and *is_all_full*.

- **JMAK.py** : file which contains the heart of the program. There are all the functions related to nucleation of new domines and growth of existent ones.

- **data_analysis.py** : contains all the function to analyze output data of the program and to plot data
## References

[1]	L. Fabbri, “Simulazione e analisi della formazione di idruri metallici.”, *Thesis*, 2020.

[2]	R. W. Balluffi, S. M. Allen, and W. C. Carter, Kinetics of Materials. Wiley - Interscience, 2005.



