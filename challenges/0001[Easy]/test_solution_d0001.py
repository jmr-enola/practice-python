from solution_d0001 import solution01, solution02

def test_solution01():
    #Test Condition 1
    assert solution01(17, [10, 15, 3, 7]) == True

    #Test Condition 2
    assert solution01(12, [10, 15, 3, 7]) == False

    #Test Condition 3
    assert solution01(14, [10, 15, 3, 7, 7, 4]) == True

    #Test Condition 4
    assert solution01(0, [0, 15, 3, 7, 7, 4]) == False

    #Test Condition 5
    assert solution02(12, [5, 15, 3, 7, 7, 4]) == True

def test_solution02():
    #Test Condition 1
    assert solution02(17, [10, 15, 3, 7]) == True

    #Test Condition 2
    assert solution02(12, [10, 15, 3, 7]) == False

    #Test Condition 3
    assert solution02(14, [10, 15, 3, 7, 7, 4]) == True

    #Test Condition 4
    assert solution02(0, [0, 15, 3, 7, 7, 4]) == False

    #Test Condition 5
    assert solution02(12, [5, 15, 3, 7, 7, 4]) == True