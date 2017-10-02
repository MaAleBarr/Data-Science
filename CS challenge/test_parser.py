#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 09:02:01 2017

@author: mariaalejandrabarrios

Test methods in Parser class 
"""

import pytest
import os

os.chdir('/Users/mariaalejandrabarrios/Documents/0_DataScience/0_Insight/Data Challenge/CS challenge')

#from parser import Parser

@pytest.fixture
def par():
    from parser import Parser
    return Parser()

# test SubString
test_SubString_data = [(' hello 90  World', ['hello','90','World'])]
@pytest.mark.parametrize('x, expected', test_SubString_data)
def test_SubString(x, expected, par):
    assert par.GetSubStrings(x) == expected

# test CleanString 
test_CleanString_data = [('#$%Lots  ','Lots'), ('$-18%','-18'), ('With%*(Caps)','WithCaps'), ('14.7-1','1471')]
@pytest.mark.parametrize('x, expected', test_CleanString_data)
def test_CleanString(x, expected, par):
    assert par.CleanString(x) == expected

# test SortByNth
test_SortByNth_data = [(['12','dog','apple','0'],'0 apple dog 12'), 
                       (['40','Baby','-1000','apple'], '-1000 apple 40 Baby')]
@pytest.mark.parametrize('x, expected', test_SortByNth_data)
def test_SortByNth(x, expected, par):
    assert par.SortByNth(x) == expected


#==============================================================================
# test_perfect_number_data = [(6,True),(28,True),(496,True),(8,False)]
# @pytest.mark.parametrize('x,expected',test_perfect_number_data)
# def test_perfect_number_optimized(x,expected, num):
#     #num = Numbers()
#     assert num.perfect_number_optimized(x) == expected
# 
#==============================================================================
