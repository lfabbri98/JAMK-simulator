# Simulation of a phase transition from Metal+H to metal hydride

## Introduction

This is a program that simulates the phase transformation from a system composed by a metal and molecular hydrogen to a metal hydride system. 
The model is based on simultaneous nucleation and growth. 
This kind of process can be nicely described by Johnson-Mehl-Avrami-Kolmogorov kinetics (JMAK kinetics) which have the following analytical behaviour:

![equation1](https://github.com/lfabbri98/Images/blob/main/eq1.png)

where **eta** is the fraction of transformed domain, **n** is a parameter that depends on dimensionality (1D/2D/3D) and **k** is a constant. 
Further information on JMAK kinetics can be found in [1], [2].

To test simulated results it's possible to perform a fit using the following relation:

![eq2](https://github.com/lfabbri98/Images/blob/main/CodeCogsEqn%20(2).png)

where d can be found as the angular coefficient of fit.

## System and model

The user is asked to provide different parameters writing them in the file *config.txt*: 
matrix dimension N, dimensionality of the process n, nucleation rate J and growth velocity R are
relative to physical properties of the simulations. Moreover the user should provide a name and a generation seed.
 The phase transition is modelled as happening on a matrix with side length N (matrix dimesion), 
depending on dimensionality n. For example, if one chooses N=100 and n=2 then a bidimensional matrix with 100x100 cells will be created. Each cell can be empty or filled 
with a single hydrogen atom. At each instant of time J new domains will be created randomly inside the matrix 
(domains’ positions will be generated according to a uniform distribution) and already present domains will grow in each direction with velocity R. So if, for example, R=2 then each domain will grow of 2 hydrogen atoms in each direction per unit time. 
The case considered is only the one with constant R and constant nucleation rate J. This means that expected d is d = 1+n.

## Dependencies

Dependencies for this program can be found in file *dependencies.txt*.

## Usage

Before starting the simulation be sure to fill configuration file *config.txt*
which is store in the same folder of the program. Be also sure to have installed all
dependencies.

To start the program simply run file **main.py**.
**Attention! All parameters must be integers. The program is provided of a control on user input. Be aware that non-integer parameters have no physical meaning.**

After the simulation (it can require much time, depending on your input paramters)
a plot of JMAK kinetic is saved into the folder *Outputs* with also some screenshots of the matrix, taken during the execution.

## Outputs

Output plots are created with library *matplotlib* and two functions are dedicated to
produce visive outcomes of simulation.

Output files will be saved in two different ways in the specific folder *Outputs/name*:

- *name-JMAK.png* for JMAK kinetics

- *name-MATRIX-fillin_percentage.png* for screenshots of matrix taken during execution

The string *name* is the same which must be provided into configuration file.

Moreover parameters of fit are plotted in the console.

## Structure of the project

This project is divided into many files:

- **main.py** : starting file, it contains the instructions to run all the simulation.

- **start.py** : contains the function *system_creation* and *generate_pos_table* which respectively creates the matrix and the table where all nuclei positions will be stored.

- **JMAK.py** : file which contains the heart of the program. There are all the functions related to nucleation of new domines and growth of existent ones.

- **data_analysis.py** : contains all the function to analyze output data of the program and to plot data

- **testing.py** : contains routine tests on the main functions of project

## References

[1]	L. Fabbri, “Simulazione e analisi della formazione di idruri metallici.”, *Thesis*, 2020.

[2]	R. W. Balluffi, S. M. Allen, and W. C. Carter, "Kinetics of Materials.", Wiley - Interscience, 2005.



