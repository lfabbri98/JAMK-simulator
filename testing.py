from hypothesis import given
import hypothesis.strategies as st
import numpy as np
import JMAK
import start

def test_matrix_changed_nucleation():
    """
    Tests if a nucleation process effectively changes the matrix and if J nuclei
    are added after nucleation

    """
    dim = 3
    J = 1
    for N in [10,100,500,1000]: #try different side lengths 
        num_nuc = 0
        m_before = start.system_creation(N, dim)
        pos = start.generate_pos_table(N, dim)
        m_after, pos, num_nuc = JMAK.nucleation(m_before,N,dim,J,pos,num_nuc)
        print(m_after)
        assert m_after.any()!=0 #error if empty matrix remains empty after nucleation
        assert num_nuc == J #test if number of nuclei is increased by J
            
    
@given (dim=st.integers(2,3),J=st.integers(1,50),num_nuc_before=st.integers(0,100))
def test_nucleation_correct_number_new_nuclei(dim,J,num_nuc_before):
    """
    Tests is the nucleation of a new domine leads to a correct increment of 
    number of nuclei in the system.
    
    Parameters
    ----------
    dim : int
        try both 2D and 3D cases
    J : int
        nucleation rate can sweep up to 50, which is very high value and
        not common
    num_nuc_before : int
        starting number of nuclei, to try if an initial number different from 0
        make any difference


    """
    N=100
    #num_nuc_before = 0
    pos = start.generate_pos_table(N, dim)
    m = start.system_creation(N, dim)
    m, pos, num_nuc = JMAK.nucleation(m,N,dim,J,pos,num_nuc_before)
    assert num_nuc == num_nuc_before+J #number of nuclei after nucleation must be increased by J
    num_nuc_before = num_nuc

@given(J=st.integers(1,30))
def test_correct_add_table(J):
    """
    Tests if repeated nucleations lead to a correct increment in table of
    positions. 20 repetitions are tested for different J on a wide range.

    Parameters
    ----------
    J : int
        nucleation rate on a wide range

    """
    N = 100
    dim = 2
    num_nuc = 0
    pos = start.generate_pos_table(N, dim)
    m = start.system_creation(N, dim)
    for i in range(1,J):
        m, pos, num_nuc = JMAK.nucleation(m,N,dim,J,pos,num_nuc)
        #Choose only non-empty lines
        choose_values_1 = np.where(pos[:,0]!=0)
        choose_values_2 = np.where(pos[:,1]!=0)
        choose_values = np.union1d(choose_values_1,choose_values_2)
        #The number of nuclei after each step must be equal to non-empty lines in table of positions
        assert num_nuc == len(pos[choose_values])
    #Total number of nuclei after full process must be equal to the # of repetitions times nucleation rate
    assert num_nuc == (J-1)*J
    

    
    
    