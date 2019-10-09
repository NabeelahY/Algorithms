#!/usr/bin/python

import argparse


def find_max_profit(prices):
    current_min_price_so_far = prices[0]
    max_profit_so_far = 0

    for i in range(len(prices)):
        if current_min_price_so_far > prices[i]:
            current_min_price_so_far = prices[i]
        if max_profit_so_far < prices[i]:
            max_profit_so_far = prices[i]

    result = max_profit_so_far - current_min_price_so_far
    return result


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
