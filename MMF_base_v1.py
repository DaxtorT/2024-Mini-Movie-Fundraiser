import pandas

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
                    return item
            # If 'first_letter' is set to no then only check the list for full strings
            else:
                if response == item:
                    return item

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

# Function for adding currency formatting
def currency(x):
    return f"${x:.2f}" 

# Global Variables/Constants Go Here
y_n_list = ["yes", "no"]
payment_method_list = ["cash", "credit"]

MAX_TICKETS = 3
tickets_sold = 0

# Lists & Dicts for ticket details
all_names = []
all_ticket_cost = []
all_surcharge = []

mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_cost,
    "Surcharge": all_surcharge
}

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

    # Add 

    # Ask user for cash or credit payment method
    payment_method = string_checker(f"How do you want to pay for your ${ticket_cost:.2f} ticket? ", payment_method_list, 2)
    print()
    print(f"You chose {payment_method}")

    if payment_method == "cash":
        surcharge = 0

    else:
        # Calculate surcharge at 5% if users are paying with credit
        surcharge = ticket_cost * 0.05

    tickets_sold += 1

    # Add ticket name, cost, and surcharge to respective lists
    all_names.append(user_name)
    all_ticket_cost.append(ticket_cost)
    all_surcharge.append(surcharge)

# Output number of ticket sold
if tickets_sold == MAX_TICKETS:
    print("Congrats you have sold all the tickets!")

else:
    print(f"You have sold {tickets_sold} ticket/s. You have {MAX_TICKETS-tickets_sold} ticket/s remaining.")

# Create the pandas table
mini_movie_frame = pandas.DataFrame(mini_movie_dict)
mini_movie_frame = mini_movie_frame.set_index('Name')

# Calculate the total ticket cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] + mini_movie_frame['Ticket Price']

# Calculate the profit for each ticket
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# Calculate ticket and profit totals
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# Currency Formatting (uses currency function)
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

# Table Formatting
print("---- Ticket Data ----")
print()

# Output table with ticket data
print(mini_movie_frame)
print()

print("---- Total Cost & Profit ----")
print()

# Output total ticket sales and profit
print(f"Total Ticket Sales: ${total:.2f}")
print(f"Total Profit: ${profit:.2f}")