class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        cur_sum = 0 

        for i in range(k):
            cur_sum += nums[i]


        max_sum = cur_sum 

        for i in range(k, n):
            cur_sum += nums[i]
            cur_sum -= nums[i-k]
            
            if cur_sum > max_sum:
                max_sum = cur_sum

        return float(max_sum) / k
