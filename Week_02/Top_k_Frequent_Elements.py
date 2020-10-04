import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        #使用Python自带容器类型的计数器函数
        return [e[0] for e in collections.Counter(nums).most_common(k)]
        '''
        '''
        利用计数器之后，再压入堆
        dic = collections.Counter(nums)
        heap, res = [], []
        for i in dic:
            heapq.heappush(heap, (-dic[i], i))
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])

        return res
        '''
