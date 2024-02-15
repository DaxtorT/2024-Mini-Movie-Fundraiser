# Global Variables/Constants Go Here
y_n_list = ["yes", "no"]
payment_method_list = ["cash", "credit"]

MAX_TICKETS = 3
tickets_sold = 0

# Functions Go Here
def string_checker(question, valid_list, error, first_letter):
    while True:
        # Ask user for choice (and force lowercase)
        response = input(question).lower()
        
        # Runs through list and if respose is an item in list (or first letter the full name is returned)
        for item in valid_list:
            # If 'first_letter' is set to yes then check the list for first letter and full strings
            if first_letter == "y":
                if response == item[0] or response == item:
                    return response
            # If 'first_letter' is set to no then only check the list for full strings
            elif first_letter == "n":
                if response == item:
                    return response

        # Output error if response not in list        
        print(error)
        print()

def instructions():
    print("Instructions go Here")
    print()

def not_blank(question):
    while True:
        response = input(question)
        # Checks if response is blank and if not then continues
        if response == "":
            print("Sorry this can't be blank Please try again")
        else:
            return response

def num_checker(question):
    while True:
        try:
            response = int(input(question))
            return response
        
        except ValueError:
            print("Please enter a number")

# Main Routine Goes Here
# Ask user of they want to see instructions
played_before = string_checker("Do you want to see the instructions? ", y_n_list, "Please Choose Yes/No.", "y")

if played_before == "yes":
    instructions()

# Loop to sell tickets
while tickets_sold < MAX_TICKETS:
    name = not_blank("Please enter your name or 'xxx' to quit: ")

    if name == "xxx":
        break

    user_age = num_checker("What is your age? ")

    if 12 <= user_age <= 120:
        pass

    elif user_age < 12:
        print("Sorry you are too young to be watching this movie.")
        continue

    elif user_age > 120:
        print("This may be a typo, please try again.")
        continue

    tickets_sold += 1

# Output number of ticket sold
if tickets_sold == MAX_TICKETS:
    print("Congrats you have sold all the tickets!")

else:
    print(f"You have sold {tickets_sold} ticket/s. You have {MAX_TICKETS-tickets_sold} ticket/s remaining.")