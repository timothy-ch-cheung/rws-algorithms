from src.util.util import get_nth_bit_from_left


def double_and_add(n, P):
    q = 0
    for i in range(P.bit_length()):
        q = 2 * q
        if get_nth_bit_from_left(P, i) == 1:
            q += n
    return q
