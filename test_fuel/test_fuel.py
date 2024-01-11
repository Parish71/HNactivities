import fuel
import pytest

def main():
    test_convert()
    test_gauge()

def test_convert():

    # Test valid inputs
    assert fuel.convert("3/4") == 75
    assert fuel.convert("1/2") == 50
    assert fuel.convert("2/5") == 40

    # Test invalid inputs
    with pytest.raises(ZeroDivisionError):
        fuel.convert("3/0")  # ZeroDivisionError should be raised

    with pytest.raises(ValueError):
        fuel.convert("cat/dog")  # ValueError should be raised

    with pytest.raises(ValueError):
        fuel.convert("5/3")  # ValueError should be raised (X > Y)

def test_gauge():

    # Test percentage values for "E"
    assert fuel.gauge(0) == 'E'
    assert fuel.gauge(1) == 'E'
    assert fuel.gauge(25) != 'E'

    # Test percentage values for "F"
    assert fuel.gauge(99) == 'F'
    assert fuel.gauge(100) == 'F'
    assert fuel.gauge(75) != 'F'

    # Test values in between for percentage format
    assert fuel.gauge(50) == '50%'
    assert fuel.gauge(30) == '30%'
    assert fuel.gauge(80) == '80%'



if __name__ == "__main__":
    main()
