import numb3rs  # Assuming numb3rs.py contains the validate function
import pytest
import sys

def main():
    test_range()
    test_format()

# Test cases for valid and invalid IPv4 address ranges
def test_range():
    # Valid IPv4 addresses within the range
    assert numb3rs.validate(r"255.255.255.255") == True
    assert numb3rs.validate(r"0.0.0.0") == True
    assert numb3rs.validate(r"1.512.1.1") == False  # Leading zeros are not allowed
    assert numb3rs.validate(r"512.0.0.1") == False  # Number exceeds 255
    assert numb3rs.validate(r"0.0.0.512") == False  # 4th Number exceeds 255

def test_format():

    assert numb3rs.validate(r"1") == False  # Incomplete address
    assert numb3rs.validate(r"1,2,3") == False  # Incomplete address
    assert numb3rs.validate(r"1.2.3") == False  # Incomplete address
    assert numb3rs.validate(r"1.2.3.4") == True  # 2nd Number exceeds 255


if __name__ == "__main__":
    main()
