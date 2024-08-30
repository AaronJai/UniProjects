from collections import *

def bidirectional_search(labyrinth):
    # TODO
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    allowed_states = set() 
    frontier = set()
    backtier = set()
    
    for r, row in enumerate(labyrinth):
        for c, cell in enumerate(row):
            if cell != '#':
                allowed_states.add((r, c))
            elif cell == 'E':
                frontier = {(r, c)}
            elif cell == 'A':
                backtier = {(r, c)}

    fore_parents = {x : None for x in frontier}
    back_parents = {x : None for x in backtier}
    
    middle = None
    while True:
        # Do a fore step
        next_frontier = set()
        for (r, c) in frontier:
            for (dr, dc) in directions:
                new_r, new_c = r + dr, c + dc
                if (new_r, new_c) not in allowed_states:
                    continue
                if (new_r, new_c) in fore_parents:
                    continue
                fore_parents[(new_r, new_c)] = (r, c)
                if (new_r, new_c) in backtier:
                    middle = (new_r, new_c)
                    break
                next_frontier.add((new_r, new_c)) 
            if middle is not None:
                break
        frontier = next_frontier
        
        if middle is not None:
            break
        if not frontier:
            return None
        
        # Do a back step
        next_backtier = set()
        for (r, c) in backtier:
            for (dr, dc) in directions:
                new_r, new_c = r + dr, c + dc
                if (new_r, new_c) not in allowed_states:
                    continue
                if (new_r, new_c) in back_parents:
                    continue
                back_parents[(new_r, new_c)] = (r, c)
                if (new_r, new_c) in frontier:
                    middle = (new_r, new_c)
                    break
                next_backtier.add((new_r, new_c)) 
            if middle is not None:
                break
        backtier = next_backtier
        
        if middle is not None:
            break
        if not backtier:
            return None
        
    
    path = [middle]
    while fore_parents[path[-1]] is not None:
        path.append(fore_parents[path[-1]])
    path.reverse()
    
    while back_parents[path[-1]] is not None:
        path.append(back_parents[path[-1]])
    path.reverse()
    
    return path