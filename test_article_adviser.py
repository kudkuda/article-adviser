from article_adviser import article_adviser


# I.1
# _the_ AdjSup X
i_1_cases = {
    'In greatest city in world': ['In the greatest city in the world'],
    'I am greatest man': ['I am the greatest man'],
}

# I.2
# _the_ X + RelClause
i_2_cases = {
    'He is actor we saw yesterday.': ['He is the actor we saw yesterday.'],
    'That is world we live in.': ['That is the world we live in.'],
    'I found purse that I had lost.': ['I found the purse that I had lost.'],
    'What was last book that you loved': ['What was the last book that you loved'],
    'What is title of that poem we read last week ?': ['What is the title of that poem we read last week ?'],
    'They delivered new flat screen TV I ordered last week':  ['They delivered the new flat screen TV I ordered last '
                                                               'week'], 
}

# I.3
# all of _the_ Xs
i_3_cases = {
    'All of students were present.': ['All of the students were present.'],
    'All of possible directories either do not exist or are readonly.': ['All of the possible directories either do '
                                                                         'not exist or are readonly.'],
}

# I.4
# _the_ X of/for Y <where Y is definite>
i_4_cases = {
    'They crossed borders of Ukraine.': ['They crossed the borders of Ukraine.'],
    'They crossed border of Ukraine.': ['They crossed the border of Ukraine.'],
    'They crossed border of the sovereign state.': ['They crossed the border of the sovereign state.'],
    'I am son of my mother.': ['I am the son of my mother.'],
    'They have not revealed full extent of their casualties.': ['They have not revealed the full extent of their '
                                                                'casualties.'],
    'I wrote her number on back of this sheet.': ['I wrote her number on the back of this sheet.'],
    'Do you know answer for this question?': ['Do you know the answer for this question?'],
    'Do you know answer for the question?': ['Do you know the answer for the question?'],
    'Do you know answer for my question?': ['Do you know the answer for my question?'],
}

# II.1
# _the_ first/same/other/main... X
ii_1_cases = {
    'Main part is fantastic.': ['The main part is fantastic.'],
    'We passed same exam': ['We passed the same exam'],
    'Yuri Gagarin was first person in space.': ['Yuri Gagarin was the first person in space.'],
}

# II.2
# _the_ X <when there's only one X>
ii_2_cases = {
    'Now sun is shining and there aren\'t any clouds in sky.': [
        'Now the sun is shining and there aren\'t any clouds in the sky.'],
}

# II.3
# __ X <when X is uncountable>
ii_3_cases = {
    'Time is money': [],
    'Sugar is bad for you': [],
    'He showed great bravery.': [],
    'Would you like milk with your cookies?': [],
}

# II.4
# a good/bad/new _X_
ii_4_cases = {
    'I bought new TV set yesterday.': ['I bought a new TV set yesterday.'],
    'He has good idea.': ['He has a good idea.'],
    'That was incredible story!': ['That was an incredible story!'],
    'It’s beautiful city': ['It’s a beautiful city'],
    'I\'m looking for new job.': ['I\'m looking for a new job.'],
    'That would be good place for me.': ['That would be a good place for me.'],
}


# III.1
# there is _a_ X
iii_1_cases = {
    'There was spider in my shoe.': ['There was a spider in my shoe.'],
    'There was girl on the bus.': ['There was a girl on the bus.'],
    'There were documents on the table': [],
}

# III.2
# a/the Adj X
iii_2_cases = {
    'My father is police officer.': ['My father is a police officer.'],
    'She is talented coach.': ['She is a talented coach.'],
    'Let’s look at int array closer': ['Let’s look at an int array closer', 'Let’s look at the int array closer'],
    'Volunteers help at food bank': ['Volunteers help at a food bank', 'Volunteers help at the food bank'],
}

# III.3
# _a/the_ X <when X is a singular noun used as part of a predicate or a subject or direct object>
iii_3_cases = {
    'He is actor.': ['He is an actor.', 'He is the actor.'],
    'Girl came to me': ['A girl came to me', 'The girl came to me'],
    'I met girl': ['I met a girl', 'I met the girl'],
}

no_article_cases = {
    #'He was part of a group of students',
    'She is coming by plane.',
    'He is always there at night.',
    'He goes to work when I go home.',
    'I’m going to Spain for my holidays.',
    'I am my mother\'s son',
    'I like this actor',
    'I’ve seen my favourite actor today!',
    'This is my house.',
    'I have one sister.',
    'I have homework to do for tomorrow.',
    'I am crazy about reading history books.',
    'Everybody knows that cats are very independent animals.',
}


def test_i_1():
    for sent in i_1_cases.keys():
        assert article_adviser(sent) == i_1_cases[sent]


def test_i_2():
    for sent in i_2_cases.keys():
        assert article_adviser(sent) == i_2_cases[sent]


def test_i_3():
    for sent in i_3_cases.keys():
        assert article_adviser(sent) == i_3_cases[sent]


def test_i_4():
    for sent in i_4_cases.keys():
        assert article_adviser(sent) == i_4_cases[sent]


def test_ii_1():
    for sent in ii_1_cases.keys():
        assert article_adviser(sent) == ii_1_cases[sent]


def test_ii_2():
    for sent in ii_2_cases.keys():
        assert article_adviser(sent) == ii_2_cases[sent]


def test_ii_3():
    for sent in ii_3_cases.keys():
        assert article_adviser(sent) == ii_3_cases[sent]


def test_ii_4():
    for sent in ii_4_cases.keys():
        assert article_adviser(sent) == ii_4_cases[sent]


def test_iii_1():
    for sent in iii_1_cases.keys():
        assert article_adviser(sent) == iii_1_cases[sent]


def test_iii_2():
    for sent in iii_2_cases.keys():
        assert article_adviser(sent) == iii_2_cases[sent]


def test_iii_3():
    for sent in iii_3_cases.keys():
        assert article_adviser(sent) == iii_3_cases[sent]


def test_no_article():
    for sent in no_article_cases:
        assert article_adviser(sent) == []
