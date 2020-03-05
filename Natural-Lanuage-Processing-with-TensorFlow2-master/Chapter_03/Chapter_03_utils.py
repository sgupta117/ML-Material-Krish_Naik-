'''
Utility Functions for Chapter_03.ipynb
Make sure this file is stored in the same folder where your Chapter_03.ipynb is located
'''
#-----------------------------------------------------------------------------------#
# Imports                                                                           #
#-----------------------------------------------------------------------------------#
import re

#-----------------------------------------------------------------------------------#
# Globals                                                                           #
#-----------------------------------------------------------------------------------#

punctPat = re.compile(r'^[\'\".,;:()!?-]+$')

def isPunctuation(token):
    '''
    True if input string is only punctuation
    '''
    if punctPat.match(token):
        return True
    return False

def terms2ints(termsList):
    '''
    Return dictionary of keys = terms, values = integer codes
    Include '<UNKNOWN>' at end as final value
    '''
    maxWords = len(list(termsList))
    result =  {t:i for (i,t) in enumerate(termsList)}
    result['<UNKNOWN>'] = maxWords
    return result

def ints2terms(termsDict):
    '''
    Flip the term:int key value pairs, return flipped result
    '''
    return {v:k for (k, v) in termsDict.items()}

class IntEncoder():
    '''
    Class to encode lists of terms as integers.
    We pass the terms-integers codes dictionary, and the reverse (integer codes to terms dictionary)
    as arguments to the init function.
    '''

    def __init__(self, termsDict, reverseTermsDict):
        '''
        Instantiate the encoder object
        '''
        assert isinstance(termsDict, dict)
        assert isinstance(reverseTermsDict, dict)

        self.termsDict = termsDict
        self.reverseTermsDict =  reverseTermsDict
        self.vocabLen = len(list(self.termsDict.keys()))

    def lookupCode(self, term):
        '''
        Lookup the integer code for a term in the dict, or return Unknown
        '''
        if (term in self.termsDict.keys()):
            return self.termsDict[term]
        else:
            return self.termsDict['<UNKNOWN>']

    def lookupTerm(self, code):
        '''
        Lookup the term corresponding to an integer code
        '''

        if (code in self.reverseTermsDict.keys()):
            return self.reverseTermsDict[code]
        else:
            return('<UNKNOWN>')

    def encode(self, termsList):
        '''
        Return a list of integer codes corresponding to the words in the input termsList
        '''

        return [self.lookupCode(t) for t in termsList]
