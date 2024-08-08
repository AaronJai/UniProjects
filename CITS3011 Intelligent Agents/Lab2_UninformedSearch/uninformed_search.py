"""
Notes
Main difference in using next_words and is_legal:

is_legal checks every word in word_list for each current word in the BFS queue, which can be slow when the word_list is large.

next_words instead modifies the word directly and checks if it exists in the word list, since it doesnt have to do any unecessary comparisons.

both code snippets utilise BFS, but highlight the importance of optimising the code for the specific problem at hand.
"""

from collections import deque

# added helper function to check if two words are adjacent
"""
Purpose: Generates all valid next words that are one letter different from the current word.

Implementation:
    - Loop Through Each Character Position: For each position in the word, try replacing the character with every letter from 'A' to 'Z'.
    - Skip Same Character: Skip if the character is the same as the current character at that position.
    - Form New Word: Form a new word by replacing the character at the current position.
    - Check Validity: Check if the new word is in the provided set of words.
    - Add to Results: If valid, add the new word to the results list.
"""
def next_words(curr_word, words):
    result = []
    
    for i in range(len(curr_word)):
        for c in range(ord('A'), ord('Z')+1):   # ord() returns the ASCII code of the letter
            char = chr(c)                       # chr() returns the letter of the ASCII code
            
            # if character in our word equals the char from the loop, skip
            if curr_word[i] == char:
                continue
            # form new word by replacing the character at the current position
            next_word = curr_word[:i] + char + curr_word[i+1:]
            
            if next_word not in words:
                continue
            result.append(next_word)
    
    return result


def find_path(start_word, end_word, word_list):
    words = {word for word in word_list if len(word) == len(start_word)}    # turn into a set, gives O(1) checks
    
    parents = {start_word: None}
    
    queue = deque()
    queue.append(start_word)
    
    while len(queue) > 0:
        curr = queue.popleft()
        
        if curr == end_word:
            sequence = []
            
            while curr != None:
                sequence.append(curr)
                curr = parents[curr]
            sequence.reverse()
            
            return sequence
        
        # no need to check for legal word anymore
        for word in next_words(curr, words):
            if word in parents:
                continue
            
            queue.append(word)
            parents[word] = curr
    
    return None



###############################################  LAB SOL1  ###############################################
##########################################################################################################
##########################################################################################################



# from collections import deque

# # Check if next word is reachable from current word by changing only one character
# def is_legal(curr_word, next_word):
#     # check length difference
#     if len(curr_word) != len(next_word):
#         return False
    
#     # return true if exactly 1 character is different
#     diff = 0
#     for i in range(len(curr_word)):
#         if curr_word[i] != next_word[i]:
#             diff += 1
#     return diff == 1


# def find_path(start_word, end_word, word_list):
#     words = [word for word in word_list if len(word) == len(start_word)]
    
#     # keep track of each word's parent in the path
#     parents = {start_word: None}
    
#     queue = deque()
#     queue.append(start_word)
    
#     while len(queue) > 0:
#         # remove and process word at the front of the queue
#         curr = queue.popleft()
        
#         # if the current word is the end word, reconstruct the path
#         # by backtracking trhough the 'parents' dictionary and returns the path
#         if curr == end_word:
#             sequence = []
            
#             while curr != None:
#                 sequence.append(curr)
#                 curr = parents[curr]
#             sequence.reverse()
            
#             return sequence
        
#         # this bit is causing the most time used
#         for word in words:
#             # check if word can be reached from current word
#             if not is_legal(curr, word): 
#                 continue
            
#             # if word is already in the path, skip it
#             if word in parents:
#                 continue
            
#             # if legal and not yet cisited, add word to queue and update its parents in the dict.
#             queue.append(word)
#             parents[word] = curr
    
#     return None