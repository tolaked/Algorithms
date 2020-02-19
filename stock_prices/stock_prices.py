#!/usr/bin/python

import argparse

def find_max_profit(prices):
    if prices[0] == max(prices):
      prices.remove(prices[0])
      max_price = max(prices)
    else:
      max_price = max(prices)

    min_sell = prices.index(max_price)
    min_prices = prices[:min_sell + 1]
    smallest_price = min(min_prices)
    maximum_profit = max_price - smallest_price
    return maximum_profit

    

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))