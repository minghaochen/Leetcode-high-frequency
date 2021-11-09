# https://leetcode-cn.com/problems/count-number-of-nice-subarrays/
# 前缀和
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre_sum, ans = 0, 0
        count = [0]*(n+1)
        count[0] = 1
        for i in range(n):
            if nums[i]%2 == 1:
                pre_sum += 1
            if pre_sum >= k:
                ans += count[pre_sum-k]
            count[pre_sum] += 1
        return ans