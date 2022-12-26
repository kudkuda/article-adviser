# article-adviser
A simple function that suggests possible amendments for English sentences with missing articles before noun phrases.

`article-adviser` uses `spacy` and in particular its `en_core_web_lg` model so to start you'll need to run:  

````
pip install -r requirements.txt
python -m spacy download en_core_web_lg
````

Once you've got all the requirements in place, you should be able to simply run
````
pytest
````
in this folder, and get the idea of the particular cases `article-adviser` can help with.

## How it works

`article-adviser` is a function that takes a string containing the text of one sentence as an argument.
It only works with noun phrases, so it iterates over "noun chunks" that `spacy` extracted from the text of a given sentence.

If a particular noun phrase already has an article or some other element that functions as a determiner (e.g. a possessive pronoun) or it is a proper noun then no further action is needed. Otherwise, `article-adviser` checks the syntactic context and lexical content of a noun phrase in order to suggest which article can be used with it. 

`article-adviser` returns an array of strings which are possible variants of the original sentence with added articles.

## Set of rules explained

The following rules attempt to cover only a small subset of possible contexts where articles can be used. The order of the rules is important.

### I. General syntactic rules

I.1. `_the_ AdjSup X`

A noun phrase with superlative adjective as a modifier requires a definite article.

Examples:

    'In _the_ greatest city in the world',
    'I am _the_ greatest man'

I.2. `_the_ X + RelClause`

A noun phrase heading a finite relative clause requires a definite article.

Examples:


    'He is _the_ actor we saw yesterday.',
    'What was _the_ last book that you loved',
    'What is _the_ title of that poem we read last week?'


### II. Specific lexical rules


II.1. `_the_ first/same/other/main... X`

Certain adjective modifiers tend to be used with a definite article.


    '_The_ main part is fantastic.',
    'We passed _the_ same exam',
    'Yuri Gagarin was _the_ first person in space.',


II.2. `_the_ X <when there's only one X>`

A definite article is required with nouns denoting unique objects.

    'Now _the_ sun is shining and there aren\'t any clouds in _the_ sky.',


II.3. `all of _the_ Xs`

`all of` is normally used with plural nouns with determiners.

    'All of _the_ students were present.',
    'All of _the_ possible directories either do not exist or are readonly.'

II.4. `be __ part of`

Normally no article is used in the expression `be part of`.

    'He was part of a group of students',


### III. Other rules

III.1. `_the_ X of/for the Y`

A noun phrase with a dependent prepositional phrase heading a definite noun phrase requires a definite article.


    'They crossed _the_ borders of Ukraine.',
    'They crossed _the_ borders of the sovereign state.',
    'They crossed _the_ borders of their state.',


III.2. `__ X <when X is uncountable>`

All the remaining rules do not apply to uncountable nouns.

    'Time is money',
    'Sugar is bad for you',
    'He showed great bravery.,
    'Would you like milk with your cookies?',


III.3. `there is _a_ X`


An indefinite article is used after `there is` or `there are`.

    'There was _a_ spider in my shoe.',
    'There was _a_ girl on the bus.',


III.4. `a/the Adj X`

Noun phrases with preposed adjectival or nominal modifiers require an indefinite article when used as part of a predicate.

    'My father is _a_ police officer.',
    'She is _a_ talented coach.',

Same noun phrases used in other syntactic contexts may require either an indefinite or a definite article depending on the context.

    'Let’s look at _an_ int array closer' or 'Let’s look at _the_ int array closer',
    'Volunteers help at _a_ food bank' or 'Volunteers help at _the_ food bank',

At the same time, certain adjective modifiers require the use of an indefinite article.

    'I bought _a_ new TV set yesterday.',
    'He has _a_ good idea.',

III.5. `it is _a/the_ X`

Singular nouns used as a part of a predicate or as a subject or a direct object can be used with an indefinite or a definite article depending on the context.

    'He is _an_ actor.' or 'He is _the_ actor.',
    '_A_ girl came to me' or '_The_ girl came to me',
    'I met _a_ girl' or 'I met _the_ girl',
