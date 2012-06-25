"""
markov.py

Reference text: section 13.8, how to think like a computer scientist

Do markov analysis of a text and produce mimic text based off the original.

Markov analysis consists of taking a text, and producing a mapping of prefixes to suffixes. A prefix consists of one or more words, and the next word to follow the prefix in the text. Note, a prefix can have more than one suffix.

Eg: markov analysis with a prefix length of '1'

    Original text:
        "The quick brown fox jumped over the lazy dog"

        "the": ["quick", "lazy"]
        "quick": ["brown"]
        "brown": ["fox"]
        "fox": ["jumped"]
        ... etc.

With this, you can reassemble a random text similar to the original style by choosing a random prefix and one of its suffixes, then using that suffix as a prefix and repeating the process.

You will write a program that performs markov analysis on a text file, then produce random text from the analysis. The length of the markov prefixes will be adjustable, as will the length of the output produced.
""" 
