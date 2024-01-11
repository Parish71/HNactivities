import um
import pytest

def main():
    test_count_simple()
    test_count_no_um()
    test_count_case_insensitive()
    test_count_as_whole_word()
    test_count_surrounded_by_spaces()
    test_count_part_of_word()
    test_count_empty_input()

# Test case 1: Ensure count returns the correct result for a simple case
def test_count_simple():
    assert um.count("Hello um World") == 1

# Test case 2: Ensure count returns 0 for a string without "um"
def test_count_no_um():
    assert um.count("This is a test") == 0

# Test case 3: Ensure count is case-insensitive
def test_count_case_insensitive():
    assert um.count("UM um Um") == 3

# Test case 4: Ensure count handles "um" as a whole word, not as a substring
def test_count_as_whole_word():
    assert um.count("I'm going to the museum") == 0

# Test case 5: Ensure count handles "um" surrounded by spaces
def test_count_surrounded_by_spaces():
    assert um.count(" um um um ") == 3

# Test case 6: Ensure count handles "um" as part of a larger word
def test_count_part_of_word():
    assert um.count("umbrella umbrella umbrage") == 0

# Test case 7: Ensure count handles empty input
def test_count_empty_input():
    assert um.count("") == 0

if __name__ == "__main__":
    pytest.main()
