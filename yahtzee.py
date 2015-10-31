"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""
#import user40_WMcctJ7gyY_6 as strategy_
#import user40_h3mj0wBviS_11 as score_test
#import user40_h3mj0wBviS_14 as ex_val_test
#import user40_WMcctJ7gyY_2 as ex_val_test_2
# Used to increase the timeout, if necessary

import codeskulptor
codeskulptor.set_timeout(40)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    current_hand_score = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    
    for dummy_idx in range(1, 9):

        for item in hand:
            if dummy_idx == item:
                current_hand_score[dummy_idx] += 1
                
    scores_per_number = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    
    for dummy_idx in range(1, 9):
        scores_per_number[dummy_idx] = current_hand_score[dummy_idx] * dummy_idx
    
    highest_score = 0
    for dummy_idx in range(1, 9):
        if scores_per_number[dummy_idx] > highest_score:
            highest_score = scores_per_number[dummy_idx]
            
           
    return highest_score
        

def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    outcome = [dummy_idx for dummy_idx in range(1, num_die_sides+1)]
    #print "outcome is ", outcome
    possible_outcomes = gen_all_sequences(outcome, num_free_dice)
    print "exp val: possible outcomes ",possible_outcomes
    #print possible_outcomes
    the_scores = []
    for item in possible_outcomes:
        item += held_dice
        new_score = score(item)
        the_scores.append(new_score)
            
    expected_val = sum(the_scores)/float(len(the_scores))
    print "exp val: scores are ", the_scores
    return expected_val


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    print "hand is ", hand
    
    result_set = set([()])
    for die_val in hand:
        new_set = result_set.copy()
        #print "gen_:die_val ", die_val
        for tuple_ in new_set:
            #print tuple_
            temp = list(tuple_)
            
            temp.append(die_val)
            temp = sorted(temp)
            result_set.add(tuple(temp))
            
    print "gen_:result_set ", result_set
    return result_set



def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    print 
    print 
    temp_set =  gen_all_holds(hand)
    results_set = {}
    for element in temp_set:
        
        print "strategy: element is ", element
        len_set = len(hand)-len(element)
        ex_val = expected_value(element, num_die_sides, len_set)
        results_set[element] = ex_val
    
    
    results_list = [(value,key) for key, value in results_set.items()]
    results_list.sort()
    
    print "strategy: result_list ", results_list
    return results_list[len(results_list)-1]


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    
    
#run_example()


#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
                                       
#strategy_.run_suite(strategy)   
#score_test.run_suite(score)
#ex_val_test.run_suite(expected_value)    
    
#ex_val_test_2.run_suite(expected_value)


