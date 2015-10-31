"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    
    new_list = []
    for item in list1:
        if item not in new_list:
            new_list.append(item)
   
    return new_list

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    
    new_list = []
    for item in list1:
        if item in list2:
            new_list.append(item)
    
    return new_list

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    This function can be iterative.
    """   
    new_list = []
    def recur(list1, list2):
        """ 
        recursive merging function
        
        """
        if len(list1) == 0:
            new_list.extend(list2)
            return
        elif len(list2) == 0:
            new_list.extend(list1)
            return
        else:
            if list1[0] <= list2[0]:
                new_list.append(list1[0])
                return recur(list1[1:], list2)
            
            elif list1[0] >= list2[0]:
                new_list.append(list2[0])
                return recur(list1, list2[1:])
    recur(list1, list2)
    
    return new_list

#print merge([1,3,5, 15, 20], [0,2,4, 22])
#print merge([3, 4, 5], [3, 4, 5])
                
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
  
    if len(list1) < 3:
        lista = list1[0:len(list1)/2]
        listb = list1[len(list1)/2:]
        return merge(lista, listb)
    
    else:
        lista = list1[0:len(list1)/2]
        listb = list1[len(list1)/2:]
        print lista, listb
        return merge(merge_sort(lista), merge_sort(listb))
    
    return []

#print merge_sort([3,2,10, 5,6])
#print merge_sort([15,8,3,2, 0])

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    
    if word == "":
        return [""]
    first = word[0]
    rest = word[1:]
    rest_strings = gen_all_strings(rest)
    
    
    print "rest strings", rest_strings
    words_list = []
    for item in rest_strings:
        print "item is ", item
        words_list.append(item)
        for index in range(len(item)+1):
            list_rest = list(item)
            list_rest.insert(index, first)
            new_word = "".join(list_rest)
            words_list.append(new_word)
        
    print words_list
    return words_list

print gen_all_strings("a")

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    return []

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
# run()

    
    
