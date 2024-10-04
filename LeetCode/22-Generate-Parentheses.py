class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        outputs = []

        def backtrack(count, str):
            if len(str) == n*2:
                outputs.append(str)
                return
            
            if count != n:
                backtrack(count + 1, str + '(')
            if count*2 != len(str):
                backtrack(count, str + ')')

        backtrack(1, '(')

        return outputs