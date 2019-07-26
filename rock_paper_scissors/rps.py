#!/usr/bin/python

import sys

def rock_paper_scissors(num_players):
  possible_moves = ["rock", "paper", "scissors"]
  result = []
  #This list is how the algo keeps track of what needs to be reset and incremented
  tracker = [0] * num_players

  #If there's no players return empty lists
  if num_players == 0:
    return [[]]
  else:

    # For each possible permutation...
    # (3^n) where n equals the number of players
    for x in range(3 ** num_players):

      # Setup an empty list for this permutation
      # And create a variable to track the next index to be incremented
      result.append([])
      next_increment = 0;

      #For each possible answer
      for y in range(num_players):

        #Append the next move to this permutation
        #According to the associative index in the tracker
        result[-1].append(possible_moves[tracker[y]])

        #Increment the right most number that's not two
        if tracker[y] != 2:
          next_increment = y
      
      #From the item that is being incremented to the end of the list
      for z in range(next_increment,len(tracker)):
        if z == next_increment:
          #Increment the index in the tracker
          tracker[next_increment] += 1
        else:
          #Reset all numbers to the right of the index being incremented
          tracker[z] = 0
      
    return result

  

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')