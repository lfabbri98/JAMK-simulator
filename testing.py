from hypothesis import given
import hypothesis.strategies as st
import numpy as np
import JMAK
import start

def test_input():
    """
    Tests if returning type of function import_parameters are correct


    """
    
    N,dim,J,R,seed,name = start.import_parameters()
    assert isinstance(N, int)
    assert isinstance(dim, int)
    assert isinstance(J, int)
    assert isinstance(R, int)
    assert isinstance(seed, int)
    assert isinstance(name, str)
    
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
        assert m_before.all() ==0 #matrix before should be empty
        assert m_after.any()!=0 #error if empty matrix remains empty after nucleation
        assert num_nuc == J #test if number of nuclei is increased by J
            
    
@given (dim=st.integers(2,3),J=st.integers(1,50),num_nuc_before=st.integers(0,100))
def test_nucleation_correct_number_new_nuclei(dim,J,num_nuc_before):
    """
    Tests if the nucleation of a new domine leads to a correct increment of 
    number of nuclei in the system.
    
    Parameters
    ----------
    dim : int
        try both 2D and 3D cases
    J : int
        nucleation rate can sweep up to 50, which is very high value and
        almost a limit case
    num_nuc_before : int
        starting number of nuclei, to try if an initial number different from 0
        makes any difference

    """
    N=100
    pos = start.generate_pos_table(N, dim)
    m = start.system_creation(N, dim)
    m, pos, num_nuc = JMAK.nucleation(m,N,dim,J,pos,num_nuc_before)
    assert num_nuc == num_nuc_before+J #number of nuclei after nucleation must be increased by J
    num_nuc_before = num_nuc


def test_correct_add_table():
    """
    Tests if repeated nucleations lead to a correct increment in table of
    positions. 30 repetitions are tested for different J on a wide range.

    """
    for J in range(0,30):
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
        
def test_correct_return_nucleation():
    """
    Tests if function nucleation returns variables of the correct type and
    dimension
    """
    N = 100
    dim = 2
    J = 2
    matrix = start.system_creation(N, dim)
    pos = start.generate_pos_table(N, dim)
    #perform nucleation
    matrix, pos, num_nuclei = JMAK.nucleation(matrix, N, dim, J, pos)
    #controls on correct dimension
    assert np.size(matrix) == N**dim
    assert np.size(pos) == N**dim * dim
    #controls on type
    assert isinstance(matrix, np.ndarray) == True
    assert isinstance(pos, np.ndarray) == True
    assert isinstance(num_nuclei, int) == True

def test_correct_number_growth_center():
    """
    Function that tests if growth from a single domain in the center of matrix
    leads to a correct increment in number of nuclei. Tests also if increment in
    position table is correct

    """
    N = 100
    dim = 2
    #do the test for different values of growth velocity R
    for R in range(1,10):
        num_nuclei = 1
        pos = start.generate_pos_table(N, dim)
        matrix = start.system_creation(N, dim)
        #insert a single domain in the center of matrix
        matrix[50,50] = 1
        #update table with domain
        pos[0] = [50,50]
        matrix, pos, num_nuclei = JMAK.growth(matrix, N, dim, R, pos, num_nuclei)
        #since growth is in 2 directions after it we should have 4*R new domains
        assert num_nuclei == 1+4*R
        #select only non empty lines from position tables
        choose_values_1 = np.where(pos[:,0]!=0)
        choose_values_2 = np.where(pos[:,1]!=0)
        choose_values = np.union1d(choose_values_1,choose_values_2)
        #similarly also position table should be updated with the same number of lines
        assert len(pos[choose_values]) == 1+4*R
        assert len(pos[choose_values]) == num_nuclei

def test_correct_return_growth():
    """
    Tests if function growth returns correct values for dimensions and type.
    Very similar to correspondent test for nucleation, this is implemented to 
    avoid multiple failings from the same test.

    """    
    N = 100
    dim = 2
    J = 2
    R = 3
    matrix = start.system_creation(N, dim)
    pos = start.generate_pos_table(N, dim)
    #perform nucleation
    matrix, pos, num_nuclei = JMAK.nucleation(matrix, N, dim, J, pos)
    #perform growth
    matrix, pos, num_nuclei = JMAK.growth(matrix, N, dim, R, pos, num_nuclei)
    #controls on correct dimension
    assert np.size(matrix) == N**dim
    assert np.size(pos) == N**dim * dim
    #controls on type
    assert isinstance(matrix, np.ndarray) == True
    assert isinstance(pos, np.ndarray) == True
    assert isinstance(num_nuclei, int) == True
    
def test_growth_circolarity():
    """
    Tests if a growth process circularity is correct. Basically the matrix is 
    thought to be connected like in a toroidal geometry. So adding a nucleus in
    last position + 1 should create that nucleus in position 1
    """
    N = 10
    dim = 2
    R = 1
    num_nuclei = 1
    pos = start.generate_pos_table(N, dim)
    matrix = start.system_creation(N, dim)
    matrix[5,N-1] = 1
    pos[0] = [5,9]
    matrix, pos, num_nuclei = JMAK.growth(matrix, N, dim, R, pos, num_nuclei)
    assert matrix[5,0] == 1
    
def test_full_JMAK():
    """
    Tests if number of nuclei and length of non-empty pos table are the same 
    after some cycles of full JMAK process (nucleation +  growth)

    """
    N = 100
    dim = 2
    J = 2
    R = 3
    matrix = start.system_creation(N, dim)
    pos = start.generate_pos_table(N, dim)
    num_nuclei = 0
    for i in range(5):
        matrix, pos, num_nuclei = JMAK.nucleation(matrix, N, dim, J, pos, num_nuclei)
        matrix, pos, num_nuclei = JMAK.growth(matrix, N, dim, R, pos, num_nuclei)
    choose_values_1 = np.where(pos[:,0]!=0)
    choose_values_2 = np.where(pos[:,1]!=0)
    choose_values = np.union1d(choose_values_1,choose_values_2)
    assert len(pos[choose_values]) == num_nuclei    
