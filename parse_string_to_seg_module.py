
'''
Ramzi Adil
CS5700
Spring 2021
Assignment 1: Sockets

This file is meant to run on python v. 3.6.8

link to assignment: https://david.choffnes.com/classes/cs4700sp22/project1.php

The purpose of this file is to have a function that
can parse a string tree expression into segments
stored in a dictionary.

The format of the strings to parse is:
    > txpr := [int] | '(' [txpr] [op] [txpr] ')'
operators that are available are
    > op   := '+' | '-' | '*' | '//' | '<<^'
    > 'a // b' := floor[a / b]
    > 'a <<^ b' := (a << 13) (xor) b
All integers in the tree are 32-bit signed integers,
    however, the result of the calculation must have infinite precision
'''

OPERATORS = ["+","-", "*","//","<<^"] # constant list


def parse_string_to_dict(expr : str) -> list:
    '''
    This function will parse a string txpr into
    segments of operator, left and right expression
    to be stored in a dictionary
    :param expr: a mathematical expression as a string
        > format of the string is:
        txpr := [int] | '(' [txpr] [op] [txpr] ')'
    :return: a dictionary containing the segments
        > ex: "( a + b )" will yield a dictionary of
            dictionary[op] = "+"
            dictionary[left] = "a"
            dictionary[right] = "b"
        > if dictionary[op] not in OPERATORS then its a single int i.e.
        ex: "a" will yield dictionary of
            dictionary[op] = "a"
            dictionary[left] = None
            dictionary[right] = None
    '''

    expr_lst = expr.split(" ")
    negative_len_list = -(len(expr_lst)) - 1 #used to iterate list backwards
    right_paren_count = 0 # counts amount of right parentheses "scanned"
    item_dict = {} # dictionary to return

    if len(expr_lst) > 1: # if txpr NOT just an int
        for i in range(-1, negative_len_list, -1):
            #TODO delete x
            x = expr_lst[i]
            if expr_lst[i].isnumeric():
                #if number and no right paren encounter
                if right_paren_count == 0:
                    break
                else:
                    continue
            elif expr_lst[i] == ")":
                right_paren_count += 1
                continue
            elif expr_lst[i] == "(":
                right_paren_count -= 1
                continue
            elif expr_lst[i] in OPERATORS:
                if right_paren_count == 1:
                    operator_split_pos = i
                    break

        operator = expr_lst[operator_split_pos]
        # left expression does not have an empty space on the right side/end of expression
        # outer paren pair is removed via list slice
        left_expr = " ".join(expr_lst[negative_len_list + 2:operator_split_pos])
        # TODO WARNING Possible error point: maybe don't include ) paren below
        right_expr = " ".join(expr_lst[operator_split_pos + 1:-1])
        item_dict["op"] = operator
        item_dict["left"] = left_expr
        item_dict["right"] = right_expr
    else:
        item_dict["op"] = expr_lst[0]
        item_dict["left"] = None
        item_dict["right"] = None

    return item_dict

def isInt(value : str):
    try:
        float(value)
        return True
    except ValueError:
        return False

def left_and_XOR(a : int, b : int):
    #'a <<^ b' := (a << 13)(xor) b
    return ( ( a << 13 ) ^ b)

def parse_input_to_useable():
    x = ""
    counter = 1
    y = input("input line {}\n".format(counter))

    while y != "":
        x += y
        counter += 1
        y = input("input line {}\n".format(counter))

    print(x)


def main():
    x = []
    with open("sample.txt", 'r') as simple:
        for each in simple.readlines():
            y = each.strip("\n")
            x.append(y)
    print(" ".join(x))

#main()