from collections import deque

def gostonepuzzle(N, S, T):
    # Initialize the BFS queue with the starting state and operation count
    initial_state = S + 'EE'
    target_state = T + 'EE'
    
    # Check if initial and target states are already the same
    if initial_state == target_state:
        return 0
    
    # BFS setup
    queue = deque([(initial_state, 0)])  # (current_state, operations_count)
    visited = set()
    visited.add(initial_state)
    
    # BFS loop
    while queue:
        current_state, steps = queue.popleft()
        
        # Find positions of empty cells
        empty_indices = [i for i, c in enumerate(current_state) if c == 'E']
        
        # Try all possible moves
        for i in range(N + 1):  # i is the index for the first stone in a pair
            if current_state[i] != 'E' and current_state[i + 1] != 'E':
                if len(empty_indices) == 2:
                    empty_index1, empty_index2 = empty_indices
                    
                    # Create a new state by moving the stones
                    new_state_list = list(current_state)
                    new_state_list[empty_index1] = new_state_list[i]
                    new_state_list[empty_index2] = new_state_list[i + 1]
                    new_state_list[i] = 'E'
                    new_state_list[i + 1] = 'E'
                    new_state = ''.join(new_state_list)
                    
                    if new_state == target_state:
                        return steps + 1
                    
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, steps + 1))
    
    # If the target state is not reachable
    return -1

# Reading input
N = int(input().strip())
S = input().strip()
T = input().strip()

# Function call
print(gostonepuzzle(N, S, T))
