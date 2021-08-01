""" Typing Test implementation """

from utils import *
from ucb import main

# BEGIN Q1-5
"*** YOUR CODE HERE ***"
def lines_from_file(path):
    fi = open(path, mode='r')
    re_fi = []
    i = 0
    temp = 1
    while(temp != ""):
        temp = readline(fi)
        if(temp != ""):
            re_fi += [strip(temp)]
    return re_fi

def new_sample(path, i):
    return lines_from_file(path)[i]

"""

Other's solution, maybe i'll comprehand it someday later
def lines_from_file(path):
    with open(path) as f:
        return [line.strip() for line in f]  # Should be rstrip() if input file is well-written

def new_sample(path, i):
    with open(path) as f:
        for _ in range(i):
            next(f)  # Discard first i-1 lines
        return next(f).strip()
        
"""

def analyze(sample_paragraph, typed_string, start_time, end_time):
    lst = []
    lst += [analyze_velocity(typed_string, start_time, end_time)]
    lst += [analyze_accuracy(sample_paragraph, typed_string)]
    return lst
def analyze_velocity(typed_string, start_time, end_time):
    words = len(typed_string)
    words_per_min = words * 12 / (end_time - start_time)
    return words_per_min

def analyze_accuracy(sample_paragraph, typed_string):
    sample = split(sample_paragraph)
    typed = split(typed_string)
    count = 0
    if(len(sample) <= len(typed)):
        for x in range(len(sample)):
            if(sample[x] == typed[x]):
                count += 1
        return count * 100 / len(sample)
    elif(len(typed) == 0):
        return 0.0
    else:
        for x in range(len(typed)):
            if(sample[x] == typed[x]):
                count += 1
        return count * 100 / len(typed)

def pig_latin(word):
    id = find_first_vovel(word)
    if is_vowel(word[0]):
        return word + "way"
    elif(id == -1):
        return word + "ay"
    else:
        return word[id:] + word[:id] + "ay"
    

def is_vowel(char):
    if char in 'aeiou':
        return True
    else: 
        return False

def find_first_vovel(word):
    for index,char in enumerate(word):
        if is_vowel(char):
            return index
    return -1

# Phase 2 passcode: 'ratification'
def autocorrect(user_input, words_list, score_function):
    if(user_input in words_list):
        return user_input
    else:
        return min(words_list, key = lambda t: score_function(user_input, t))

def swap_score(s1, s2):
    #disregard all extra characters
    if(not s1 or not s2):
        return 0
    else:
        if(s1[0] != s2[0]):
            return 1 + swap_score(s1[1:], s2[1:])
        else:
            return swap_score(s1[1:], s2[1:])

# END Q1-5

# Question 6

def score_function(word1, word2):
    """A score_function that computes the edit distance between word1 and word2."""

    if not word1 or not word2 or word1 in word2 or word2 in word1: # Fill in the condition
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        return abs(len(word1) - len(word2))
        # END Q6

    elif word1[0] == word2[0]: # Feel free to remove or add additional cases
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        return score_function(word1[1:], word2[1:])
        # END Q6
    
    else:
        add_char = 1 + score_function(word1, word2[1:])  # Fill in these lines
        remove_char = 1 + score_function(word1[1:], word2)
        substitute_char = 1 + score_function(word1[1:], word2[1:])
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        return min(add_char, remove_char, substitute_char)
        # END Q6

KEY_DISTANCES = get_key_distances()

# BEGIN Q7-8
"*** YOUR CODE HERE ***"
def score_function_accurate(word1, word2):
    if not word1 or not word2 or word1 in word2 or word2 in word1: 
        return abs(len(word1) - len(word2))

    elif word1[0] == word2[0]:
        return score_function_accurate(word1[1:], word2[1:])
    
    else:
        add_char = 1 + score_function_accurate(word1, word2[1:])
        remove_char = 1 + score_function_accurate(word1[1:], word2)
        substitute_char = KEY_DISTANCES[word1[0], word2[0]] + score_function_accurate(word1[1:], word2[1:])
        return min(add_char, remove_char, substitute_char)

def score_function_final(word1, word2):
    if not word1 or not word2 or word1 in word2 or word2 in word1: 
        return abs(len(word1) - len(word2))

    elif word1[0] == word2[0]:
        return score_function_final(word1[1:], word2[1:])
    
    else:
        add_char = 1 + score_function_final(word1, word2[1:])
        remove_char = 1 + score_function_final(word1[1:], word2)
        substitute_char = KEY_DISTANCES[word1[0], word2[0]] + score_function_final(word1[1:], word2[1:])
        return min(add_char, remove_char, substitute_char)

def mem(f):
    cache = dict()
    def mem_f(*args):
        if args in cache:
            return cache[args]
        result = f(*args)
        cache[args] = result
        return result
    return mem_f
    
score_function_final = mem(score_function_final)
# END Q7-8
