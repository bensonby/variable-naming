# Please replace all function names, variable names and constant names

# Hint: dice is the plural form of die

import sys
import random

NUMBER_OF_DICE = 3  # 3 means 3 dice
MAX_NUMBER_IN_DICE = 6  # 6 means the die gives either 1, 2, 3, 4, 5, 6
SMALL_RANGE = (4, 10)  # means 4, 5, 6, 7, 8, 9, 10 are the numbers you win when you bet small
BIG_RANGE = (11, 17)  # means 11, 12, 13, 14, 15, 16, 17 are the numbers you win when you bet big
PAYOUT = {
    'small': 1,
    'big': 1,
    '4': 60,  # means you gain $60 when you bet $1 to a total sum of dice = 4
    '5': 20,
    '6': 18,
    '7': 12,
    '8': 8,
    '9': 6,
    '10': 6,
    '11': 6,
    '12': 6,
    '13': 8,
    '14': 12,
    '15': 18,
    '16': 20,
    '17': 60,
}


def main():
    current_bets = []  # [{'amount': 3, 'type': 'small'}, {'amount': 5, 'type': '11'}] means betting $3 on small, and $5 on total 11
    money = 100  # 100 means you have $100 to play
    while True:
        print("You currently have %s" % money)
        print_menu()
        choice = read_input("Input your choice: ")

        if choice == '1':
            bet = create_bet()
            current_bets.append(bet)
            money = money - bet['amount']

        elif choice == '2':
            dice_results = throw_dice()
            print("Result: %s, %s, %s" % (dice_results[0], dice_results[1], dice_results[2]))
            gain = calculate_gain(dice_results, current_bets)
            money = money + gain
            print("---------------------------------------------------------")
            current_bets = []

        elif choice == '3':
            sys.exit(0)


def print_menu():
    print("1 - Add a bet")
    print("2 - Open")
    print("3 - Exit")


def read_input(prompt_message):  # show prompt_message; wait for user input and return the input
    return input(prompt_message)


def throw_dice():
    results = []
    for i in list(range(0, NUMBER_OF_DICE)):  # list(range(0, 3)) means [0, 1, 2]
        random_number = random.randrange(MAX_NUMBER_IN_DICE) + 1  # random.randrange(6) returns one of (0, 1, 2, 3, 4, 5)
        results.append(random_number)
    return results  # return [3, 4, 2] for example, i.e. the random numbers on the dice


def create_bet():
    input_bet = read_input("Enter the bet (amount and type separated by space): ")  # sample input: "3 small", or "6 16"
    (bet_amount, bet_type) = input_bet.split(' ')
    return {'amount': int(bet_amount), 'type': bet_type}


def calculate_gain(dice_results, bets):  # calculate_gain([3, 4, 2], [{'amount': 3, 'type': 'small'}, {'amount': 5, 'type': '11'}])
    total_gain = 0
    for bet in bets:
        if bet['type'] == 'small':
            if SMALL_RANGE[0] <= sum(dice_results) <= SMALL_RANGE[1]:
                total_gain += bet['amount'] * (1 + PAYOUT['small'])
        elif bet['type'] == 'big':
            if BIG_RANGE[0] <= sum(dice_results) <= BIG_RANGE[1]:
                total_gain += bet['amount'] * (1 + PAYOUT['big'])
        elif int(bet['type']) == sum(dice_results):
            total_gain += bet['amount'] * (1 + PAYOUT[bet['type']])

    return total_gain  # if I bet $3 on small and $5 on 11, and the sum is 9, this will return 6 ($3*2)


if __name__ == "__main__":
    main()
