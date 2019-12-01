from y2018.d03 import Hunk


def test_hunk():
    hunk = Hunk('#123 @ 3,2: 5x4')
    assert hunk._first_column == 3, 'start column is not identical'
    assert hunk._first_row == 2, 'start row is not identical'
    assert hunk._one_after_last_column == 8, 'end column is not identical'
    assert hunk._one_after_end_row == 6, 'end row is not identical'
    assert list(hunk.covered_cells()) == [(2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (3, 3), (3, 4), (3, 5), (3, 6),
                                          (3, 7),
                                          (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (5, 3), (5, 4), (5, 5), (5, 6),
                                          (5, 7)]
