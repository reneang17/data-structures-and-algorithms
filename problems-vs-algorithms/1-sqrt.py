
def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        return -1
    lower = 0
    upper = number
    mid  = lower + (upper-lower) //2
    while True:
        if mid < int(number**0.5):
            lower = mid+1
        elif mid > int(number**0.5):
            upper = mid -1
        else:
            return mid
        mid  = lower + (upper-lower)//2
    return -1

if __name__ == '__main__':
    def test_edges():
        assert 0 == sqrt(0)
        assert 1 == sqrt(1)
        assert -1 == sqrt(-1)
        print('Edge cases passed')
    test_edges()

    def test_stardardcases():
        assert 2 == sqrt(4)
        assert 3 == sqrt(9)
        assert 4 == sqrt(16)
        assert 5 == sqrt(27)
        assert 9 == sqrt(81)
        print('Standard cases passed')
    test_stardardcases()
