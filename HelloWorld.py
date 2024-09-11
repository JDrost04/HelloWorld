def play_tictactoe() -> int:
    """Plays 1 round of tic tac toe.
    Returns:
        int: The winner of the tic tac toe game. If it's 0, then it's 	a tie. 
    """
    # player 1: 1
    # player 2: -1
    player = 1
 
    board = np.zeros((3, 3))
    winner = 0
    done = False
    while not done:
        # get available spots
        available = check_available_moves(board)

        # choose random move
        board = make_move(board, available, player)

        # check if a player won
        done, winner = check_winner(board, player)
        if done:
            return winner
 
        # check for a tie
        s = np.sum(board == 0)       
        # count the number of 0s on the board. If it's 0, then all 	
	    # places are filled and it's a tie
        if s == 0:
            done = True
            winner = 0
            print("It's a tie!")
            return winner
        
        player = 1 if player == -1 else -1

