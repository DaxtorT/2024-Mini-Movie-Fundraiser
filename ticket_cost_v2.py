import pandas

def currency(x):
    return f"${x:.2f}"

# Lists & Dictionaries to hold ticket details
all_names = ["a", "b", "c", "d", "e"]
all_ticket_cost = [7.50, 7.50, 10.50, 10.50, 6.50]
surcharge = [0, 0, 0.53, 0.53, 0]

mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_cost,
    "Surcharge": surcharge
}

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