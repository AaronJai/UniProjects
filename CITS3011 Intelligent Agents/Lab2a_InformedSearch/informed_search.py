import heapq

def find_path(start_word, end_word, word_list):
    # create a set of words with the same length as start_word
    words = {word for word in word_list if len(word) == len(start_word)}
    
    # Heuristic to return an estimate of how far away we are from the end
    def heuristic(word):
        # return 0
        
        # estimates how far the current word is from the end_word. 
        count = 0
        for l, r in zip(word, end_word):
            # if the letters are the same, decrement the count
            if l == r:
                count -= 1
        return count
    
    parents = {}
    # dist = {}
    pq = []
    heapq.heappush(pq, (0, 0, None, start_word)) # (priority, distance, parent, word/state)
    
    while pq:
        _, d, p, u = heapq.heappop(pq)
        
        # if we have already visited this word, skip
        if u in parents:
            continue
        # otherwise mark as visited
        parents[u] = p  
        
        # early exit after marking as visited
        if u == end_word:
            path = []
            while u is not None:
                path.append(u)
                u = parents[u]
            path.reverse()
            return path 
       
        # go through next words
        for v in next_words(u, words):
            # if already visited, skip
            if v in parents:
                continue
            g = d + 1                 # compute distance to that child
            h = heuristic(v)                # heuristic for that child state 
            f = g + h                       # add them together to get the priority
            heapq.heappush(pq, (f, g, u, v))   # push the child to the queue with the priority
    
    return None
                
                
def next_words(word, words):
    result = []
    for i in range(len(word)):
        for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            w = word[:i] + c + word[i+1:]
            if w in words:
                result.append(w)
    return result



# def next_words(curr_word, words):
#     result = []
    
#     for i in range(len(curr_word)):
#         for c in range(ord('A'), ord('Z')+1):   # ord() returns the ASCII code of the letter
#             char = chr(c)                       # chr() returns the letter of the ASCII code
            
#             # if character in our word equals the char from the loop, skip
#             if curr_word[i] == char:
#                 continue
#             # form new word by replacing the character at the current position
#             next_word = curr_word[:i] + char + curr_word[i+1:]
            
#             if next_word not in words:
#                 continue
#             result.append(next_word)
    
#     return result
 