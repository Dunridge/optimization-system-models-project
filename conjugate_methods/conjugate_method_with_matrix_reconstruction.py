
import math as m
import numpy as np


def conjugate_method_with_matrix_reconstruction(polynomial, x1_der, x2_der, x3_der, H0, x):
    # k = 0, n = 3
    k = 0
    x1_der_val = x1_der(x)
    x2_der_val = x2_der(x)
    x3_der_val = x3_der(x)
    f_val_on_prev_step = 2
    f_val_on_next_step = 1
    x_on_prev_step = x
    x_on_current_step = 0
    x_on_next_step = 0
    der_value_vector = [x1_der_val, x2_der_val, x3_der_val]
    limit_val = m.pow(10, -15)
    rho = 0.05
    while (x1_der_val != 0 or x2_der_val != 0 or x3_der_val != 0) or f_val_on_prev_step - f_val_on_next_step < limit_val:
        f_val_on_prev_step = polynomial(x)
        if k == 0:
            h = - np.transpose(H0) * der_value_vector
            rho = minimize_rho_function(x, rho, h)
            x = x + [elem * rho for elem in h]
            k = k + 1
            # TODO: and than make the program go to the start of the while condition

        # h0 = - np.transpose(H0) * der_value_vector
        if k % len(x) == 0:
            H = H0
            # TODO: and than make the program go to the 8th step
        else:
            return
            # TODO: make the program go to the 6th step

        r = x

        # rho_min = minimize_rho_function(x, rho, h0)

        # function value after the algorithm is calculated
        f_val_on_next_step = polynomial(x)
        k = k + 1

    if x1_der_val != 0 or x2_der_val != 0 or x3_der_val != 0:
        return x


    return "conjugate_method_with_matrix_reconstruction"


def minimize_rho_function(x, rho, h0):
    rho_min = 0
    return rho_min


