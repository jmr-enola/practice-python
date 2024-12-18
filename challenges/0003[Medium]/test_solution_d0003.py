from solution_d0003 import Node, serialize, deserialize

def test_solution01():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'