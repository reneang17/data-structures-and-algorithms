from basic_algorithms import Mergesort

def rearrange_digits(arr):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    #First we reorder the list using Mergesort
    #from scratch
    if len(arr) == 0:
        return [0,0]
    if len(arr) == 1:
        return [0,arr[0]]

    mergesort = Mergesort()
    arr = mergesort.sortArray(arr)

    n2 = ''
    for i in range(len(arr)-1, -1 ,-2):
        n2+=str(arr[i])

    n1 = ''
    for i in range(len(arr)-2, -1 ,-2):
        n1+=str(arr[i])

    return [int(n1), int(n2)]

if __name__ == '__main__':

    def test_function(test_case):
        output = rearrange_digits(test_case[0])
        solution = test_case[1]
        assert sum(output) == sum(solution)


    test_function([[1, 2, 3, 4, 5], [542, 31]])
    test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

    test_function([[1,0], [0, 1]])
    test_function([[0,0], [0, 0]])
    test_function([[1], [0, 1]])
    print('All test cases passed')
