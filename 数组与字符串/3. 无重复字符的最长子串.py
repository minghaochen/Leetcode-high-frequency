# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
# 左右指针一轮遍历
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        exist = set() # 哈希集合，记录每个字符是否出现过
        right = 0
        ans = 0
        for left in range(n):
            if left != 0:
                # 左指针向右移动一格，移除一个字符
                exist.remove(s[left-1]) 
            while right < n and s[right] not in exist:
                # 不断地移动右指针
                exist.add(s[right])
                right += 1
            ans = max(ans, right-left)
        return ans