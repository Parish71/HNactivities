import pytest
from working import convert

def main():
    test_valid_format_24_hour()
    test_valid_format_no_minutes()
    test_valid_hour()
    test_invalid_format()

def test_valid_format_24_hour():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('10 PM to 8 AM') == '22:00 to 08:00'
    assert convert('10:30 PM to 8:50 AM') == '22:30 to 08:50'

def test_valid_format_no_minutes():
    input_hours = '9:60 AM to 9:60 PM'
    with pytest.raises(ValueError):
        convert(input_hours)

def test_valid_hour():
    input_hours = '13 PM to 17 PM'
    with pytest.raises(ValueError):
        convert(input_hours)

def test_invalid_format():
    input_hours = '9 AM - 9PM'
    with pytest.raises(ValueError):
        convert(input_hours)

if __name__ == "__main__":
    main()
