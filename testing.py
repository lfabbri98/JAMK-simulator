from controls import *
from hypothesis import given, settings
import hypothesis.strategies as st
import numpy as np
from start import *
from JMAK import *

"""max(N) = 1500 to avoid saturation of memory. Obviusly it depends on the
machine. Tests are done on a machine with 16GB of RAM which is generally
in the average for nowadays consumer machines
"""
@given(N=st.integers(0,1500), n=st.integers(2,3), J=st.integers(0), R=st.integers(0))
@settings(deadline=None)
def test_correct_generate_matrix(N,n,J,R):
    if n==2:
        matrix = system_creation([N,n,J,R])
        assert np.size(matrix) == N**2
    if n==3:
        matrix = system_creation([N,n,J,R])
        assert np.size(matrix) == N**3
     
@given(N=st.integers(0,1000),n=st.integers(2,3))
@settings(deadline=None)
def test_correct_generate_table_positions(N,n):
    table = np.zeros((N**n, n))
    assert len(table) == N**n
    assert np.size(table) == N**n * n

@given(N=st.integers(10,100),J=st.integers(1,10))
@settings(deadline=None)
def test_nucleation_2D(N,J):
    matrix = np.zeros((N,N))
    params = [N,2,J,1]
    num_nuclei = 0
    position_nuclei = generate_pos_table(params)
    matrix, position_nuclei, num_nuclei = nucleation_2D(matrix, params, position_nuclei, num_nuclei)
    assert num_nuclei == J

@given(N=st.integers(10,100),J=st.integers(1,10))
@settings(deadline=None)
def test_nucleation_3D(N,J):
    matrix = np.zeros((N,N,N))
    params = [N,3,J,1]
    num_nuclei = 0
    position_nuclei = generate_pos_table(params)
    matrix, position_nuclei, num_nuclei = nucleation_3D(matrix, params, position_nuclei, num_nuclei)
    assert num_nuclei == J
    