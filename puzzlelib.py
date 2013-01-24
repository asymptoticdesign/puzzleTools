"""
Title: puzzle lib
Author: nathan lachenmyer
Description: A python library to manipulate hubway data stored on a server.
Usage:
Date Started: 2013 Jan
Last Modified: 2013 Jan
"""
import sys
from collections import Counter

dictionary = []
dict_file = open('/usr/share/dict/words','r')

for word in dict_file:
    dictionary.append(word.upper().strip("\n"))

def anagram(pattern,dictionary=dictionary):
    """
    Find all anagrams of 'pattern' in the dictionary file
    """
    #turn word into a list of character
    character_list = list(pattern.upper())
    #sort the characters
    character_list.sort()
    #check against all words in our dictionary
    for word in dictionary:
        #check if words are the same length -- if not, they can't be anagrams of each other!
        if(len(word) == len(character_list)):
            sorted_word = sorted(word)
            if character_list == sorted_word:
                print word

def superanagram(pattern,max_size = 100, dictionary=dictionary):
    """
    Find all subanagrams
    """
    #turn word into a list of character
    character_list = list(pattern.upper())
    #sort the characters
    character_list = Counter(character_list)
    #check against all words in our dictionary
    for word in dictionary:
        #check if words are the appropriate -- if not, they can't be anagrams of each other!
        if((len(word) >= len(character_list)) & (len(word) <= max_size)):
            wordCounter = Counter(word)
            if((character_list & wordCounter) == character_list):
                print word, (wordCounter - character_list).items()

def subanagram(pattern,min_size=0,dictionary=dictionary):
    """
    Find all subanagrams
    """
    #turn word into a list of character
    character_list = list(pattern.upper())
    #sort the characters
    character_list = Counter(character_list)
    #check against all words in our dictionary
    for word in dictionary:
        #check if words are the appropriate -- if not, they can't be anagrams of each other!
        if((len(word) < len(character_list)) & (len(word) <= min_size)):
            wordCounter = Counter(word)
            if((character_list & wordCounter) == wordCounter):
                print word, (character_list - wordCounter).items()

def transadd(pattern,add_size=1,dictionary=dictionary):
    """
    Find all superanagrams of length n+1
    Optional: select letter
    """
    #turn word into a list of character
    character_list = list(pattern.upper())
    #sort the characters
    character_list = Counter(character_list)
    #check against all words in our dictionary
    for word in dictionary:
        #check if words are the appropriate -- if not, they can't be anagrams of each other!
        if(len(word) == len(character_list) + add_size):
            wordCounter = Counter(word)
            if((character_list & wordCounter) == character_list):
                print word, (wordCounter - character_list).items()

def transdelete(pattern,delete_size=1,dictionary=dictionary):
    """
    Find all superanagrams of length n+1
    """
    #turn word into a list of character
    character_list = list(pattern.upper())
    #sort the characters
    character_list = Counter(character_list)
    #check against all words in our dictionary
    for word in dictionary:
        #check if words are the appropriate -- if not, they can't be anagrams of each other!
        if(len(word) + delete_size == len(character_list)):
            wordCounter = Counter(word)
            if((character_list & wordCounter) == wordCounter):
                print word, (character_list-wordCounter).items()

#to-do:
#words distance from
#filter words (regex)

#ceasar shift (stringtools)
#word bank
