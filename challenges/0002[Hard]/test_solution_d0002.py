from solution_d0002 import solution01, solution02

def test_solution01():
    #Test Condition 1
    result = solution01([1, 2, 3, 4, 5])
    excepted = [120, 60, 40, 30, 24]
    assert result == excepted

    #Test Condition 2
    result = solution01([3, 2, 1])
    excepted = [2, 3, 6]
    assert result == excepted

def test_solution02():
    #Test Condition 1
    result = solution02([1, 2, 3, 4, 5])
    excepted = [120, 60, 40, 30, 24]
    assert result == excepted

    #Test Condition 2
    result = solution02([3, 2, 1])
    excepted = [2, 3, 6]
    assert result == excepted