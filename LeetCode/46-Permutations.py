class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        size_of_nums = len(nums)
        results = []
        
        def backtrack(output):
            if len(output) == size_of_nums:
                results.append(output)
                return
            
            for n in nums:
                if n not in output:
                    backtrack(output + [n])

        backtrack([])
        return results