'''
Project: Binary Search Tree
Author: Parker Thurston
Course: CS 2420 Data Structures and Algorithms
Date: 11/05/21

Description: Imported a txt file and stored the occurance 
of each alphabetic and numeric character in a Binary Search Tree

Lessons Learned: The basics of BSTs

'''
from pathlib import Path
from string import whitespace, punctuation
from bst import BST


class Pair:
    ''' Encapsulate letter,count pair as a single entity.
    
    Realtional methods make this object comparable
    using built-in operators. 
    '''
    def __init__(self, letter, count = 1):
        self.letter = letter
        self.count = count
    
    def __eq__(self, other):
        return self.letter == other.letter
    
    def __hash__(self):
        return hash(self.letter)

    def __ne__(self, other):
        return self.letter != other.letter

    def __lt__(self, other):
        return self.letter < other.letter

    def __le__(self, other):
        return self.letter <= other.letter

    def __gt__(self, other):
        return self.letter > other.letter

    def __ge__(self, other):
        return self.letter >= other.letter

    def __repr__(self):
        return f'({self.letter}, {self.count})'
    
    def __str__(self):
        return f'({self.letter}, {self.count})'

def make_tree():
    ''' A helper function to build the tree.
    
    The test code depends on this function being available from main.
    :param: None
    :returns: A binary search tree
    '''
    file = open("around-the-world-in-80-days-3.txt", "r")
    root= None
    lyst = ["!",'"',"'","(",")","-",".",":",';',"?", "`"]
    mylist = [' ',',','\n']
    while 1:
        char = file.read(1)
        if not char:
            break
        if(char not in mylist):
            if(char not in lyst):
                bst = BST(char)
                root=bst.add(root,char)
    
    return BST(root)

def main():
    ' Program kicks off here.'
    bst = make_tree()
    print(bst.inorder())
    
if __name__ == "__main__":
    main()
