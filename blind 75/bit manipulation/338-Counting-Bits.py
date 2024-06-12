# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

# Example 1:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10

# Example 2:

# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101


#my sol:
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            countt = (bin(i)[2:]).count("1")
            res.append(countt)
        return res


#op sol: using dp
"""
i          ofset   dp
0 - 0000 - 0     - 0
1 - 0001 - 1     - 1 + dp[i-ofset] - dp[1-1] - dp[0] - 1
2 - 0010 - 2     - 1 + dp[i-ofset] - dp[2-2] - dp[0] - 1
3 - 0011 - 2
4 - 0100 - 4
5 - 0101 - 4
6 - 0110 - 4
7 - 0111 - 4     - 1 + dp[i-ofset] - dp[7-4] - dp[3] - 2
8 - 1000 - 8     - 1 + dp[i-ofset] - dp[8-8] - dp[0] - 1
"""
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]*(n+1)
        offset = 1
        for i in range(1,n+1):
            if offset*2 == i:
                offset = i
            dp[i] = 1+dp[i-offset]
        return dp
