# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        #第一种方法：递归DFS
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
        return root
        '''
        #第二种方法：递归DFS+字典
        fa = {root:None}
        def dfs(root:'TreeNode'):
            if root.left != None:
                fa[root.left] = root
                dfs(root.left)
            if root.right != None:
                fa[root.right] = root
                dfs(root.right)
        
        dfs(root)
        l1, l2 = p, q
        while l1 != l2:
            l1 = fa.get(l1, q)
            l2 = fa.get(l2, p)
        return l1