
import math as m

from conjugate_methods import conjugate_method_with_matrix_reconstruction as mr
from conjugate_methods import conjugate_method_without_matrix_reconstruction as wmr

H0 = [[1, 0, 0],
      [0, 1, 0],
      [0, 0, 1]]

x = [1, 0, -1]


def polynomial_func(x):
    return 2*m.pow(x[0], 4) + 3*m.pow(x[1], 4) + 16*m.pow(x[2], 4) + \
           12 * m.pow(x[0], 2) * m.pow(x[1], 2) - 8 * m.pow(x[0], 3) * x[1] \
           - 8 * x[0] * m.pow(x[1], 3) + 24 * m.pow(x[1], 2) * m.pow(x[2], 2) \
           - 8 * m.pow(x[1], 3) * x[2] - 32 * x[1] * m.pow(x[2], 3) \
           + 4 * m.pow(x[0], 2) - 16 * x[0] + 6


def x1_der_of_polynomial_func(x):
    return 8 * m.pow(x[0], 3) + 24 * x[0] * m.pow(x[1], 2) - 24 * m.pow(x[0], 2) * x[1] \
           - 8 * m.pow(x[1], 3) + 8 * x[0] - 16


def x2_der_of_polynomial_func(x):
    return 12 * m.pow(x[1], 3) + 24 * m.pow(x[0], 2) * x[1] - 8 * m.pow(x[0], 3) \
           - 24 * x[0] * m.pow(x[1], 2) + 48 * x[1] * m.pow(x[2], 3) - 24 * m.pow(x[1], 2) * x[2] \
           - 32 * m.pow(x[2], 3)


def x3_der_of_polynomial_func(x):
    return 64 * m.pow(x[2], 3) + 48 * m.pow(x[1], 2) * x[2] - 8 * m.pow(x[1], 3) \
           - 96 * x[1] * m.pow(x[2], 3)


def test_methods():
    print("Please, choose the methods that you want to run: ")
    print("1 - conjugate method with matrix reconstruction")
    print("2 - conjugate method without matrix reconstruction")
    chosen_method = int(input("Enter the method number: "))
    # polynomial, x1_der, x2_der, x3_der, H0, x0
    # TODO: later on build functions for analysis
    if chosen_method == 1:
        mr.conjugate_method_with_matrix_reconstruction(polynomial_func,
                                                       x1_der_of_polynomial_func,
                                                       x2_der_of_polynomial_func,
                                                       x3_der_of_polynomial_func,
                                                       H0, x)
    elif chosen_method == 2:
        wmr.conjugate_method_without_matrix_reconstruction(polynomial_func,
                                                       x1_der_of_polynomial_func,
                                                       x2_der_of_polynomial_func,
                                                       x3_der_of_polynomial_func,
                                                       H0, x)