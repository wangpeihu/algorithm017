class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        size_tasks = len(tasks)
        if size_tasks == 0:
            return 0
        '''
        flag = 0
        map = [0] * 26
        for item in tasks:
            map[ord(item) - ord('A')] += 1
        map.sort()
        for i in range(1, 26):
            if map[25 - i] == map[25]:
                continue
            else:
                flag = i
                break
        maxval = map[25] - 1

        if flag == 0:
            empty_pod = maxval * n
        else:
            empty_pod = maxval * (n - flag + 1)

        for i in range(flag, 26):
            empty_pod -= map[25 - i]
        return empty_pod + size_tasks if empty_pod > 0 else size_tasks
        '''
        map = [0] * 26
        for item in tasks:
            map[ord(item) - ord('A')] += 1
        map.sort()
        maxval = map[25] - 1
        empty_pod = maxval * n
        
        for i in range(1, 26):
            if map[25 - i] > 0:
                empty_pod -= min(maxval, map[25 - i])

        return empty_pod + size_tasks if empty_pod > 0 else size_tasks