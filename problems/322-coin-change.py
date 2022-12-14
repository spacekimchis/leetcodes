class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            if dp[i] == float('inf'): continue
            if i == amount:
                return dp[i]
            for coin in coins:
                if i + coin <= amount:
                    dp[i + coin] = min(dp[i] + 1, dp[i + coin])
        return -1

