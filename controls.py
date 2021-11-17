import numpy as np
#function to control that inserted parameters for simulation are 
#all integers
def input_control(data):
    
    for x in range(len(data)):
        try:
            value = int(data[x]) #error if conversion to int is impossible
        except:
            print("Attention! You inserted some non integer parameters! Please retry and be more careful!")
            return True
        
    #n can be only 2 or 3 -> physical reason
    if not (int(data[1])==2 or int(data[1]==3)):
        print("You put a wrong n.")
        return True
    
    return False

#this function controls if the matrix if all full
def is_all_full(is_full_matrix, params):
        
    if params[1] == 2:
        for i in range(0,params[0]):
            for j in range(0, params[0]):
                if is_full_matrix[i,j] == 0:
                    return False
    if params[1] == 3:
        for i in range(0,params[0]):
            for j in range(0, params[0]):
                for k in range(0,params[0]):
                    if is_full_matrix[i,j,k] == 0:
                        return False
                
        return True
