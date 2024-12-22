from solution_d0008 import Tree, solution01

def test_solution01():
    example_tree = Tree(0,
        left=Tree(1),
        right=Tree(0,
            left=Tree(1,
                left=Tree(1),
                right=Tree(1)
            ),
            right=Tree(0)
        )
    )

    # Test the solution
    result = solution01(example_tree)
    assert result == 5