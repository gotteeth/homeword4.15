import random

items = ['apple', 'banana', 'cherry', 'date', 'elderberry']


selected_item = random.choice(items)

while True:
    user_guess = input("Guess the fruit (apple, banana, cherry, date, elderberry): ")

    if user_guess.lower() == selected_item:
        print("Congratulations! You guessed correctly.")
        break  
    else:
        print("Wrong guess. Try again!")

print(f"The correct fruit was: {selected_item}")
