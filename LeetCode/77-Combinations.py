class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        results = []

        def backtrack(picked, candidates):
            if len(picked) == k:
                results.append(picked)
                return

            for i in range(len(candidates)):
                num = candidates.pop(0)
                backtrack(picked + [num], candidates.copy())

        backtrack([], list(range(1, n+1)))

        return results