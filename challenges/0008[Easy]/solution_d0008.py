'''
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \\
 1   0
    / \\
   1   0
  / \\
 1   1

'''

class Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def solution01(root: Tree) -> int:

    def helper(node: Tree) -> tuple[int, bool]:
        if not node:
            return 0, True
        
        left_count, is_left_unival = helper(node.left)
        right_count, is_right_unival = helper(node.right)
        
        if is_left_unival and is_right_unival:
            if (node.left and node.left.value == node.value) or not node.left:
                if (node.right and node.right.value == node.value) or not node.right:
                    return left_count + right_count + 1, True
        
        return left_count + right_count, False

    count, _ = helper(root)
    return count