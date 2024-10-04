class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        results = []

        def backtrack(used: list, lower):
            sum_of_used = sum(used)
            if sum_of_used == target:
                results.append(used)
                return
            
            for index, candidate in enumerate(candidates[lower:]):
                if sum_of_used + candidate <= target:
                    backtrack(used + [candidate], lower + index)

        backtrack([], 0)

        return results