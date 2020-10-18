# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        '''
        #第一种方法：递归
        if len(inorder) == 0:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        
        return root
        '''
        '''
        #第二种方法：递归
        def buildTreeHelper(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None

            preroot = pre_left
            root = TreeNode(preorder[preroot])

            #获取根节点在中序遍历列表中的下标
            inroot = index[preorder[preroot]]
            size_of_left_subtree = inroot - in_left
            #递归构造左右子树
            root.left = buildTreeHelper(pre_left + 1, pre_left + size_of_left_subtree, in_left, inroot - 1)
            root.right = buildTreeHelper(pre_left + size_of_left_subtree + 1, pre_right, inroot + 1, in_right)

            return root

        n = len(preorder)
        #字典生成式
        index = {element:i for i, element in enumerate(inorder) }
        return buildTreeHelper(0, n-1, 0, n-1)
        '''
        #第三种方法
        def build(stop):
            if inorder and inorder[-1] != stop:
                root = TreeNode(preorder.pop())
                root.left = build(root.val)
                inorder.pop()
                root.right = build(stop)
                return root

        preorder.reverse()
        inorder.reverse()
        return build(None)