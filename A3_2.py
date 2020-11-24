"""Program that a value a_length and generates an asceding, descending and
randomized list of that length. Then it sorts it in ascedning order using
insertion, selection and bubble and then compares their performance.

Authour: Victor Tarnovski
Date 2020-11-18

"""
import list_generator
import quadratic_sorts


def main():
    while True:
        a_length = input("Please enter the length of the list: ")
        if a_length.isdigit():
            a_length = int(a_length)
            break
        else:
            print("Please enter a valid input")
    print("\n")

    best_case = list_generator.list_ascending(a_length)
    worst_case = list_generator.list_descending(a_length)
    rand_case = list_generator.list_randomized(a_length)
    print("Best-case example: ", best_case)
    print("Worst-case example: ", worst_case)
    print("Randomized example: ", rand_case)
    print("\n")

    #Insertion Sort
    print("Insertion Sort:")
    a = {"Best-case": quadratic_sorts.insertion(best_case.copy()),
    "Worst-case": quadratic_sorts.insertion(worst_case.copy()),
    "Randomized-case": quadratic_sorts.insertion(rand_case.copy()),}

    print ("{:<20} {:<20} {:<20} {:<20}".format('','# of outer loops'
    ,'# of innner loops','# of swaps'))

    for k, v in a.items():
        inner, outer, swap = v
        print ("{:<20} {:<20} {:<20} {:<20}".format(k, inner, outer, swap))
    print("\n")

    #Selection Sort
    print("Selection Sort:")
    b = {"Best-case": quadratic_sorts.selection(best_case.copy()),
    "Worst-case": quadratic_sorts.selection(worst_case.copy()),
    "Randomized-case": quadratic_sorts.selection(rand_case.copy()),}

    print ("{:<20} {:<20} {:<20} {:<20}".format('','# of outer loops'
    ,'# of innner loops','# of swaps'))

    for x, y in b.items():
        inner, outer, swap = y
        print ("{:<20} {:<20} {:<20} {:<20}".format(x, inner, outer, swap))
    print("\n")

    #Bubble Sort
    print("Bubble Sort:")
    d = {"Best-case": quadratic_sorts.bubble(best_case.copy()),
    "Worst-case": quadratic_sorts.bubble(worst_case.copy()),
    "Randomized-case": quadratic_sorts.bubble(rand_case.copy()),}

    print ("{:<20} {:<20} {:<20} {:<20}".format('','# of outer loops'
    ,'# of innner loops','# of swaps'))

    for k, v in d.items():
        inner, outer, swap = v
        print ("{:<20} {:<20} {:<20} {:<20}".format(k, inner, outer, swap))

main()
