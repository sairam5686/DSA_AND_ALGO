# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def depth_finder(root):
    if(not root):
        return 0
    left_tree = depth_finder(root.left)
    right_tree = depth_finder(root.right)
    return 1+(max(left_tree, right_tree))

class Solution(object):
    def maxDepth(self, root):
        max_dept = depth_finder(root)
        return max_dept
        