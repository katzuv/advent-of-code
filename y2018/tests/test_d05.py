from y2018.d05 import do_react


def test_do_react():
    assert do_react('R', 'r')
    assert do_react('r', 'R')
    assert do_react('c', 'C')
    assert do_react('A', 'a')
    assert not do_react('R', 'R')
    assert not do_react('s', 'r')
