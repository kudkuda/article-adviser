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
in this folder, and get the idea of the particular cases `article-adviser` is able to help with.

## How it works

`article-adviser` is a function that takes a string containing the text of one sentence as an argument.
It only works with noun phrases, so it iterates over "noun chunks" that `spacy` extracted from the text of a given sentence.

If a particular noun phrase already has an article or some other element that functions as a determiner (e.g. a possessive pronoun) or it is a proper noun then no further action is needed. Otherwise, `article-adviser` checks the syntactic context and lexical content of a noun phrase in order to suggest which article can be used with it. 

`article-adviser` returns an array of strings which are possible variants of the original sentence with added articles.