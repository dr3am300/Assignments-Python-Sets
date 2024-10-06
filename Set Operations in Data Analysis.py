# Objective: The aim of this assignment is to enhance your skills in using Python sets for data analysis tasks. 
# You will apply various set operations to handle real-world data scenarios, focusing on their practical application and efficiency.
# Task 1: Duplicate Entries Cleanup You are given a list of customer IDs, some of which are duplicated. Write a Python script to remove duplicates and display the unique customer IDs.
# Example Code:
# customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
# Expected Outcome: A set of unique customer IDs, ensuring no duplicates. For instance, `{'C001', 'C002', 'C003', 'C004'}`. ---
# Ensure that all code in your file is ready to run. 
# This means that if someone opens your file and clicks the run button at the top, all code executes as intended. 
# For example, if there are if statements, print statements, or for loops, they should function correctly and display output in the console as expected. 
# If you have a function, make sure the function is called and runs.
# The goal of this note is to ensure that all code in your Python file runs smoothly and that is has been tested.

def duplicate_entries_cleanup():
    customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
    unique_customer_ids = set(customer_ids)
    print("Unique Customer IDs: ", unique_customer_ids)
    would_you_like_to_continue()
def show_original_customer_ids():
    customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
    print("Original Customer IDs: ", customer_ids)
    would_you_like_to_continue()
def would_you_like_to_continue():
    continue_program = input("Would you like to continue? [YES] Yes [NO] No: ").upper()
    if continue_program == "YES":
        main()
    elif continue_program == "NO":
        print("Thank you for using the program. shutting down... in 10 seconds.")
        countdown = 10
        while countdown > 0:
            print(countdown)
            countdown -= 1
        print("Goodbye!")
    else:
        print("Invalid input. Please try again.")
        would_you_like_to_continue()
def main():
    print("Welcome to the Duplicate Entries Cleanup Program.")
    print("Please select an option below:")
    print("[1] Remove Duplicate Entries")
    print("[2] Show Original Customer IDs")
    print("[3] Exit Program")
    user_input = input("Please select an option: ")
    if user_input == "1":
        duplicate_entries_cleanup()
    elif user_input == "2":
        show_original_customer_ids()
    elif user_input == "3":
        are_you_sure = input("Are you sure you want to exit the program? [YES] Yes [NO] No: ").upper()
        if are_you_sure == "YES":
            print("Thank you for using the program. shutting down... in 10 seconds.")
            countdown = 10
            while countdown > 0:
                print(countdown)
                countdown -= 1
            print("Goodbye!")
        elif are_you_sure == "NO":
            main()
        else:
            print("Invalid input. Please try again.")
            main()
            
while True:
    main()
    break
