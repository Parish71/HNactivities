# test_bank.py

import bank
import pytest

def test_starts_with_hello():
    assert bank.value("hello world") == 0
    assert bank.value("HELLO world") == 0
    assert bank.value("hello") == 0
    assert bank.value("HELLO") == 0

def test_starts_with_h():
    assert bank.value("hi there") == 20
    assert bank.value("HOLA") == 20

def test_otherwise():
    assert bank.value("goodbye") == 100
    assert bank.value("123") == 100
    assert bank.value("  something") == 100

if __name__ == "__main__":
    pytest.main()
