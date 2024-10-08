
class C4Agent: 

    def move(self, symbol, board, last_move):
        '''
        symbol is the character that represents the agent's moves in the board
        symbol will be consistent throughout the game
        board is an array of 7 strings each describing a column of the board
        last_move is the column that the opponent last droped a piece into (or -1 if it is the first move of the game)
        This method should return the column the agent would like to drop their token into.
        '''
        
        # This agent plays from the leftmost column so long as it is a legal move
        for i in range (7):
            if len(board[i]) < 6:
                return i
            
            
        # This agent always plays in the leftmost column
        # return 0   
