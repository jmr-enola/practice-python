'''
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
'''

class Node:
    
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node: Node) -> str:

    if (node == None):
        return "None, "
    
    string = node.val + ", " + serialize(node.left) + serialize(node.right)
    
    # if (node.left != None):
    #     string += ", " + serialize(node.left)

    # if (node.right != None):
    #     string += ", " + serialize(node.right)
    
    return string

def deserialize(serialized: str) -> Node:
    node = None
    nodes = serialized.split(", ")

    def helper(vals: list):

        if len(vals) <= 0:
            return None
        
        if vals[0] == 'None':
            vals.pop(0)
            return None
        
        node = Node(vals.pop(0))
        node.left = helper(vals)
        node.right = helper(vals)    

        return node
    
    node = helper(nodes)
    return node