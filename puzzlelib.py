"""
Title: puzzle lib
Author: nathan lachenmyer
Description: A python library to manipulate strings for wordplay puzzles
Usage:
Date Started: 2013 Jan
Last Modified: 2013 Jan
"""

import re
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
        if((len(word) <= len(character_list)) & (len(word) >= min_size)):
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

def transmix(pattern,dist=1,dictionary=dictionary):
    """
    Retrieve all words from the dictionary that are a given distance from the given pattern (including anagram)
    """
    #turn word into a list of character
    character_list = list(pattern.upper())
    #sort the characters
    character_list = Counter(character_list)
    #check against all words in our dictionary
    for word in dictionary:
        if(len(word) == len(character_list)):
            wordCounter = Counter(word)
            if(sum((wordCounter - character_list).values()) == dist):
                print word, (wordCounter - character_list).items()

def find_distance(pattern,dist=1,dictionary=dictionary):
    """
    Retrieve all words from the dictionary that are a given distance from the given pattern (including anagram)
    """
    #turn word into a list of character
    character_list = list(pattern.upper())
    #check against all words in our dictionary
    for word in dictionary:
        err = 0
        word_list = list(word)
        if(len(word_list) == len(character_list)):
            for i in range(len(character_list)):
                if word_list[i] == character_list[i]:
                    #characters are the same
                    None
                else:
                    err+=1
                if err > dist:
                    break
                if i == len(character_list) - 1:
                    print word

def caesar_shift(encrypted_msg):
    """
    Show all possible caesar shifts of a given string.
    """
    for shift in range(26):
        msg = ''
        for character in encrypted_msg:
            if character.isalpha():
                val = ord(character.upper())

                msg += chr(((val - 65 + shift) % 26) +  65)
            else:
                msg += character
        print shift,":",msg

#to-do:
#string manipulations
## sub bank
## super bank
## bank  
