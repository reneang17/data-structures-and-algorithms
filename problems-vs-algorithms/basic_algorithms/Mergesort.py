class Mergesort(object):
    def sortArray(self, nums):
        #return self.mergesort(nums)
        #return self.quick_sort(nums)
        return self.heapsort(nums)

    def mergesort(self, arr):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(arr)<= 1:
            return arr

        mid = len(arr)//2

        left = self.mergesort(arr[:mid])
        right = self.mergesort(arr[mid:])

        return self.merge(left, right)

    def merge(self, left, right):

        L = 0
        R = 0
        merged = []
        while L< len(left) and R < len(right):
            if left[L] <= right[R]:
                merged.append(left[L])
                L+=1
            else:
                merged.append(right[R])
                R+=1
        merged += left[L:]
        merged += right[R:]

        return merged

    def sort_a_little_bit(sefl, nums, start_index, end_index):
        left_index = start_index
        pivot_index = end_index
        pivot_value = nums[pivot_index]
        while pivot_index != left_index:
            left_value = nums[left_index]
            if left_value <= pivot_value:
                left_index+=1
                continue

            nums[left_index] = nums[pivot_index - 1]
            nums[pivot_index- 1] = pivot_value
            nums[pivot_index] = left_value
            pivot_index -= 1
        return pivot_index

    def sort_all(self, nums, start_index, end_index):
        if end_index < start_index:
            return
        pivot_index = self.sort_a_little_bit(nums, start_index, end_index)
        self.sort_all(nums, start_index, pivot_index - 1)
        self.sort_all(nums, pivot_index + 1, end_index)

    def quick_sort(self,nums):
        self.sort_all(nums,0,len(nums)-1)
        return nums


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
