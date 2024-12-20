from solution_d0007 import solution01

def test_solution01():
    assert solution01('111') == 3
    assert solution01('1112') == 5
    assert solution01('11123') == 8
    assert solution01('111213') == 13

    assert solution01('141') == 2
    assert solution01('111234') == 8
    assert solution01('71524131') == 8