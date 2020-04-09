
def binary_search(array, target):
    '''Write a function that implements the binary search algorithm using iteration
    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    start_index = 0
    end_index = len(array) - 1
    while start_index<=end_index:
        mid = (start_index+ end_index)//2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start_index=  mid+1
        else:
            end_index=  mid-1
    return -1
