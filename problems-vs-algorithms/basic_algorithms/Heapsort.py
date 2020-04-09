class Heapsort(object):
    def sortArray(self, nums):
        return self.heapsort(nums)

    def heapsort(self,arr):

        n = len(arr)

        # Build a maxheap.
        for i in range(n, -1, -1):
            self.downheapify(arr, n, i)

        # One by one extract elements
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i] # swap
            self.downheapify(arr, i, 0)
        return arr


    def downheapify(self, arr, n, i):

        # consider current index as largest
        largest_index = i
        left_node = 2 * i + 1
        right_node = 2 * i + 2

        # compare with left child
        if left_node<n and arr[largest_index] < arr[left_node]:
            largest_index = left_node

        # compare with right child
        if right_node<n and arr[largest_index] < arr[right_node]:
            largest_index = right_node

        if largest_index != i:
            cache = arr[largest_index], arr[i]
            arr[i], arr[largest_index] = cache
            self.downheapify(arr, n, largest_index)
