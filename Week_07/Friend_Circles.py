class Solution:
    def __init__(self):
        '''
        初始化变量
        '''
        self.tree_num = 0  # 连通集个数
        self.tree_node = []  # 根节点所在树的节点总数，被合并的树停止更新
        self.parent = []  # 每个节点的父亲节点

    def initialize_tree(self, total_node):
        '''
        初始化所有节点树
        '''
        #total_node为节点总数,是一个数值
        self.tree_num = total_node
        self.tree_node = [1] * total_node
        self.parent = [i for i in range(total_node)]

    def union(self, node_i, node_j):
        '''
        合并集合的函数
        '''
        root_i = self.find(node_i)
        root_j = self.find(node_j)
        #将规模小的树添加到规模大的树上
        if root_i == root_j:
            return
        if self.tree_node[root_i] > self.tree_node[node_j]:
            self.parent[root_j] = root_i
            self.tree_node[root_i] += self.tree_node[root_j]
        else:
            self.parent[root_i] = root_j
            self.tree_node[root_j] += self.tree_node[root_i]
        self.tree_num -= 1

    def find(self, node):
        '''
        查找节点的根
        '''
        #路径压缩
        while self.parent[node] != node:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def findCircleNum(self, M: List[List[int]]) -> int:
        '''
        连通集个数
        '''
        self.initialize_tree(len(M))
        for i in range(len(M)):
            for j in range(i):
                if M[i][j] == 1:
                    self.union(i, j)
        return self.tree_num
