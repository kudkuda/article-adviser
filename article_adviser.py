import spacy

from uncountable_nouns_list import UNCOUNTABLE_NOUNS_LIST
from a_an_exceptions import an_with_h_exceptions, a_with_vowel_exceptions

nlp = spacy.load("en_core_web_lg")


class ArticleReplace:
    # A class containing information on the position and the type of missing article

    def __init__(self, text, lower_next_char):
        self.text = text
        self.lower_next_char = lower_next_char

    def apply(self, curr_char):
        next_char = curr_char if not self.lower_next_char else curr_char.lower()
        return self.text + next_char


def generate_the(np_root):
    return ArticleReplace(capitalize_at_start('the ', np_root), should_lower_next_word(np_root))


def generate_a(np_root):
    res = choose_a_an(np_root.left_edge.text)
    return ArticleReplace(capitalize_at_start(res, np_root), should_lower_next_word(np_root))


def capitalize_at_start(string, np_root):
    if np_root.left_edge.is_sent_start:
        return string.capitalize()
    return string


def choose_a_an(text):
    if text.lower() in an_with_h_exceptions or text[0].lower() in ['a', 'e', 'i', 'o',
                                                                   'u'] and text.lower() not in a_with_vowel_exceptions:
        return 'an '
    return 'a '


def should_lower_next_word(np_root):
    # if we insert an article on sentence start we may need to lower the first character of the next token
    first_token = np_root.left_edge
    return first_token.pos_ != 'PROPN' and first_token.is_sent_start and not first_token.is_upper


def may_require_an_article(np_root):
    first_token = np_root.left_edge
    if first_token.pos_ in ['PRON', 'DET', 'NUM'] or np_root.pos_ == 'PROPN':
        return False
    return True


def is_definite(np_root):
    first_token = np_root.left_edge
    if first_token.pos_ == 'DET' and first_token.morph.get('Definite') != ['Ind']:
        return True
    if (first_token != np_root and first_token.pos_ in ['PRON', 'NUM']) or np_root.pos_ == 'PROPN':
        return True
    return False


def article_adviser(sentence):
    doc = nlp(sentence)
    articles = {}

    # we iterate over the noun phrases found in the sentence
    for np in doc.noun_chunks:
        root = np.root

        # if noun phrase already has other determiners or is headed by a proper noun, we skip it
        if not may_require_an_article(root):
            continue

        first_token = root.left_edge
        offset = np.start_char

        corrections = []

        # Rules for generating article suggestions (the order is important)
        # I. General syntactic rules
        # 1. _the_ AdjSup X
        if first_token.morph.get('Degree') == ['Sup']:
            corrections.append(generate_the(root))
        # 2. _the_ X +RelClause
        elif any(child.dep_ == 'relcl' and child.morph.get('VerbForm') != ['Inf'] for child in root.children):
            corrections.append(generate_the(root))

        # II. Specific lexical rules
        # 1. _the_ first/same/other/main... X
        elif root != first_token and first_token.text.lower() in ['first', 'second', 'same', 'other', 'main', 'primary',
                                                                  'last', 'next', 'previous', 'current', 'only']:
            corrections.append(generate_the(root))
        # 2. _the_ X <when there's only one X>
        elif root == first_token and root.text.lower() in ['sun', 'sky', 'internet', 'truth', 'sea', 'ocean',
                                                           'world', 'future']:
            corrections.append(generate_the(root))
        # 3. all of _the_ Xs
        elif root.head.text.lower() == 'of' and root.head.head.lemma_ == 'all' and root.morph.get('Number') == [
                'Plur']:
            corrections.append(generate_the(root))
        # 4. be __ part of
        elif root.text.lower() in ['part'] and root.dep_ == 'attr' and any(
                child.text.lower() == 'of' for child in root.children):
            continue

        # III. Other rules
        # 1. _the_ X of/for Y <where Y is definite>
        elif any(child.text.lower() in ['of', 'for'] and
                 any(is_definite(grandchild) for grandchild in child.children) for child in root.children):
            corrections.append(generate_the(root))
        # 2. __ X <when X is uncountable>
        elif root.text.lower() in UNCOUNTABLE_NOUNS_LIST:
            continue
        # 3. there is _a_ X
        elif any(child.text.lower() in ['there'] for child in root.head.children) and root.morph.get('Number') == [
                'Sing']:
            corrections.append(generate_a(root))
        # 4. _a/the_ Adj X
        elif root != first_token and first_token.dep_ in ['amod', 'compound'] and root.morph.get('Number') == ['Sing']:
            if root.dep_ == 'attr' or first_token.text.lower() in ['good', 'bad', 'new', 'beautiful', 'old', 'ugly',
                                                                   'nice', 'incredible', 'great']:
                # it is _a_ Adj X
                corrections.append(generate_a(root))
            else:
                # _a/the_ Adj X
                corrections.extend([generate_a(root), generate_the(root)])
        # 5. _a/the_ X <when X is a singular noun used as part of a predicate or a subject or direct object>
        elif root == first_token and root.dep_ in ['attr', 'nsubj', 'dobj'] and root.morph.get('Number') == ['Sing']:
            corrections.extend([generate_a(root), generate_the(root)])
        else:
            continue

        articles[offset] = corrections

    res = []

    # if we came up with no article suggestions, the function returns an empty array
    if len(articles.keys()) == 0:
        return res

    res.append('')

    # we iterate over the characters of the original string and apply articles where necessary
    #
    # if several variants of article use are appropriate, multiple strings with all combinations are generated
    for ind, char in enumerate(sentence):
        if articles.get(ind):
            new_res = []
            for article_variant in articles[ind]:
                new_res += list(map(lambda x: x + article_variant.apply(sentence[ind]), res))
            res = new_res
        else:
            res = list(map(lambda x: x + sentence[ind], res))

    return res
