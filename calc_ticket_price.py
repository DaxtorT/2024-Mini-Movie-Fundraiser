# Functions Go Here
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
while True:

    # Get users age
    age = int(input("Age: "))

    # Calculate ticket price
    ticket_cost = calc_ticket_price(age)
    print(f"Age: {age}, Ticket Price: ${ticket_cost:.2f}")