from solution_d0007 import solution01, solution02, solution03

def test_solution01():
    assert solution01('111') == 3
    assert solution01('1112') == 5
    assert solution01('11123') == 8
    assert solution01('111213') == 13

    assert solution01('141') == 2
    assert solution01('111234') == 8
    assert solution01('71524131') == 8
    assert solution01('101') == 1

def test_solution02():
    assert solution02('111') == 3
    assert solution02('1112') == 5
    assert solution02('11123') == 8
    assert solution02('111213') == 13

    assert solution02('141') == 2
    assert solution02('111234') == 8
    assert solution02('71524131') == 8
    assert solution02('101') == 1

def test_solution03():
    assert solution03('111') == 3
    assert solution03('1112') == 5
    assert solution03('11123') == 8
    assert solution03('111213') == 13

    assert solution03('141') == 2
    assert solution03('111234') == 8
    assert solution03('71524131') == 8
    assert solution03('101') == 1