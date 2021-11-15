# https://leetcode-cn.com/problems/product-of-array-except-self/
# 利用索引左侧所有数字的乘积和右侧所有数字的乘积（即前缀与后缀）相乘得到答案

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        res=[1]*n

        for i in range(1,n):
            res[i] = res[i-1]*nums[i-1]

        temp = 1
        for i in range(1,n):
            temp *= nums[n-i]
            res[n-1-i] *= temp
        
        return res