class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Create dp table
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        
        # Fill dp table
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = dp[i][j-1]
                    
        return dp[len(s)][len(t)] == len(s)