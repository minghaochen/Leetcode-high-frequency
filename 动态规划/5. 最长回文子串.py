# https://leetcode-cn.com/problems/longest-palindromic-substring/
# 动态规划

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        
        dp = [[False]*n for i in range(n)]
        for i in range(n):
            dp[i][i] = True
        max_L = 1
        begin = 0
        for L in range(2,n+1): # 子串长度
            for left in range(0,n): # 子串左边界

                right = left + L - 1
                if right >= n:
                    break
                
                if s[left] != s[right]:
                    dp[left][right] == False
                else:
                    if right - left == 1:
                        dp[left][right] = True
                    else:
                        dp[left][right] = dp[left+1][right-1]
                    if dp[left][right] and right - left + 1 >= max_L:
                        # print(max_L)
                        max_L = right-left+1
                        begin = left
        
        return s[begin:begin+max_L]