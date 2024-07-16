class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1:1,2:2}
        def dp1(n):
            if n==1 or n==2:
                return n
            else:
                for i in range(3,n+1):
                    memo[i] = memo[i-1] + memo[i-2]
                return memo[i]
        return dp1(n)
        