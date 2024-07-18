from bai9 import Grade


def test1():
    assert Grade(11) == 'I'


def test2():
    assert Grade(10) == 'A'


def test3():
    assert Grade(8) == 'B'


def test4():
    assert Grade(6.5) == 'C'


def test5():
    assert Grade(5) == 'D'


def test6():
    assert Grade(4) == 'F'
