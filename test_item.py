from item import Item


def test_item_has_correct_type():
    i = Item("dot", 3, 4)
    assert i.kind == "dot"
    assert i.x == 3
    assert i.y == 4
