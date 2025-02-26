class Solution:
    count = 0
    def climbStairs(self, n: int) -> int:
        stair = [1, 1]

        for i in range(2, n+1):
            stair.append(stair[i-1] + stair[i-2])

        return stair[n]