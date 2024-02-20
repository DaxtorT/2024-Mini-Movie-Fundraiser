# Global Variables/Constants Go Here
y_n_list = ["yes", "no"]
payment_method_list = ["cash", "credit"]

MAX_TICKETS = 3
tickets_sold = 0

# Functions Go Here
# Function for checking if input is a valid answer (checks from 'valid_list')
def string_checker(question, valid_list, num_letters):
    while True:      
        # Error message generation
        error = f"Please choose {valid_list[0]} or {valid_list[1]}"

        # Ask user for choice (and force lowercase)
        response = input(question).lower()
        
        # Runs through list and if response is an item in list (or first letter the full name is returned)
        for item in valid_list:
            # If 'first_letter' is set to yes then check the list for first letter and full strings
            if num_letters > 0:
                if response == item[:num_letters] or response == item:
                    return response
            # If 'first_letter' is set to no then only check the list for full strings
            else:
                if response == item:
                    return response

        # Output error if response not in list        
        print(error)

# Function for printing instructions
def instructions():
    print("Instructions go Here")
    print()

# Function for checking string is not blank
def not_blank(question):
    while True:
        response = input(question)
        # Checks if response is blank and if not then continues
        if response == "":
            print("Sorry this can't be blank Please try again")
        else:
            return response

# Function for checking a number is valid
def num_checker(question):
    while True:
        try:
            response = int(input(question))
            return response
        
        except ValueError:
            print("Please enter a number")

# Function for calculating ticket price
def calc_ticket_price(var_age):
    # If/Elif loop for checking age
    # Price is $7.50 for under 16s
    if 12 <= var_age <= 15:
        price = 7.50
    # Price is $10.50 for 16 - 64
    elif 16 <= var_age <= 64:
        price    = 10.5
    # Price is $6.50 for seniors (64+)
    elif 65 <= var_age <= 120:
        price = 6.5
    
    return price

# Main Routine Goes Here
# Ask user of they want to see instructions
played_before = string_checker("Do you want to see the instructions? ", y_n_list, 1)

if played_before == "yes":
    instructions()

# Loop to sell tickets
while tickets_sold < MAX_TICKETS:
    user_name = not_blank("Please enter your name or 'xxx' to quit: ")

    if user_name == "xxx":
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

    # Calculate the cost of the ticket
    ticket_cost = calc_ticket_price(user_age)

    # Ask user for cash or credit payment method
    payment_method = string_checker(f"How do you want to pay for your ${ticket_cost:.2f} ticket? ", payment_method_list, 2)
    print()

    tickets_sold += 1

# Output number of ticket sold
if tickets_sold == MAX_TICKETS:
    print("Congrats you have sold all the tickets!")

else:
    print(f"You have sold {tickets_sold} ticket/s. You have {MAX_TICKETS-tickets_sold} ticket/s remaining.")