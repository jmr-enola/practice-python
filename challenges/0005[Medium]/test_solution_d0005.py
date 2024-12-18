from solution_d0005 import cons, car, cdr

def test_car():
    assert car(cons(1, 2)) == 1
    assert car(cons(11, 4)) == 11
    assert car(cons(33, 12)) == 33
    assert car(cons(5, 8)) == 5
    assert car(cons(0, -1)) == 0

def test_cdr():
    assert cdr(cons(1, 2)) == 2
    assert cdr(cons(11, 4)) == 4
    assert cdr(cons(33, 12)) == 12
    assert cdr(cons(5, 8)) == 8
    assert cdr(cons(0, -1)) == -1
