"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:
    def wordFinder(self):
        file = open('words.txt', 'r')
        read_file = []
        for line in file:
            read_file.append([line.strip('\n')])
        return choice(read_file)
