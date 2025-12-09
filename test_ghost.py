from ghost import Ghost

def test_ghost_initial_position():
    g = Ghost(1, 2)
    assert g.x == 1
    assert g.y == 2
