class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        output = []
        def backtrack(path, used):
            if len(path) == len(nums):
                output.append(path[:])
                return

            for i, num in enumerate(nums):
                if not used[i]:
                    path.append(num)
                    used[i] = True
                    backtrack(path, used)
                    path.pop()
                    used[i] = False

        backtrack([], [False] * len(nums))
        return output