def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if ints == []:
        return None, None

    minn = float('inf')
    maxx = -float('inf')

    for n in ints:
        if n < minn:
            minn = n
        if n > maxx:
            maxx = n
    return minn, maxx

if __name__ == '__main__':

## Example Test Case of Ten Integers

    import random
    l = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(l)
    assert (0, 9) == get_min_max(l)

    # More extreme test
    l = [i for i in range(0, 100000)]  # a list containing 0 - 9
    random.shuffle(l)
    assert (0, 100000 -1) == get_min_max(l)

    # Edge cases

    assert (None, None) == get_min_max([])
    assert 1 ,1  == get_min_max([1])
    assert 1 ,2  == get_min_max([2,1])
    print('All tests passed')
