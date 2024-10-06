# Objective: The aim of this assignment is to deepen your understanding and application of Python sets.
# Task 1: Flight Route Comparison Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. 
# You have two sets of flight destinations, one for each airline. 
# Write a Python program to find out:
# 1. Destinations that both airlines fly to.
# 2. Destinations unique to your airline.
# 3. Whether there are any destinations that neither airline shares.
# Example Code:
# our_routes = {"LAX", "JFK", "CDG", "DXB"}
# competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
    
def compare_flight_routes():
    our_routes = {"LAX", "JFK", "CDG", "DXB"}
    competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
    print("Destinations that both airlines fly to: ", our_routes.intersection(competitor_routes))
    print("Destinations unique to your airline: ", our_routes.difference(competitor_routes))
    print("Destinations unique to the competitor: ", competitor_routes.difference(our_routes))
    print("Whether there are any destinations that neither airline shares: ", our_routes.symmetric_difference(competitor_routes))
    would_you_like_to_continue()
def unique_to_your_airline():
    our_routes = {"LAX", "JFK", "CDG", "DXB"}
    competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
    print("Destinations unique to your airline: ", our_routes.difference(competitor_routes))
    would_you_like_to_continue()
def neither_airline_shares():
    our_routes = {"LAX", "JFK", "CDG", "DXB"}
    competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
    print("Whether there are any destinations that neither airline shares: ", our_routes.symmetric_difference(competitor_routes))
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
        exit()
    else:
        print("Invalid input. Please try again.")
        would_you_like_to_continue()
def main():
    print("Welcome to the Flight Route Comparison Program.")
    print("Please select an option below:")
    print("[1] Compare Flight Routes")
    print("[2] Destinations Unique to Your Airline")
    print("[3] Destinations Neither Airline Shares")
    print("[4] Exit Program")
    user_input = input("Please select an option: ")
    if user_input == "1":
        compare_flight_routes()
    elif user_input == "2":
        unique_to_your_airline()
    elif user_input == "3":
        neither_airline_shares()
    elif user_input == "4":
        are_you_sure = input("Are you sure you want to exit the program? [YES] Yes [NO] No: ").upper()
        if are_you_sure == "YES":
            print("Thank you for using the program. shutting down... in 10 seconds.")
            countdown = 10
            while countdown > 0:
                print(countdown)
                countdown -= 1
            print("Goodbye!")
            exit()
        elif are_you_sure == "NO":
            main()
    else:
        print("Invalid input. Please try again.")
        main()
if __name__ == "__main__":
    main()

while True:
    try:
        main()
    except:
        print("An error occurred. Please try again.")
        continue
    

        
