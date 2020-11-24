"""Contains 3 functions that take a value a_length and creates a list that
is a_length long and either creates a random ascending list, random
descending list or a completely randomized list

Authour: Victor Tarnovski
Date 2020-11-18

"""

import random

best_list = []
worst_list = []
rand_list = []

def list_ascending(a_length):
    """"Takes a value a_length and generates an ascending list of this
    length"""
    i = 0
    x = 0
    while i < a_length:
        y = round(random.uniform(x, 100), 2)
        best_list.append(y)
        x = y
        i += 1
    return best_list


def list_descending(a_length):
    """"Takes a value a_length and generates a descending list of this
    length"""
    i = 0
    x = 100
    while i < a_length:
        y = round(random.uniform(0, x), 2)
        worst_list.append(y)
        x = y
        i += 1
    return worst_list


def list_randomized(a_length):
    """"Takes a value a_length and generates a random list of this
    length"""
    i = 0
    while i < a_length:
        rand_list.append(round(random.uniform(0, 100), 2))
        i += 1
    return rand_list
