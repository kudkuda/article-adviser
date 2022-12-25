from article_adviser import choose_a_an

nouns_on_consonant_cases = [
    'beaver',
    'cat',
    'dog',
    'pig',
    'Sheep',
]

nouns_on_vowel_cases = [
    'egg',
    'orbit',
    'uprising',
    'apricot',
    'Indian',
]


exceptions_an_cases = [
    'honour',
    'honourable',
    'honest',
]


exceptions_a_cases = [
    'umbrella',
    'unicorn',
    'unison'
]


def test_nouns_on_consonant():
    """
    Before noun starting in a consonant article 'a' is used
    """
    for noun in nouns_on_consonant_cases:
        assert choose_a_an(noun) == 'a '


def test_nouns_on_vowel():
    """
    Before noun starting in a consonant article 'a' is used
    """
    for noun in nouns_on_vowel_cases:
        assert choose_a_an(noun) == 'an '

def test_exceptions_a():
    """
    Checking exceptions
    """
    for noun in exceptions_a_cases:
        assert choose_a_an(noun) == 'a '


def test_exceptions_an():
    """
    Checking exceptions
    """
    for noun in exceptions_an_cases:
        assert choose_a_an(noun) == 'an '