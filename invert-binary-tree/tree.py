class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        queue = []
        queue.append(root)
        while queue:
            first = queue.pop(0)
            if first:
                first.left, first.right = first.right, first.left
                queue.append(first.left)
                queue.append(first.right)
        return root
