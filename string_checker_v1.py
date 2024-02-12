# Constants Go Here
y_n_list = ["yes", "no"]
payment_method_list = ["cash", "credit"]

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

# Main Routine Goes Here
played_before = string_checker("Do you want to see the instructions? ", y_n_list, "Please Choose Yes/No.", "y")

if played_before == "yes":
    instructions()

payment_method = string_checker("Do you want to pay with Cash or Credit? ", payment_method_list, "Please Choose Cash/Credit.", "n")

print(payment_method)