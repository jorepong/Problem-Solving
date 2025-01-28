class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(i, j):
            if i>j:
                return -1
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binary_search(mid+1, j)
            else:
                return binary_search(i, mid-1)
        return binary_search(0, len(nums)-1)