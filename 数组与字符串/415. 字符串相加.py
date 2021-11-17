# https://leetcode-cn.com/problems/add-strings/
# 模拟加法



class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        m, n = len(num1)-1, len(num2)-1
        carry = 0
        res = ''
        while m >=0 or n >= 0:

            a = int(num1[m]) if m >=0 else 0
            b = int(num2[n]) if n >=0 else 0

            tmp = a+b+carry
            carry = tmp // 10
            res = str(tmp%10) + res

            m-=1
            n-=1
        
        return "1" + res if carry else res
