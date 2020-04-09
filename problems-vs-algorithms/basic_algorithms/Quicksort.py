class Quicksort(object):
    def sortArray(self, nums):
        return self.quick_sort(nums)

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
