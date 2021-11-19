# https://leetcode-cn.com/problems/subarray-sum-equals-k/
# 前缀和

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 记录 "前缀和" (从0到i的前缀和) 的 值和出现的次数.
        pre_sum = collections.defaultdict(int) 
        # 初始化 前缀和 为 0 的 子序列 出现了 一次. 
        pre_sum[0] = 1  
        # 记录 当前 位置的 前缀和
        cur_pre_sum = 0
        # 用于记录结果
        res = 0
        for i in range(len(nums)):
            cur_pre_sum += nums[i]  # 计算 当前位置的 前缀和
            # cur_sum - k 是我们想找的前缀和 nums[0..j]
            green_sum = cur_pre_sum - k
            if green_sum in pre_sum:
                res += pre_sum[green_sum]
            # 每次计算都将前缀和加入字典
            pre_sum[cur_pre_sum] += 1
        return res