"""
Obviously pretty easy if you know the beta...

Hard part here is recognizing that this is a fib sequence

Bottom up DP is pretty straightforward -> really like memo for problems like this more intuitive that top down

Time complexity: O(n) -> we are iterating through the entire list once
Space complexity: O(n) -> we are storing the entire list in the memo
"""


class Solution:
    def climbStairs(self, n: int) -> int:

        memo = [0]*(n+1)
        memo[0] = memo[1] = 1

        for i in range(2,n+1):
            memo[i] = memo[i-1] + memo[i-2]
        
        print(memo)
        return memo[n]
