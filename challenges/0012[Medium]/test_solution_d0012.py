from solution_d0012 import solution01, solution02, solution03

def test_solution01():
    assert solution01(4) == 5
    assert solution01(5) == 8
    assert solution01(6) == 13

def test_solution02():
    assert solution02(4) == 5
    assert solution02(5) == 8
    assert solution02(6) == 13

def test_solution03():
    assert solution03(4, {1, 3, 5}) == 3