class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(i, j):
            if i<=j:
                mid = (i+j) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    return binary_search(mid+1, j)
                else:
                    return binary_search(i, mid-1)
            else:
                return -1
        
        n = nums[0]
        shift = 0
        for i in range(1, len(nums)):
            if nums[i] < n:
                shift = i
                break
            else:
                n = nums[i]
        
        nums = nums[shift:] + nums[:shift]
        result = binary_search(0, len(nums)-1)
        return -1 if result == -1 else (shift + result) % len(nums)
                    