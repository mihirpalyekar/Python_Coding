import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sumn = 0
        maxn = nums[0]
        for n in nums:
            sumn += n
            if sumn > maxn:
                maxn = sumn
            if sumn < 0:
                sumn = 0
        
        return maxn