class Solution:
    def countHousePlacements(self, n: int) -> int:
        dp = [0, 2, 3]

        for i in range(3, n+1):
            dp.append(dp[i-1] + dp[i-2])

        return (dp[n]**2) % (10**9 + 7)