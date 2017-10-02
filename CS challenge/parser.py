#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 22:05:17 2017

@author: mariaalejandrabarrios

------------------------------------------------------------------------------
                          Class Description
------------------------------------------------------------------------------
- Parse a string containing words and integers into a sorted list of 
  words (in alphabetical order) and integers in ascending order. 
  
- The type in position n is conservered. If the n-th entry was an integer in the 
  original list, it will be an integer in the sorted list, and likewise if the
  n-th entry was a word in the input list, then it will be a worde in the sorted
  list. 
- Words and integers may have symbols, need to clean symbols out. 
- String can have upper and lower case a-z
- Integers can be from -999999 to 999999
------------------------------------------------------------------------------
"""

import numpy as np

class Parser(object):
    
    def __init__(self):
        pass
    
    def GetSubStrings(self, string):
        '''Parse input string where there is a space'''
        str_ls = []
        ii = 0
        ind0 = 0
        while ii < len(string):
            if string[ii] == ' ':
                str_ls.append(string[ind0:ii])
                ind0 = ii + 1
            elif ii == len(string)-1:
                str_ls.append(string[ind0:ii+1])
            ii = ii +1
        
        # Remove empty strings in list  
        while '' in str_ls:
            str_ls.remove('')
        
        return str_ls
   
    def CleanString(self, string):
        '''Take a string and remove all symbols, leaving only numeric or 
        alphabetical characters. Can handle negative numbers'''
        str_clean = ''
        
        # Keep only alphanumeric characters
        for i,char in enumerate(string):
            if char.isalpha():
                str_clean = str_clean+char
            elif char.isnumeric():
                str_clean = str_clean+char
            # Add exception for '-' character if it is first in list and 
            # next character is nuerical, to account for -(ve) numbers    
            elif char == '-' and string[i+1].isnumeric() and str_clean == '':
                str_clean = str_clean+char 
        return str_clean

    def isint(self, value):
        # Insint tests if value is an integer, will return True if input can be 
        # converted to int
        try:
            int(value)
            return True
        except ValueError:
            return False
        
    def SortByNth(self, str_ls):
        ''' Sorts list of strings by alphabetical order for words and ascending
        numerical order for integers, where input list type for i-th entry is 
        preserved. If i-th entry in input list is numeric (alpha char), it will
        be numeric (alpha car) after sorting. List of strings is converted into
        a single string, with 1-space between entries. '''
        # Initialize list of indices for words and integers
        ind_ints = []
        ind_words = []
        # Find ind for words ans integers in list 
        for i,string in enumerate(str_ls):
            if self.isint(string):
                ind_ints.append(i)
            else:
                ind_words.append(i)  
        # Concert to np array for ease and sort
        sorted_ls = np.asarray(str_ls)
        # lower and uppwer case o si no upper case will be first 
        sorted_ls[ind_ints] = sorted(sorted_ls[ind_ints])
        sorted_ls[ind_words] = sorted(sorted_ls[ind_words], key=str.lower) 
        # Create a single string from sorted list, with 1 space between words
        # or integers
        sorted_str = ' '.join(sorted_ls)
        return sorted_str

    def CleanAndSortedString(self, input_file, output_file):
        ''' Imports string from text file, and exports text file with sorted string
        where all symbols were removed. Uses GetSubstring, CleanString, and 
        SortByNth methods'''
        # Add txt extension
        input_file = input_file+'.txt'
        output_file = output_file+'.txt'
        # Open and read txt file
        file = open(input_file, 'r')
        string = file.read()
        # Generate substrings
        sub_strs = self.GetSubStrings(string)
        # Remove symbols such that each substring is either alphanumeric or numeric only 
        clean_strs = [self.CleanString(f) for f in sub_strs]
        # Sort list such that numbers are in ascending order and words are in alphabetical order
        # where n-th element is word or numeric if it was originally word or numeric
        sort_str = self.SortByNth(clean_strs)
        # Save output txt file
        with open(output_file, 'w') as txt_file:
            txt_file.write(sort_str)    
        return sort_str
    
