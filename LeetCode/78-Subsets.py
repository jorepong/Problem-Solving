class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        outputs = []

        def backtrack(front, path):
            outputs.append(path[:])
            if front == len(nums):
                return

            for i in range(front+1, len(nums) + 1):
                path.append(nums[i-1])
                backtrack(i, path)
                path.pop()
        
        backtrack(0, [])

        return outputs