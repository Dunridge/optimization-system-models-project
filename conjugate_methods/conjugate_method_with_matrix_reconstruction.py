
import math as m

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


def conjugate_method_with_matrix_reconstruction():
    # k = 0, n = 3
    return "conjugate_method_with_matrix_reconstruction"



