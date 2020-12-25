from src.util.util import get_nth_bit_from_left


def square_and_multiply(base, exp):
    output = base
    for i in range(1, exp.bit_length()):
        if get_nth_bit_from_left(exp, i) == 0:
            output = pow(output, 2)
        else:
            output = pow(output, 2) * base
    return output
