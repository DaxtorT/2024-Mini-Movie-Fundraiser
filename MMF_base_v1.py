import pandas
import random
from datetime import date

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

# Function for showing instructions
def show_instructions():
    print('''
***** Instructions *****
          
For each ticket, enter ...
- The Person's Name (Can't be blank)
- Age (Between 12 and 120)
- Payment Method (Cash / Credit)

When you have entered all the users, press 'xxx' to quit.
          
The program will then display the ticket details 
including the cost for each ticket, the total 
cost and total profit.
          
This information will automatically be written to 
a text file
          
************************''')

# Global Variables/Constants Go Here
y_n_list = ["yes", "no"]
payment_method_list = ["cash", "credit"]

MAX_TICKETS = 100
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
    show_instructions()

# Loop to sell tickets
while tickets_sold < MAX_TICKETS:
    user_name = not_blank("Please enter your name or 'xxx' to quit: ")

    if user_name == "xxx" and len(all_names) > 0:
        break
    elif user_name == "xxx":
        print("You must sell at least ONE ticket before quitting")
        continue

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
    payment_method = string_checker("How do you want to pay for your ticket? ", payment_method_list, 2)
    print(f"You chose {payment_method}")
    print()

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

# Print me
print()

# Create the pandas table
mini_movie_frame = pandas.DataFrame(mini_movie_dict)\

# Calculate the total ticket cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] + mini_movie_frame['Ticket Price']

# Calculate the profit for each ticket
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# Calculate ticket and profit totals
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# Raffle Winner Stuff
# Choose a winner name and loop up total won
winner_name = random.choice(all_names)
win_index = all_names.index(winner_name)
total_won = mini_movie_frame.at[win_index, 'Total']

# Set index at end (before printing)
mini_movie_frame = mini_movie_frame.set_index('Name')

# All Date, Heading and Filename Stuff
# Get today's date
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%y")

heading = f"***** The Current Date is {day}/{month}/{year} *****"
filename = f"MMF_{day}_{month}_{year}"

# Currency Formatting (uses currency function)
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

# All File Export Stuff
# Change frame to a sting so we can export to file
mini_movie_string = pandas.DataFrame.to_string(mini_movie_frame)

# Crate strings for printing
ticket_cost_heading = "\n---- Ticket Cost / Profit ----"
total_ticket_sales = f"Total Ticket Sales: ${total}"
total_profit = f"Total Profit: {profit}"

# Output number of ticket sold
tickets_sold_heading = "\n---- Tickets Sold ----"
if tickets_sold == MAX_TICKETS:
    sales_status = "Congrats you have sold all the tickets!"

else:
    sales_status = f"You have sold {tickets_sold} ticket/s. You have {MAX_TICKETS-tickets_sold} ticket/s remaining."

winner_heading = "\n---- Raffle Winner ----"
winner_text = f"The Winner of the raffle is {winner_name}. " \
              f"They have won ${total_won:.2f}. ie: Their Ticket is free!"

# List holding content to print / write to file
to_write = [heading, mini_movie_string, ticket_cost_heading, total_ticket_sales, total_profit, tickets_sold_heading, sales_status, winner_heading, winner_text]

# Print output
for item in to_write:
    print(item)

# Write output to file
# Create file to hold data (add .txt extension)
write_to = f"{filename}.txt"
text_file = open(write_to, "w+")

for item in to_write:
    text_file.write(item)
    text_file.write("\n")

text_file.close()

# Note to me
print(f"\nYou will find this sale's information in the file named '{filename}.txt'\n")