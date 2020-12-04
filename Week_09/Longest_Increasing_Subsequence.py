class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        size_nums = len(nums)
        if size_nums < 2:
            return size_nums
        
        dp = [1] * size_nums
        for i in range(1, size_nums):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
        '''
        size_nums = len(nums)
        if size_nums < 2:
            return size_nums
        
        tail = [nums[0]]
        for i in range(1, size_nums):
            #先看看能不能加到tail的最后
            if nums[i] > tail[-1]:
                tail.append(nums[i])
                continue
  
            #二分查找
            left = 0
            right = len(tail) - 1
            while left < right:
                mid = (left + right) >> 1
                if tail[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid

            tail[left] = nums[i]

        return len(tail)