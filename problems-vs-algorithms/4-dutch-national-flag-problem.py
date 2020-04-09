def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    arr = input_list[:]
    index_0 = 0 #Index to place zeros
    index_2 =len(arr)-1 #Index to place twos
    front_index = 0

    # Every time a 0(2) is fount is it moved to the beggining (end)
    while front_index <= index_2:
        if arr[front_index] == 0:
            arr[front_index] = arr[index_0]
            arr[index_0] = 0
            index_0+=1
            front_index+=1
        elif arr[front_index] == 2:
            arr[front_index] = arr[index_2]
            arr[index_2] = 2
            index_2-=1
        else:
            front_index+=1
    return arr

if __name__ == '__main__':

    def test_function(test_case):
        sorted_array = sort_012(test_case)
        assert sorted_array == sorted(test_case)


    test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
    test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
    test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

    #test edge cases
    test_function([0])
    test_function([1,0])
    test_function([2,0])
    test_function([2,1])
    test_function([1,2])
    test_function([])

    print('All test cases passed')
