"""
Monte Carlo Tic-Tac-Toe Player
"""
#import user40_h3mj0wBviS_9 as test

#import user40_UYG2dk3s9k_0 as mc_test
#import user40_UYG2dk3s9k_5 as mc_best
#import user40_UYG2dk3s9k_12 as mc_move_test

import random

import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.

NTRIALS = 10         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
# Add your functions here.
BOARD_SIZE = 3





def mc_trial(board, player):
    """
    MC Trial
    """
    #print board.__str__()
    while board.check_win() == None:
        empty_square = board.get_empty_squares()
        #print "empty squares 1", empty_square
        #if len(empty_square) > 1:
        random_square = empty_square[random.randrange(len(empty_square))]

        board.move(random_square[0], random_square[1], player)
        player = provided.switch_player(player)

        empty_square = board.get_empty_squares()
        #print "empty squares 2", empty_square
        if len(empty_square) < 1 :
            return
        random_square = empty_square[random.randrange(len(empty_square))]

        #elif len(empty_square)  == 0:
        random_square = empty_square[0]
        board.move(random_square[0], random_square[1], player)      
    return
    

    
#scores_grid = [[0 for dummy_idx in range(BOARD_SIZE)] for dummy_idx in range(BOARD_SIZE)]


def mc_update_scores(scores, board, player):
    """
    Update Scores
    """
    game_outcome = board.check_win()
    print "outcome ", game_outcome
    who_won = {}
    
    if game_outcome == provided.DRAW:
         return
    elif game_outcome == provided.PLAYERX:
        who_won = {provided.PLAYERX: 1, provided.PLAYERO: -1, provided.EMPTY:0}
    elif game_outcome == provided.PLAYERO:
        who_won = {provided.PLAYERO: 1, provided.PLAYERX: -1, provided.EMPTY:0}
       
    game_board = [[0 for dummy_idx in range(board.get_dim())] for dummy_idx in range(board.get_dim())]
    
      
    for dummy_row in range(board.get_dim()):
        for dummy_col in range(board.get_dim()):
            square = board.square(dummy_row, dummy_col)
            game_board[dummy_row][dummy_col] = square
            
    
    
    
    for dummy_row in range(len(scores)):
        for dummy_col in range(len(scores)):
            
            scores[dummy_row][dummy_col] += who_won[game_board[dummy_row][dummy_col]]

    
    #print scores
    
def get_best_move(board, scores):
    """
    Get best move 
    """
    squares = board.get_empty_squares()
    
    squares_list = []
    
   
    for item in squares:
        squares_list.append((scores[item[0]][item[1]], item))
    print "Squares list ", squares_list
    score, pos = max(squares_list)
    print "the max is ", score
    return pos
   
        
 
    
def mc_move(board, player, trials):
    """
    MC move 
    """
    
    print 
    print
    board_dim = board.get_dim()
    new_board = board.clone()
    
    print "new test"
    
    scores = [[0 for dummy_idx in range(board_dim)] for dummy_idx in range(board_dim)]
    for dummy_inx in range(trials):
        mc_trial(new_board, player)
        print new_board.__str__()
        
        mc_update_scores(scores, new_board, player)
        print "scores ", scores
        new_board = board.clone()
    next_move = get_best_move(board, scores)
    
    
    print "next move ", next_move
    return next_move
    
    
    
 


#test.run_suite(mc_update_scores)
#mc_test.run_suite(mc_trial)
#mc_best.run_suite(get_best_move)
#mc_move_test.run_suite(mc_move)

# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

#provided.play_game(mc_move, 3, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, 10, False)
