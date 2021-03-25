# Movie-Recommendation
#### Sentiment Analysis using Text

    Get sentence or paragraph from user for movie review.
    Determine the sentiment from the words.
    Problem Category: Natural Language Processing
    Models:
    Dataset: Kaggle

#### Requirements for the sentimental analysis Step by Step

 Tokenizing sentences to break text down into sentences, words, or other units
 Removing stop words like “if,” “but,” “or,” and so on
Normalizing words by condensing all forms of a word into a single form
Vectorizing text by turning the text into a numerical representation for consumption by your classifier

#### Adding packages to requirements.txt
    pip freeze > requirements.txt

### Installing requirements for spacy
    pip install nltk

    pip install spacy==2.3.5
    
    pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.3.1/en_core_web_sm-2.3.1.tar.gz
    
    pip install pyresparser
