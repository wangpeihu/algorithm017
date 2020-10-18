class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        #第一种方法：python库函数itertools实现
        return list(itertools.permutations(nums))
        '''
        '''
        #第二种方法：不使用标记的回溯方法
        res = []
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp[:])
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])

        backtrack(nums, [])
        return res
        '''
        '''
        #第三种方法：使用标记的回溯方法
        k = len(nums)
        if k == 0:
            return []
        path = []
        res = []
        used = [False for _ in range(k)]
        def backtrack(nums, path, res):
            if len(path) == k:
                res.append(path[:])
                return 

            for i in range(k):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtrack(nums, path, res)
                    used[i] = False
                    path.pop()

        backtrack(nums, path, res)
        return res
        '''




'''
if __name__ == '__main__':
    nums = [1, 2, 3]
    solution = Solution()
    res = solution.permute(nums)
    print(res)
'''