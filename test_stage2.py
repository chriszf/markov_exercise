"""
Tests
"""

import markov
import pytest
import random

def fn_exists(name):
    try:
        getattr(markov, name)
        return True
    except:
        return False

def test_sentence_generation():
    mapping = markov.process_file("sample3.txt")
    print mapping
    random.seed(1)
    received = markov.build_sentence(mapping)
    expected = "how are you doing?"
    print "Expected output:", expected
    print "Your output:", received
    assert expected == received, """\
Now that we've produced a complete mapping of the input file, we need to update our sentence generation function. Right now, it chooses a single random prefix and generates a phrase combined with the correct suffix.

This produces a phrase of three words, but not an entire sentence. To produce a sentence, we need to use the last two words of our phrase as a new prefix.

    # Original string: "hey there good buddy."
    mapping = { ("hey", "there"): ["good"],
                ("there", "good"): ["buddy."]) }

    If our program randomly chooses the first mapping, we will have the intermediate sentence
    
    "hey there good"

    We can then use "there" and "good" as a new prefix, which results in the final suffix "buddy."

To build a sentence, we repeat this process until we encounter a suffix that has a sentence terminator in it (. ? !).

This process will be easier if you use the shift() function we wrote earlier.
"""

def test_paragraph():
    assert fn_exists("build_paragraph"), """\
The next step is to build a function that assembles a paragraph from several random sentences. It's signature looks like this:
    
    build_paragraph(dict, int) -> str

The dict argument is a mapping produced by your process_file function.

The integer argument is the number of sentences to use to generate a paragraph. It will call your build_sentence() function several times and then join the resulting sentences together into a single string. Use the string join() function to do this.""" 

    random.seed(12345)
    mapping = markov.process_file("emma.txt")
    sentence = markov.build_paragraph(mapping, 4)
    terminators = 0
    for letter in sentence:
        if letter in "?.!":
            terminators += 1

    print "Your sentence:", sentence
    print "Expected 4 sentences, found %d"%terminators

    assert terminators >= 4, """Because the text does not consistently have a space after the end of each terminator in a sentence, your paragraph may have more than the expected number of terminators."""

def test_build_tweet():
    assert fn_exists("build_tweet"), """\
We'll build a new function, build_tweet, which mostly behaves the same as build paragraph, but tries to produce sentences less than 140 characters. The strategy here will be to produce sentences, appending them to each other as long as the complete text is less than 140 characters. For the first sentence, if it is greater than 140 characters, produce a new sentence until you create an appropriate one.

The signature for this function is

    build_tweet(dict) -> str
"""
    mapping = markov.process_file("emma.txt")
    tweet = markov.build_tweet(mapping)
    print "Your tweet:", tweet
    print "Expected: less than 140 characters, found %d"%len(tweet)
    assert len(tweet) <= 140

