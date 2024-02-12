# Functions Go Here
def yes_no_checker(question):
    while True:
        y_n_input = input(question).lower()
        if y_n_input == "yes" or y_n_input == "y":
            return "yes"

        elif y_n_input == "no" or y_n_input == "n":
            return "no"
        
        else:
            print("Please Answer Yes/No")

def instructions():
    print("Instructions go Here")

# Main Routine Goes Here
played_before = yes_no_checker("Do you want to see the insrtuctions? ")

if played_before == "yes":
    instructions()