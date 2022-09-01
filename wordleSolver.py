#!/usr/bin/python3

# Main info about the code
#Need a datastructure.

#install pylint w/ flycheck for macos

import argparse
import os
from enum import Enum
from collections import OrderedDict
parser = argparse.ArgumentParser(description='Input for Wordle Solver')

parser.add_argument('--solution', '-s', metavar='"word"', type=ascii, nargs='+',
                    default='trial', help='the solution word')
parser.add_argument('--allowed_words_file', '-a', metavar='path/to/file.txt',
                    default='wordle-lists/wordle-nyt-allowed-guesses.txt', nargs='+',
                    help='file containing list of allowed words')

    
#Wordle Data Structure
class WordleStruct(object):
    SIZE = 5 #Wordle is 5 words
    GREY = 0
    YELLOW = 1
    GREEN = 10
    
    def __init__(
        self,
        wordle,
        matchArray = [0,0,0,0,0]
    ):
        self.wordle = wordle.strip()
        self.matchArray = matchArray
        
        if self.isNotWordleSize(self.wordle):
            raise Exception("Lenth of "+self.wordle+" != 5" )

    def isNotWordleSize(self, word):
        if len(word) != WordleStruct.SIZE:
            return True;
        return False;
    
    def printWord(self):
        print(self.wordle)
        
    def printMatch(self):
        print (self.matchArray)
        
    def compare(self, test_word):
        if len(self.wordle) != len(test_word):
            raise Exception("Lenth of "+test_word+" != " )

        for i in range(0, WordleStruct.SIZE):
            for j in range(0, WordleStruct.SIZE):
                if self.wordle[i] is test_word[j]:
                    self.matchArray[i] = WordleStruct.YELLOW
            if self.wordle[i] is test_word[i]:
                self.matchArray[i] = WordleStruct.GREEN
        self.printMatch()
        return self.matchArray
    
        
            
class WordleData(object): # In Python 3, all classes are "new-style," and writing (object)
    def __init__(
        self,
            letter_position_count = {'a': [0,0,0,0,0]}, # dict
        word_list = []
    ):
        # tyep(str, list, float)
        self.word_list = word_list
        self.letter_position_count = letter_position_count
        
    def updateLetterPosition(self, word):
        word = word.strip()
        for i in range(0,WordleStruct.SIZE):
            letter = word[i]
            count = self.letter_position_count.setdefault(letter, [0,0,0,0,0])
            count[i] +=1
        self.letter_position_count = OrderedDict(sorted(self.letter_position_count.items()))

    def printLetterCount(self):
        for letter, count in self.letter_position_count.items():
            print(letter, " : ", count)
        """
        Definition

        :param name_of_param : description
        """
#        super(SomeClass, self).__init__(test_name=test_name) #super() returns objects represented in the parent class


        self.time = 0.0

        
class WordleSolver(object): # In Python 3, all classes are "new-style," and writing (object)
    def __init__(
            self,
            allowed_words_file_path = "test.txt",
            starter_word = "irate",
            solution = "steal",
            solutions = [],
    ):
        self.data = WordleData();
        self.allowed_words_file_path = allowed_words_file_path
        self.solutions = solutions
        self.starter_word = starter_word
        self.solution = solution

        #parse NYT list file into wordle struct
        with open(self.allowed_words_file_path, newline='') as f:
            lines = f.readlines()
            for line in lines:
               # print(line)
                self.data.word_list.append(WordleStruct(line))
                self.data.updateLetterPosition(line)
            self.data.printLetterCount()
        
    def printList(self):
        for solution in self.data.word_list:
            print(solution.wordle)

    def solveFor(self, word):
        print (word)

    def setStarterWord(self, starter_word):
        self.starter_word = starter_word

    def begin(self):
        for word in self.data.word_list:
            word.compare(self.starter_word)
## Main        
args = parser.parse_args()
abs_path = os.path.abspath(args.allowed_words_file)



wordleSolver = WordleSolver(args.allowed_words_file)
wordleSolver.setStarterWord("irate")
wordleSolver.begin()

#wordleSolver.printList()

wordle = WordleStruct("apple")
wordle.printWord()
wordle.compare("green")
wordle.compare("apple")
#print(wordleSolver.__dict__)
