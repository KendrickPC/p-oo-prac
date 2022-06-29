# https://www.pythontutorial.net/python-basics/python-read-text-file/

"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """
    cat
    dog
    porcupine

    >>> wf = WordFinder("/Users/student/words.txt")
    3 words read

    >>> wf.random()
    'cat'

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'

    >>> wf.random()
    'dog'
    """
    def __init__(self, path):
        """Read words.txt and calculates how many words have been read"""
        f = open(path, 'r')
        self.words = self.parse(f)
        print(f"words read: {len(self.words)}")

    def parse(self, f):
        """parse f (file) to a list of words"""
        return [word.strip() for word in f]

    def random(self):
        """imports random library and chooses a random word from the self.words list"""
        return random.choice(self.words)
        # return self.words

# wf = WordFinder("words.txt")
# print(wf.random())

# Inherit from the WordFinder class
class SpecialWordFinder(WordFinder):
    """
    Rewriting a new parse function to deal with edge case in specialWordFinder.txt
    """
    def parse(self, f):
        # return [w.strip() for w in f if w.strip() and not w.startswith("#")]
        
        return [w.strip() for w in f if w.strip() and not w.startswith("#")]

swf = SpecialWordFinder("specialWordFinder.txt")
print(swf.random())
# print(swf.random() in ['kale', 'parsnips', 'apple', 'mango'])
# print(swf.random() in ['kale', 'parsnips', 'apple', 'mango'])
# print(swf.random() in ['kale', 'parsnips', 'apple', 'mango'])
# print(swf.random() in ['kale', 'parsnips', 'apple', 'mango'])
# print(swf.random() in ['kale', 'parsnips', 'apple', 'mango'])
# print(swf.random() in ['kale', 'parsnips', 'apple', 'mango'])