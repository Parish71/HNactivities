import twttr
from twttr import shorten

def test_shorten_no_vowels():
    assert shorten("hello") == "hll"

def test_shorten_with_vowels():
    assert shorten("python") == "pythn"

def test_shorten_empty_string():
    assert shorten("") == ""

def test_shorten_all_vowels():
    assert shorten("AEIOUaeiou") == ""

def test_shorten_mixed_case():
    assert shorten("CS50") == "CS50"

def test_shorten_with_punctuation():
    with pytest.raises(SystemExit) as e:
        shorten("Hello, World!")
    assert e.value.code == 1

if __name__ == "__main__":
    pass
