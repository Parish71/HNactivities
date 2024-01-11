from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    assert str(jar) == "🍪🍪🍪🍪🍪"

    # Test depositing more than the capacity
    with pytest.raises(ValueError, match="Not enough space in the jar"):
        jar.deposit(10)

def test_withdraw():
    jar = Jar()
    jar.deposit(8)

    jar.withdraw(3)
    assert jar.size == 5
    assert str(jar) == "🍪🍪🍪🍪🍪"

    # Test withdrawing more than available
    with pytest.raises(ValueError, match="Not enough cookies in the jar"):
        jar.withdraw(10)
