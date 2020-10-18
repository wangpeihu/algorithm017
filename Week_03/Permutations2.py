class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        '''
        #第一种方法：自己的暴力法
        size = len(nums)
        if size == 0:
            return []
        path = []
        res = []
        used = [False for _ in range(size)]
        res_set = set()
        def backtrack(nums, path, res):
            if len(path) == size:
                res_set.add(tuple(path[:]))
                return

            for i in range(size):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtrack(nums, path, res_set)
                    used[i] = False
                    path.pop()

        backtrack(nums, path, res_set)
        for item in res_set:
            res.append(item)

        return res
        '''
        '''
        #第二种方法：自己的第二种暴力法
        size = len(nums)
        if size == 0:
            return []
        path = []
        res_set = set()
        res = []
        def backtrack(nums):
            if not nums:
                res_set.add(tuple(path[:]))
                return 

            for i in range(len(nums)):
                path.append(nums[i])
                backtrack(nums[:i] + nums[i + 1:])
                path.pop()

        backtrack(nums)
        for item in res_set:
            res.append(item)
        
        return res
        '''
        '''
        #第三种方法
        size = len(nums)
        if size == 0:
            return []
        path = []
        res = []
        used = [False for _ in range(size)]
        nums.sort()

        def backtrack(nums, path):
            if len(path) == size:
                res.append(path[:])
                return

            for i in range(size):
                if not used[i]:
                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        continue
                
                    used[i] = True
                    path.append(nums[i])
                    backtrack(nums, path)
                    used[i] = False
                    path.pop()

        backtrack(nums, path)
        return res
        '''