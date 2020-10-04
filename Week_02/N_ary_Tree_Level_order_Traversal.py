"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
import collections


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        '''
        #第一种迭代方法
        if root is None:
            return None

        res = []
        deq = collections.deque([root])

        while deq is not None:
            level = []

            for _ in range(len(deq)):
                node = deq.popleft()
                level.append(node.val)
                deq.extend(node.children)

            res.append(level)
            
        return res
        '''
        #第二种迭代方法
        if root is None:
            return None

        res = []
        previous_layer = [root]

        while previous_layer:
            current_layer = []
            res.append([])

            for node in previous_layer:
                res[-1].append(node.val)
                current_layer.extend(node.children)
            previous_layer = current_layer

        return res
