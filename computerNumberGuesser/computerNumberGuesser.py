import random


min, max = 1, 100
ai_guess = random.randint(min, max)
user_number = int(input("Choose your number: "))
guess_count = 0
print(f'Your number is {user_number}! \nComputer will now guess the number...')


while ai_guess != user_number:
    print(f"Computer guess is {ai_guess}!")
    status = input("high / low: ")
    if status == "high":
        max = ai_guess - 1
        ai_guess = random.randint(min, max)
        guess_count += 1
    elif status == "low":
        min = ai_guess + 1
        ai_guess = random.randint(min, max)
        guess_count += 1


print(f"Your number is {user_number}! It took {guess_count+1} times to guess.")
