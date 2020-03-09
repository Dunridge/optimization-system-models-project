
from conjugate_methods import conjugate_method_with_matrix_reconstruction as mr
from conjugate_methods import conjugate_method_without_matrix_reconstruction as wmr

def test_methods():
    print("Please, choose the methods that you want to run: ")
    print("1 - conjugate method with matrix reconstruction")
    print("2 - conjugate method without matrix reconstruction")
    chosen_method = int(input("Enter the method number: "))
    # TODO: later on build functions for analysis
    if(chosen_method == 1):
        mr.conjugate_method_with_matrix_reconstruction()
    elif(chosen_method == 2):
        wmr.conjugate_method_without_matrix_reconstruction()
