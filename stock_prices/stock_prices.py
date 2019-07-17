#!/usr/bin/python

import argparse

def find_max_profit(prices):
  #Receives a list of stock prices
  #Return the maximum profit that can be made from a single buy and sell.
  #You must buy first before selling; no shorting is allowed here.

  x = 0
  z = 0
  max_profit = None;

  while x < len(prices):
    while z < len(prices):
      if not max_profit:
        max_profit = prices[z] - prices[x]
      elif x != z and x < z and prices[z] - prices[x] > max_profit:
        max_profit = prices[z] - prices[x]
      z += 1
    x += 1
    z = 0

  return max_profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))