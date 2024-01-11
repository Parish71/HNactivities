import sys
from datetime import date, datetime, timedelta
from unittest.mock import patch
import pytest
from seasons import AgeCalculator, main


def main():
    test_one_year_ago(capsys)
    test_two_years_ago(capsys)
    test_invalid_date_exit(capsys)
    test_custom_date(capsys)

def test_one_year_ago(capsys):
    birthdate = (date.today() - timedelta(days=365)).strftime("%Y-%m-%d")
    with patch('builtins.input', return_value=birthdate):
        age_calculator = AgeCalculator()
        age_calculator.display_age()
        captured = capsys.readouterr()
        assert "Five hundred twenty-five thousand, six hundred minutes" in captured.out

def test_two_years_ago(capsys):
    birthdate = (date.today() - timedelta(days=365 * 2)).strftime("%Y-%m-%d")
    with patch('builtins.input', return_value=birthdate):
        age_calculator = AgeCalculator()
        age_calculator.display_age()
        captured = capsys.readouterr()
        assert "One million, fifty-one thousand, two hundred minutes" in captured.out

def test_invalid_date_exit(capsys):
    original_stdin = sys.stdin
    sys.stdin = open("/dev/stdin", "r")
    sys.stdin.readline = lambda: "February 6th, 1998"

    try:
        AgeCalculator().display_age()
    except SystemExit as sys_exit:
        assert sys_exit.code == 1

    sys.stdin = original_stdin

    captured = capsys.readouterr()
    assert "Invalid date" in captured.out  # Change to captured.out


def test_custom_date(capsys):
    birthdate = "1970-01-01"
    with patch('builtins.input', return_value=birthdate):
        age_calculator = AgeCalculator()
        age_calculator.display_age()
        captured = capsys.readouterr()
        assert "Twenty-eight million, three hundred ninety-two thousand, four hundred eighty minutes" in captured.out

if __name__ == "__main__":
    main()
