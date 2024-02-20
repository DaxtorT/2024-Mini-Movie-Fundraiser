# Constants Go Here
y_n_list = ["yes", "no"]
payment_method_list = ["cash", "credit"]

# Functions Go Here
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
        print()

def instructions():
    print("Instructions go Here")
    print()

# Main Routine Goes Here
for case in range(0, 5):
    played_before = string_checker("Do you want to see the instructions? ", y_n_list, 1)

    if played_before == "yes":
        instructions()

    payment_method = string_checker("Do you want to pay with Cash or Credit? ", payment_method_list, 2)