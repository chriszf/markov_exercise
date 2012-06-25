import markov
import pytest

def test_cap():
    mapping = markov.process_file("emma.txt")
    for i in range(5):
        s = markov.build_sentence(mapping)
        print "Sentence generated:", s
        assert s[0] == s[0].capitalize(), """Everything's looking pretty good now, you can generate tweets and sentences and paragraphs, the last detail is that sentences are generated with a lowercase letter to start. Make sure that the first word of each sentence is capitalized properly."""
