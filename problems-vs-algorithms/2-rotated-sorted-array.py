from basic_algorithms import binary_search

def rotated_array_search(arr, number):
    """
    Find the index by searching in a rotated sorted array
    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    # Address edge cases
    if len(arr) == 0: return -1
    if len(arr) == 1 and number == arr[0]:
        return 0
    if len(arr) == 1 and number != arr[0]:
        return -1


    # Search for index of rotation
    pivot = search_pivot(arr)


    sorted_arr= arr[pivot+1:] + arr[:pivot+1]
    sorted_index = binary_search(arr[pivot+1:] + arr[:pivot+1], number)

    if sorted_index  == -1:
        return -1

    if sorted_index <= len(arr[pivot+1:])-1:
        rotated_index = sorted_index + len(arr[:pivot+1])
    else:
        rotated_index = sorted_index - len(arr[pivot+1:])


    return rotated_index



def search_pivot(arr):
    """
    Find rotation index of a sorted array
    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index
    """
    if len(arr)<=1: return 0
    if len(arr)==2 and arr[0] > arr[1]: return 0
    n = len(arr)-1
    lower = 0
    upper = n
    mid = lower +  (upper - lower) //2
    while True:
        if mid == n and arr[n-1] > arr[n]:
            return mid
        elif arr[0] <= arr[mid] > arr[mid +1]:
            return mid
        elif arr[0] <= arr[mid] <= arr[mid +1]:
            lower =  mid + 1
        elif arr[0] > arr[mid]:
            upper =  mid - 1
        mid = lower +  (upper - lower) //2




if __name__ == '__main__':
    def test_search_pivot():
        assert search_pivot([6, 7, 8, 9, 10, 1, 2, 3, 4]) == 4
        assert search_pivot([6, 7, 8, 1, 2, 3, 4]) == 2
        assert search_pivot([6, 1, 2, 3, 4]) == 0
        assert search_pivot([1, 2, 0]) == 1
        assert search_pivot([1, 0]) == 0
        assert search_pivot([1]) == 0
        print('Search pivot tests passed')

    test_search_pivot()






    def linear_search(input_list, number):
        for index, element in enumerate(input_list):
            if element == number:
                return index
        return -1

    def test_function(test_case):
        input_list = test_case[0]
        number = test_case[1]
        assert linear_search(input_list, number) == rotated_array_search(input_list, number)
        print('passed')
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 8])
    test_function([[6, 7, 8, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 10])

    #ALL edge cases
    test_function([[1,0], 10])
    test_function([[1,0], 1])
    test_function([[1,0], 0])
    test_function([[1], 0])
    test_function([[0], 0])
    test_function([[], 0])
