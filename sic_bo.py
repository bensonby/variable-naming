# Please replace all function names, variable names and constant names

# Hint: dice is the plural form of die

import sys
import random

CONSTANT_A = 3  # 3 means 3 dice
CONSTANT_B = 6  # 6 means the die gives either 1, 2, 3, 4, 5, 6
CONSTANT_C = (4, 10)  # means 4, 5, 6, 7, 8, 9, 10 are the numbers you win when you bet small
CONSTANT_D = (11, 17)  # means 11, 12, 13, 14, 15, 16, 17 are the numbers you win when you bet big
CONSTANT_E = {
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
    variable_m1 = []  # [{'amount': 3, 'type': 'small'}, {'amount': 5, 'type': '11'}] means betting $3 on small, and $5 on total 11
    variable_m2 = 100  # 100 means you have $100 to play
    while True:
        print("You currently have %s" % variable_m2)
        function_a()
        variable_m3 = function_b("Input your choice: ")

        if variable_m3 == '1':
            variable_m4 = function_d()
            variable_m1.append(variable_m4)
            variable_m2 = variable_m2 - variable_m4['amount']

        elif variable_m3 == '2':
            variable_m5 = function_c()
            print("Result: %s, %s, %s" % (variable_m5[0], variable_m5[1], variable_m5[2]))
            variable_m6 = function_e(variable_m5, variable_m1)
            variable_m2 = variable_m2 + variable_m6
            print("---------------------------------------------------------")
            variable_m1 = []

        elif variable_m3 == '3':
            sys.exit(0)


def function_a():
    print("1 - Add a bet")
    print("2 - Open")
    print("3 - Exit")


def function_b(variable_b1):  # show variable_b1; wait for user input and return the input
    return input(variable_b1)


def function_c():
    variable_c1 = []
    for i in list(range(0, CONSTANT_A)):  # list(range(0, 3)) means [0, 1, 2]
        variable_c2 = random.randrange(CONSTANT_B) + 1  # random.randrange(6) returns one of (0, 1, 2, 3, 4, 5)
        variable_c1.append(variable_c2)
    return variable_c1  # return [3, 4, 2] for example, i.e. the random numbers on the dice


def function_d():
    variable_d1 = function_b("Enter the bet (amount and type separated by space): ")  # sample input: "3 small", or "6 16"
    (variable_d2, variable_d3) = variable_d1.split(' ')
    return {'amount': int(variable_d2), 'type': variable_d3}


def function_e(variable_e3, variable_e4):  # function_e([3, 4, 2], [{'amount': 3, 'type': 'small'}, {'amount': 5, 'type': '11'}])
    variable_e1 = 0
    for variable_e2 in variable_e4:
        if variable_e2['type'] == 'small':
            if CONSTANT_C[0] <= sum(variable_e3) <= CONSTANT_C[1]:
                variable_e1 += variable_e2['amount'] * (1 + CONSTANT_E['small'])
        elif variable_e2['type'] == 'big':
            if CONSTANT_D[0] <= sum(variable_e3) <= CONSTANT_D[1]:
                variable_e1 += variable_e2['amount'] * (1 + CONSTANT_E['big'])
        elif int(variable_e2['type']) == sum(variable_e3):
            variable_e1 += variable_e2['amount'] * (1 + CONSTANT_E[variable_e2['type']])

    return variable_e1  # if I bet $3 on small and $5 on 11, and the sum is 9, this will return 6 ($3*2)


if __name__ == "__main__":
    main()
