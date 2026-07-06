def add( x , y ):
    return x + y

def test_add():
      assert add(1,2) == 3
      assert add(5,4) == 9
      assert add(-1,-2) == -3

def test_add_big_number():
    assert add(1000000, 2000000) == 3000000
    assert add(500000, 400000) == 900000