"""Demonstrates how to make a simple call to the Natural Language API."""

import argparse

from sys import argv
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


def print_result(annotations):
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude

    for index, sentence in enumerate(annotations.sentences):
        sentence_sentiment = sentence.sentiment.score
        print('Sentence {} has a sentiment score of {}'.format(
            index, sentence_sentiment))

    print('Overall Sentiment: score of {} with magnitude of {}'.format(
        score, magnitude))
    return 0


def analyze(movie_review_filename):
    """Run a sentiment analysis request on text within a passed filename."""
    client = language.LanguageServiceClient()

    with open(movie_review_filename, 'r') as review_file:
        # Instantiates a plain text document.
        content = review_file.read()

    document = types.Document(
        content=content,
        type=enums.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(document=document)

    score = annotations.document_sentiment.score
    # Print the results
    print_result(annotations)

    return score

def compare(score):
    if score >= initial_score:
        print("Sentiment becomes better!")
    else:
        print("Sentiment becomes worse.")

if __name__ == '__main__':
    initial_score = 0
    for i in range(len(argv)):
        if i != 0:
            score = analyze(argv[i])
            compare(score)
            initial_score = score
