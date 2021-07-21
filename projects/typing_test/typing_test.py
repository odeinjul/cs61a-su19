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
# END Q1-5

# Question 6

def score_function(word1, word2):
    """A score_function that computes the edit distance between word1 and word2."""

    if ______________: # Fill in the condition
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        # END Q6

    elif ___________: # Feel free to remove or add additional cases
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        # END Q6
    
    else:
        add_char = ______________  # Fill in these lines
        remove_char = ______________ 
        substitute_char = ______________ 
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        # END Q6

KEY_DISTANCES = get_key_distances()

# BEGIN Q7-8
"*** YOUR CODE HERE ***"
# END Q7-8
