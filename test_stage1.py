"""
Tests
"""

import markov
import markov_solution
import pytest
import random

def fn_exists(name):
    try:
        getattr(markov, name)
        return True
    except:
        return False

def test_initial_layout():
    """Start your function with high-level pseudocode"""
    assert fn_exists("main"), """\
Your program is missing a 'main' function. Please add it.

Before you do anything, you should produce a rough sketch of your
code, starting with your main function.

Your main function should contain your main loop:
    def main():
        some_setup()
        loop some number of times:
            read_input()
            process_input()

When you put your code in a main function, you also need to tell
python to run that function when it starts, so you should also add the
following lines to the bottom of your file:

    if __name__ == "__main__":
        main()
    """

    assert fn_exists("process_file"), """\
First, we start by doing our setup. In this case, our setup is some
sort of file processing. We roughly sketch it out by creating a
function named process_file. The signature looks like this

    process_file(str) -> ???

Right now, we don't know what the output should look like, but we'll
just place it in there to start. For now, it should return nothing and
do nothing. Remember, you can make an empty function by doing the
following:

    def fn(arg):
        pass

You should call this function right before your main loop."""


def test_basic_markov():
    assert markov.process_file("sample1.txt") == {}, """\
Here is the heart of the markov analysis. Let us assume for now that
all markov analysis uses a prefix length of two. We have provided for
you a series of incrementally complex files to test your markov
function.

The first file, 'sample1.txt' is completely empty, and should produce
an empty output.

Now is the time to decide what kind of output process_file
returns. The functionality can be stated (in non-programming terms) in
the following way:

    process_file opens a text file, analyzes the text, and returns a
    mapping of word prefix chains to their suffixes.

The only data structure we've learned so far that supports the concept
of 'mapping' one value to another is the dictionary, or hash.

If sample1.txt is an empty file, we can assume that running
process_file("sample1.txt") will produce an empty dictionary, {}.

This solidifies our interface, the signature now looks like this:

    process_file(str) -> dict

Where 'str' is the filename and 'dict' contains the Markov mappings.

Note: we do not need to specifically check that 'sample1.txt' is an
empty file. If we do our processing correctly, our function will
return an empty dictionary if there is no input. For now, it is
sufficient to blindly return an empty dictionary without actually
opening the file.
"""
    output = {("hi", "there"): ["friend."]}
    assert markov.process_file("sample2.txt") == output, """\
If you open 'sample2.txt', you will find it contains the phrase 'hi
there friend'. Aside from an empty file, this is what we call the
'degenerate case' of the input. According to our instructions, we
should use a prefix of length 2, and each prefix should map to a
suffix that contains a single word. In this case,

    hi there => friend

In the vein of choosing the right data structures, we need to think
about how to represent the prefix and the suffix.

As I've mentioned before, string manipulation is difficult. In this
case, we're working on the level of individual words, and as we'll see
later, after we've read the initial input, we won't want to worry
about splitting and rejoining strings until the very end. For now,
trust that you'll want to keep individual words of the prefixes
separated, so that means using a collection, like a list or a tuple.

    prefix example: ["hi", "there"] or ("hi", "there")

Remember, this prefix is used as the key in your mapping. Try playing
around in the console to see which one makes sense to use.

The other thing to think about is what data structure to use to hold
your suffix. In this example, the suffix is simple, there is only one
word.

However, consider this example:

    would you, could you, in a box
    would you, could you, with a fox
    would you, could you, in a house
    would you, could you, with a mouse

Notice that 'could you,' an be followed by either 'in' or 'with'. The
partial mapping might look like:

    could you, => in a, with a
    in a => box, house
    with a => fox, mouse

The suffix must then be some sort of collection as well, either a set or a tuple.

As you implement this, remember the mantra: do it first for a single
case, then figure out how to repeat it.

It will help to simply open your file, read only one line, then close
it, like this:

f = open(filename)
line = f.readline()
f.close()

Then try writing your function to process that single line.
"""

def test_shift():
    assert fn_exists("shift"), """\
Utility function: shift

As a quick aside, we need to build a function called 'shift' with
certain useful behavior. I promise that you will use this later, but
it is non-obvious right now how. Still, this is a good time to build
it.

The signature of shift looks like this:

    shift(tuple, anything) => tuple

Shift takes a tuple, removes the first element, then adds the second
argument to the end, and returns the new tuple.

    t = (1,2)
    shift(t, 3)
        => (2, 3)

'Shifting' values onto the end of a collection while removing them
from the front is a commonly used operation.

Try experimenting with adding tuples together in the console to get an
idea of how to write this function."""

    assert markov.shift((1,2), 3) == (2,3), """\
Here are more test cases to try out your shift function."""
    assert markov.shift(("cat", "in"), "the") == ("in","the"), """\
Notice the specification of 'any' type for the second argument. Shift
should work on a tuple, and any variable that can go in a tuple."""

def test_phrase_generation():
    assert fn_exists("build_sentence"), """\
Now that we've produced a super simple markov mapping, we need to
check to see if we can use it to build a phrase. We'll start by
creating a function with the following signature:

    build_sentence(dict) => str

The dictionary that it accepts is the markov mapping we produced in
our process_file function.

Notice how we are explicit about inputs and return values from our
function, and how the output of the other function is used as the
input to this one. So far, we've been using global variables to store
our intermediate values, which is considered a bad practice."""

    your_sentence = markov.build_sentence({("this", "old"): ["man."]})
    expected = "this old man."
    print "Expected sentence:", expected
    print "Your sentence:", your_sentence
    assert your_sentence == expected, """\
To produce a random sentence from a markov mapping, we choose a random
key/value pair from our map, which should look like this:

    ("word1", "word2") : ["word3"]

We then assemble the three words into a single sentence. Using 'sample2.txt':

    # after running process_file, our mapping looks like this:
    mapping = {("hi", "there"): ["friend."]}

We randomly choose one element in the dictionary, but since there is
only one, we use that and assemble the sentence.

    build_sentence(mapping)
        => "hi there friend."\
"""

def test_first_integration(capsys):
    markov.main()
    out, err = capsys.readouterr()
    assert out == "hi there friend.\n", """\
Now is the time to bring it all together. When you run your file,
markov.py from the command line

    python markov.py

It should should then try to run markov analysis and build a single
sentence from sample2.txt, outputting

    hi there friend.

You have to chain this behavior together in your main function,
calling process_file and feeding the output of that into
build_sentence, then printing the output of that."""


def test_complex_input_1():
    mapping = markov.process_file("sample3.txt")
    output = {
            ("how", "are"): ["you"],
            ("are", "you"): ["doing?"]
            }
    print "Expected map:", output
    print "Your map:", mapping
    assert mapping == output, """\
Now that we've done a full integration on our degenerate (basic) case,
we're increasing complexity. Try to improve your 'process_file'
function to process more than one prefix-suffix pair.

Remember, a prefix consists of two words, and a suffix is a single
word, so the maximum number of pairs that can be produced from three
words is one.

In general, if there are N words in the input, it should be possible
to generate N-2 pairs."""

def test_complex_input_2():
    correct_map = markov_solution.build_chains("sample4.txt", 2)
    print "Expected map:", correct_map
    new_map = markov.process_file("sample4.txt")
    print "Your map:", new_map

    assert new_map == correct_map, """\
The previous example tested a single line longer than 3 words, now
update your function to work on a multiline file.

Remember that calling string.split() with no arguments will
automatically split on all whitespace, including newlines, tabs, and
spaces."""

def test_complex_input_3():
    correct_map = markov_solution.build_chains("sample5.txt", 2)
    new_map = markov.process_file("sample5.txt")

    for key in correct_map.keys():
        print "Expected: %r => %r"%(key, correct_map[key])
        print "Received: %r => %r"%(key, new_map[key])
        assert sorted(correct_map[key]) == sorted(new_map[key]), """\
Sometimes a prefix will have more than allowable suffix, as in the
following example:

    Humpty Dumpty sat on a wall
    Humpty Dumpty had a great fall

    The prefix "Humpty Dumpty" can become either "sat" or "had".

Make sure that your processing function can produce handle that scenario.
"""
