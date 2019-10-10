#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # current minimum price at hand will be the first value of prices
    current_min_price_so_far = prices[0]
    # max profit will be next value in prices - current min price
    max_profit_so_far = prices[1] - current_min_price_so_far

    # Loop through other values in prices list to compare
    for i in range(1, len(prices) - 1):
        # Calculate the next profit by subtracting the previous from the current value
        new_profit = prices[i] - current_min_price_so_far
        # Compare new profit with previous profit
        if new_profit > max_profit_so_far:
            # if greater than the profit, replace it with the larger profit
            max_profit_so_far = new_profit
        # if previous min is greater current value, replace it with the current value
        if current_min_price_so_far > prices[i]:
            current_min_price_so_far = prices[i]

    return max_profit_so_far


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers',
                        metavar='N',
                        type=int,
                        nargs='+',
                        help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".
          format(profit=find_max_profit(args.integers), prices=args.integers))
