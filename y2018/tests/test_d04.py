from y2018.d04 import amount_of_most_common_item_only_one


def test_amount_of_most_common_item():
    assert amount_of_most_common_item_only_one([1, 2, 2, 3, 4, 2, 5, 6, 3, 1, 2, 3, 3, 3, 2, 7]) == 5
