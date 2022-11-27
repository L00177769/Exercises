"""
Script: remove_brackets.py
By: John O'Raw
Purpose: Removes brackets from an input string
Tested: 12/11/2022
"""


# function provided by lecturer John O'Raw        
def remove_brackets(string_with_brackets):
    """ removes brackets from an item """
    # remove right bracket using Python string function
    string_without_brackets = str(string_with_brackets.strip('('))
    # remove left bracket using Python string function
    string_without_brackets = str(string_without_brackets.strip(')'))
    # returns string with brackets removed
    return string_without_brackets