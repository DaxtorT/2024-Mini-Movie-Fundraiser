# Functions Go Here
def not_blank(question):
    while True:
        response = input(question)
        # Checks if response is blank and if not then continues
        if response == "":
            print("Sorry this can't be blank Please try again")
        else:
            return response
        
# Main Routine Goes Here
while True:
    name = not_blank("Enter your name (or 'xxx' to quit) ")
    if name == "xxx":
        break

print("We are done")