def reverse_string(s):
    """
    Reverses order or characters in string s.
    """
    return s[::-1]


def test_reverse_string():
    assert reverse_string('foobar!') == '!raboof'
    assert reverse_string('stressed') == 'desserts'


def reverse_words(s):
    """
    Reverses order or words in string s.
    """
    words = s.split()
    words_reversed = words[::-1]
    return ' '.join(words_reversed)


def test_reverse_words():
    assert reverse_words('dogs hate cats') == 'cats hate dogs'
    assert reverse_words('dog eat dog') == 'dog eat dog'
    assert reverse_words('one two three four') == 'four three two one'

