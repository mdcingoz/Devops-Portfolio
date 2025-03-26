from calculator import add, multiply

def test_add():
    assert add(4, 6) == 10, "Addition failed"
    assert add(-2, 3) == 1, "Addition with negatives failed"

def test_multiply():
    assert multiply(4, 6) == 24, "Multiplication failed"
    assert multiply(0, 5) == 0, "Multiplication with zero failed"

if __name__ == "__main__":
    test_add()
    test_multiply()
    print("All tests passed!")
