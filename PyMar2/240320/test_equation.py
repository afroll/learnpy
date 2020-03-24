import equation as e

def test_add():
    assert e.add(2,3) == 5
    assert e.add(3,3) == 6
    assert e.add(10,-10) == 0
    for i in range(0, 100):
        assert e.add(i, i) == 2*i