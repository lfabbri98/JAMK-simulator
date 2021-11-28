from hypothesis import given
import hypothesis.strategies as st
import numpy as np
import JMAK
import start

@given (dim=st.integers(2,3),J=st.integers(1,50))
def test_nucleation_correct_number_new_nuclei(dim,J):
    N=100
    num_nuc_before = 0
    pos = start.generate_pos_table(N, dim)
    m = start.system_creation(N, dim)
    m, pos, num_nuc = JMAK.nucleation(m,N,dim,J,pos,num_nuc_before)
    assert num_nuc == num_nuc_before+J
    num_nuc_before = num_nuc

@given(J=st.integers(1,30))
def test_correct_add_table(J):
    N = 100
    dim = 2
    num_nuc = 0
    pos = start.generate_pos_table(N, dim)
    m = start.system_creation(N, dim)
    for i in range(1,20):
        m, pos, num_nuc = JMAK.nucleation(m,N,dim,J,pos,num_nuc)
        choose_values_1 = np.where(pos[:,0]!=0)
        choose_values_2 = np.where(pos[:,1]!=0)
        choose_values = np.union1d(choose_values_1,choose_values_2)
        assert num_nuc == len(pos[choose_values])
    assert num_nuc == 19*J
    

    
    
    