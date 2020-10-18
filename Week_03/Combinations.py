class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        '''
        #第一种方法
        #先生成数
        nums = [i for i in range(1, n + 1)]
        #存储结果的列表
        res = []

        def backtrack(nums_c, cur_res, index):
            #cur_res代表res中的元素
            if len(cur_res) == k:
                #print(cur_res)
                res.append(cur_res[:])
                #print(res)
                return 

            for i in range(index, n - k + 2):
                cur_res.append(nums[i])
                backtrack(nums_c[index:], cur_res, i + 1)
                cur_res.pop()

        if k == 0 or n == 0:
            return []
        backtrack(nums, [], 0)

        return res
        '''
        '''
        #第二种方法：python库函数实现
        return list(itertools.combinations(range(1, n + 1), k))
        '''
        
        #第三种方法：根据java版本对应的方法
        res = []
        if k <= 0 or n == 0 or n < k:
            return res
        path = []
        def dfs(begin, path, res):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(begin, n + 2 - k + len(path)):
                path.append(i)
                dfs(i + 1, path, res)
                path.pop()
        dfs(1, path, res)
        return res