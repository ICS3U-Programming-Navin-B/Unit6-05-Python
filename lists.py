#!/usr/bin/env python3

# Created by: Navin Balekomebole
# Created on: Feb 1 2022
# This program gets the user to enter grades until
# they enter -1, it then calculates the average of these grades.


# function to calculate the average of inputs
def calc_average(num_list):
    total = 0
    for current_num in num_list:
        total += current_num
    # calculate and return the average
    average = total / len(num_list)
    return average


def main():
    list_of_grades = []
    # to make sure the list is not empty
    grade_string = input("Enter your grade: ")
    # error checking
    try:
        grade = int(grade_string)
        list_of_grades.append(grade)
        # loop to add additional inputs
        while True:
            grade_string = input("Enter your grade (or -1 to quit): ")
            # error checking
            try:
                grade = int(grade_string)
                # error checking
                if grade < -1:
                    print("Invalid input, try again.")
                    continue
                # for when the user wants to quit
                elif grade == -1:
                    break
                list_of_grades.append(grade)
            except Exception:
                print("Invalid input, try again.")
        # outside of the loop
        average_main = calc_average(list_of_grades)
        # display results
        print("The average is {}". format(average_main))
    except Exception:
        print("Invalid input.")


if __name__ == "__main__":
    main()
