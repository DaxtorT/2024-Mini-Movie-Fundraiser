# Functions Go Here
def num_checker(question):
    while True:
        try:
            response = int(input(question))
            return response
        
        except ValueError:
            print("Please enter a number")

# Main Routine Goes Here
tickets_sold = 0

while True:

    name = input("Enter your name or 'xxx' to quit: ")

    if name == "xxx":
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

    tickets_sold += 1

print(f"You have sold {tickets_sold} tickets.")

