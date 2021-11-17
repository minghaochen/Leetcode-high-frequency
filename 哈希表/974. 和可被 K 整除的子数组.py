# https://leetcode-cn.com/problems/subarray-sums-divisible-by-k/
# 前缀和 + 同余定理
# (P[j]−P[i−1])modK==0 等价于  P[j] mod K == P[i-1] mod K

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        N = len(nums)
        occur = {0:1}
        ans = 0
        total = 0
        for i in range(N):
            total += nums[i]
            res = total%k 
            same = occur.get(res,0)
            ans += same
            occur[res] = same + 1

        return ans

