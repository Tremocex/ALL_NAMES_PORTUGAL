# -*- coding: utf-8 -*-
"""
Created on Sun May 16 19:39:59 2021

@author: eduar
"""

import re
from collections import Counter
from spellchecker import SpellChecker
import io

WORDS = {}

def words(text): return re.findall(r'\w+', text.upper())

#print(WORDS)
def P(word, N=sum(WORDS.values())): 
    "Probability of `word`."
    return WORDS[word] / N

def correction(word): 
    "Most probable spelling correction for word."
    return max(candidates(word), key=P)

def candidates(word): 
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

def known(words): 
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)

def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = ' ÃÁÀÂABCDEÉÊFGHIÍÌÇJKLMNOÓÒÔÕPQRSTUÚÙVXYZ'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word): 
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))

def get_word(word,flag):
    global WORDS
    
    if flag == 0:
        
        WORDS = Counter(words(io.open('names_final.txt', 'r', encoding='utf-8').read()))
    
        if WORDS[word] == 0:
            return False
        else:
            return True
        
    else:
        
        WORDS = Counter(words(io.open('surnames_final.txt', 'r', encoding='utf-8').read()))
    
        if WORDS[word] == 0:
            return False
        else:
            return True
        
#print((WORDS['YAGE']))
print(get_word('MIGUEL',1))