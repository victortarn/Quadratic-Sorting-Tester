# Quadratic-Sorting-Tester
Analyzes the effectiveness of sorting by insertion, selection and bubble.
Written using python 3.

list_generator.py is a module that has three functions: 
list_ascending(a_length) creates a random list in ascending order that is a_length long
list_descending(a_length) creates a random list in descending order that is a_length long
list_randomized(a_length) creates a randomized list that is a_length long

quadratic_sorts.py is a module that has three functions:
insertion(a_list) Takes a_list and sorts it in ascending order using insertion and returns the number of outer-loops, inner-loops and swaps.
selection(a_list) Takes a_list and sorts it in ascending order using selection and returns the number of outer-loops, inner-loops and swaps.
bubble(a_list) Takes a_list and sorts it in ascending order using bubble sort and returns the number of outer-loops, inner-loops and swaps.

A3_2.py asks the user for the length of the list and then outputs a random ascending list, a random descending list and a randomized list using list_generator.py
It then sorts each list using the 3 sorting algorithims in quadratic_sorts.py
Then it outputs a table for each sorting algorithim that has the number of outer-loops, inner-loops and swaps fpr each list.
