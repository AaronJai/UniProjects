"""
Attempting to solve the issue with 'left hand on the wall' strategy
Using DFS
"""

# ACTIONS = {
#     'D': (0, -1),
#     'U': (0, 1),
#     'L': (-1, 0),
#     'R': (1, 0)
# }

# REVERSE = {
#     'D': 'U',
#     'U': 'D',
#     'L': 'R',
#     'R': 'L'
# }

# class MazeAgent():
#     def reset(self):
#         self.stack = []
#         self.pos = None
#         self.blocked = set()
#         self.next_pos = None

#     def get_next_move(self, x, y):
#         prev_pos = self.pos
#         self.pos = (x, y)
#         if self.pos == prev_pos:
#             self.blocked.add(self.next_pos)
        
#         self.blocked.add(self.pos)
#         choice = None
        
#         for d, (dx, dy) in ACTIONS.items(): # for each direction, (dx, dy) = change in direction
#             nx, ny = x + dx, y + dy         # new x, new y
#             if (nx, ny) not in self.blocked: # if new position not visited
#                 choice = d
#                 self.stack.append(choice)
#                 self.next_pos = (nx, ny)
#                 break
        
#         if choice is None:
#             choice = REVERSE[self.stack.pop()] # backtrack
        
#         return choice
            
        

###############################################  LAB SOL1  ###############################################
##########################################################################################################
##########################################################################################################

"""
- 'left hand on the wall' strategy' - always turn left
agent always attempts to change direction on each iteration,
moves to next direction if it moved from the previous position,
otherwise, it moves to the previous direction.

while it passes the test cases, it will fail in situations such as an open space where it will
essentially go in a circle
"""

ACTIONS = ['D', 'R', 'U', 'L']

class MazeAgent():
    def reset(self):
        self.dir = 0
        self.pos = None

    def get_next_move(self, x, y):
        prev_pos = self.pos
        self.pos = (x, y)
        if self.pos != prev_pos: # means we moved
            # len(ACTIONS) keep self.dir within the range of 0-3 (in ACTIONS)
            self.dir = (self.dir + 1) % len(ACTIONS) # move to next direction
        else:
            self.dir = (self.dir - 1) % len(ACTIONS)
        
        return ACTIONS[self.dir]
        


###############################################  DFS v2  #################################################
##########################################################################################################
##########################################################################################################

"""
Adjusted DFS strategy

fixed the issue for backtracking when it didnt reverse the direction it took.
- also ignored storing the direction in the stack intially (before needing to backtrack)
also initialised the stack with the start position instead of an empty list
 
"""

# import random

# class MazeAgent:
#     def __init__(self):
#         self.reset()
        
#     def reset(self):
#         self.previous_location = None
#         self.last_direction = None
#         self.visited = set() 
#         self.stack = []  # Initialize stack with the start position instead of empty list
    
#     def get_next_move(self, x, y):
#         if not self.stack:
#             # First call: Initialize the stack with the current position
#             self.stack.append((x, y))
#             self.visited.add((x, y))
#             return None  # No more moves available

#         # Move options with corresponding coordinate changes
#         moves = {'L': (x - 1, y), 'R': (x + 1, y), 'U': (x, y + 1), 'D': (x, y - 1)}
        
#         # Check valid moves
#         valid_moves = []
#         for direction, (nx, ny) in moves.items():
#             if 0 <= nx < 10 and 0 <= ny < 10 and (nx, ny) not in self.visited:
#                 valid_moves.append(direction)
        
#         if valid_moves:
#             # Choose a move from valid options
#             direction = random.choice(valid_moves)
#             nx, ny = moves[direction]
            
#             # Update state
#             self.last_direction = direction
#             self.previous_location = (x, y)
#             self.visited.add((nx, ny))  # Mark the new cell as visited
#             self.stack.append((nx, ny))  # Push the new position onto the stack
            
#             return direction
#         else:
#             # BACKTRACKING
#             self.stack.pop()  # Remove the current position from the stack
            
#             if self.stack:
#                 # Move to the previous position in the stack
#                 prev_x, prev_y = self.stack[-1]
#                 if prev_x < x:
#                     direction = 'L'
#                 elif prev_x > x:
#                     direction = 'R'
#                 elif prev_y < y:
#                     direction = 'D'
#                 else:
#                     direction = 'U'
                
#                 self.previous_location = (x, y)
#                 self.last_direction = direction
                
#                 return direction
#             else:
#                 return None  # No more moves available

#####################################################DFS##################################################
##########################################################################################################
##########################################################################################################

"""
Introduce DFS strategy
added a stack to keep track of path taken

when we pushed onto the stack, it stored the new position and direction it took.
issue here is that when backtracking it didnt reverse the direction it took.
"""


# import random

# class MazeAgent:
#     def __init__(self):
#         self.reset()
        
#     def reset(self):
#         self.previous_location = None
#         self.last_direction = None
#         self.visited = set()  # To keep track of visited cells
#         self.stack = []  # Stack to manage the DFS path
    
#     def get_next_move(self, x, y):
#         # Move options with corresponding coordinate changes
#         moves = {'L': (x - 1, y), 'R': (x + 1, y), 'U': (x, y + 1), 'D': (x, y - 1)}
        
#         # Check valid moves
#         valid_moves = []
#         for direction, (nx, ny) in moves.items():
#             if 0 <= nx < 10 and 0 <= ny < 10:  # Check grid bounds
#                 if (nx, ny) not in self.visited:  # Check if not visited
#                     valid_moves.append(direction)
        
#         if not valid_moves:
#             if self.stack:
#                 # Backtrack if no valid moves
#                 direction, (x, y) = self.stack.pop()
#                 self.previous_location = (x, y)
#                 self.last_direction = None
#                 return direction
#             else:
#                 return None  # No valid moves and stack is empty
        
#         # Choose a move based on DFS strategy
#         direction = random.choice(valid_moves)
        
#         # Update state
#         self.last_direction = direction
#         self.previous_location = (x, y)
#         self.visited.add((x, y))  # Mark the current cell as visited
        
#         # Calculate new position
#         new_x, new_y = moves[direction]
        
#         # Push the move to the stack
#         self.stack.append((direction, (new_x, new_y)))
        
#         return direction


#####################################################3####################################################
##########################################################################################################
##########################################################################################################

"""
this version now started tracking visited cells
turned moves into a dictionary
after selecting a move, agent will add the current cell to the visited set
"""

# import random

# class MazeAgent:
#     def __init__(self):
#         self.reset()
        
#     def reset(self):
#         self.previous_location = None
#         self.last_direction = None
#         self.visited = set()  # To keep track of visited cells
    
#     def get_next_move(self, x, y):
#         # Move options
#         moves = {'L': (x - 1, y), 'R': (x + 1, y), 'U': (x, y + 1), 'D': (x, y - 1)} # helps check for valid moves
#         valid_moves = []
        
#         # Check valid moves
#         for direction, (nx, ny) in moves.items():
#             if 0 <= nx < 10 and 0 <= ny < 10:  # Check grid bounds
#                 if (nx, ny) not in self.visited:  # Check if not visited
#                     valid_moves.append(direction)
        
        
#         # Remove last direction if it led to the previous location
#         if (x, y) == self.previous_location and self.last_direction:
#             if self.last_direction in valid_moves:
#                 valid_moves.remove(self.last_direction)
        
#         if not valid_moves:
#             return None  # No valid moves
        
#         # Choose a random move from valid options
#         direction = random.choice(valid_moves)
        
#         # Update state
#         self.last_direction = direction
#         self.previous_location = (x, y)
#         self.visited.add((x, y))  # Mark the current cell as visited
        
#         return direction


################################################  TEST 2  ################################################
##########################################################################################################
##########################################################################################################
"""
defined a set of moves,
defined what the legal moves were for each position,

removed the last direction tried if it led to the previous location (current location - i.e., didnt move),
chose a random move from the remaining options,
updated the last direction and previous location, and
returned the chosen direction.
"""

# import random

# class MazeAgent():
#     def reset(self):
#         self.previous_location = None
#         self.last_direction = None
        
#     def get_next_move(self, x, y):
#         moves = ['L', 'R', 'U', 'D']
        
#         if x == 9 and y == 9:           # top right corner
#             moves = ['L', 'D']          
#         elif x == 0 and y == 9:         # top left corner
#             moves = ['L', 'U']
#         elif x == 9 and y == 0:         # bottom right corner
#             moves = ['R', 'D']
#         elif 1 < x < 9 and y == 9:      # top row
#             moves = ['L', 'R', 'D']     
#         elif 1 < x < 9 and y == 0:      # bottom row
#             moves = ['L', 'R', 'U']
#         elif x == 9 and 1 < y < 9:      # right column
#             moves = ['D', 'U', 'L']
#         elif x == 0 and 1 < y < 9:      # left column
#             moves = ['D', 'U', 'R']
            
#         if (x, y) == self.previous_location and self.last_direction:
#             moves.remove(self.last_direction) # remove last direction tried
        
#         # Choose a random move from the remaining options
#         direction = random.choice(moves)
        
#         # update last direction and previous location
#         self.last_direction = direction
#         self.previous_location = (x, y) 
        
#         return direction


###############################################  TEST 1  #################################################
##########################################################################################################
##########################################################################################################

        
        # if (x, y) == self.previous_location:
        #     return random.choice(moves)
        # self.previous_location = (x, y)
        # return random.choice(moves)

    
    # def get_next_move(self, x, y):
    #     valid_coordinate = set()
    #     wall_coordinate = set()
    #     playing_area = set()
        
    #     for i in range(0, 10):
    #         for j in range(0, 10):
    #             playing_area.add((i, j))
                
    #     # Starting point
    #     valid_coordinate.add((x, y))
        
    #     while (x, y) in playing_area:
            

# if y = 0 and 1 <= 9: random.choice(['L', 'R', 'U'])
            
"""
first had us act as agent to see what the input/output looked like
"""
    
    # def get_next_move(self, x, y):
    #     print(x, y)
    #     d = input().strip()
    #     return d