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