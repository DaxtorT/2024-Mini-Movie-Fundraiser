# Functions Go Here

# Main Routine Goes Here
# Set max # tickets below
MAX_TICKETS = 3

# Loop to sell tickets
tickets_sold = 0
while tickets_sold < MAX_TICKETS:
    name = input("Please enter your name or 'xxx' to quit: ")

    tickets_sold += 1

    if name == "xxx":
        break

# Output number of ticket sold
if tickets_sold == MAX_TICKETS:
    print("Congrats you have sold all the tickets!")

else:
    if name == "xxx":
        tickets_sold -= 1

    print(f"You have sold {tickets_sold} ticket/s. You have {MAX_TICKETS-tickets_sold} ticket/s remaining.")