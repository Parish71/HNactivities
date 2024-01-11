
from plates import is_valid

def main():
    test_has_minimum_and_maximum_length()

    test_starts_with_two_letters()

    test_has_middle_numbers()

    test_starts_with_zero()

    test_has_punctuation()

def test_has_minimum_and_maximum_length():
    assert is_valid('AB') == True
    assert is_valid('H') == False
    assert is_valid('ABCDEF') == True
    assert is_valid('OUTATIME') == False

def test_starts_with_two_letters():
    assert is_valid('AB') == True
    assert is_valid('A1') == False
    assert is_valid('1A') == False
    assert is_valid('12') == False

def test_starts_with_zero():
    assert is_valid('CS50') == True
    assert is_valid('CS05') == False

def test_has_middle_numbers():
    assert is_valid('CSA512') == True
    assert is_valid('CSS50B') == False

def test_has_punctuation():
    assert is_valid('PI3.14') == False
    assert is_valid('CS!05') == False


if __name__ == "__main__":
    main()
