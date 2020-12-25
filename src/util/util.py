def get_nth_bit_from_right(binary, n):
    """
    :param binary: value to extract a bit from
    :param n: nth bit to extract (0 indexed)
    :return: nth bit from right
    """
    return (binary & (1 << n)) >> n


def get_nth_bit_from_left(binary, n):
    """
        :param binary: value to extract a bit from
        :param n: nth bit to extract (0 indexed)
        :return: nth bit from left
        """
    return get_nth_bit_from_right(binary, binary.bit_length() - n - 1)
