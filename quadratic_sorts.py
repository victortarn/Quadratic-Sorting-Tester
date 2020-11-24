"""Contains 3 functions that sort a list into ascendining order and count
the number of outer loops, inner loops and swaps. One function sorts by
insertion, one by selection and one sorts by bubble.

Authour: Victor Tarnovski
Date 2020-11-18

"""


def insertion(a_list):
    """Takes a list a_list sorts it by insertion and counts the number of
    outer loops, inner loops and swaps"""
    in_loops = 0
    swaps = 0
    for out_loops in range (1, len(a_list)):
        i = out_loops
        while i > 0 and a_list[i-1] > a_list[i]:
            in_loops += 1
            a_list[i-1], a_list[i] = a_list[i], a_list[i-1]
            swaps += 1
            i = i - 1
    return (out_loops, in_loops, swaps)


def selection(a_list):
    """Takes a list a_list sorts it by selection and counts the number of
    outer loops, inner loops and swaps"""
    out_loops = 0
    in_loops = 0
    swaps = 0
    n = len(a_list)
    for i in range(n-1):
        out_loops += 1
        current_min = i
        for j in range (i+1,n):
            in_loops += 1
            if a_list[j] < a_list[current_min]:
                current_min = j
        if current_min != i:
            a_list[i], a_list[current_min] = a_list[current_min], a_list[i]
            swaps += 1
    return (out_loops, in_loops, swaps)


def bubble(a_list):
    """Takes a list a_list sorts it by bubble and counts the number of
    outer loops, inner loops and swaps"""
    size = len(a_list)
    out_loops = 0
    in_loops = 0
    swaps = 0
    
    for i in range (size - 1, -1, -1):
        out_loops += 1
        is_sorted = True
        for j in range(size - 1):
            in_loops += 1
            if a_list[j] > a_list[j + 1]:
                swaps += 1
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
                is_sorted = False
        if is_sorted:
            return out_loops, in_loops, swaps
    return out_loops, in_loops, swaps
