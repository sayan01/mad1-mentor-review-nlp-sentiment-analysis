# Sentiment Analysis of MAD1 Project Mentor Reviews

This repo is to house the small scripts used to perform NLP Sentiment Analysis on
the reviews of Appdev1 Project Mentees to analyze the overall sentiment.

## Running

Install `nltk` and `textblob` to run the code.

```
. ./venv/bin/activate
pip install -r requirements.txt
```

Then run the `porterstemmer.py` file.

```
python porterstemmer.py
```

## Output as of 17 Aug:

```
Enter the path to the text file(review):
Enter common words file path(common):
Top Frequently used Words in Reviews
-------------------------------
help: 15
project: 11
mentor: 10
session: 6
doubt: 6
time: 6
onli: 5
realli: 5
wa: 5
mani: 5
Sentiment Analysis Summary:
-------------------------------
Happy reviews: 13
Angry reviews: 0
```
