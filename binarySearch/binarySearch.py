def binarySearch():
    numbers = []
    for i in range(1, 101):
        numbers.append(i)

    min, max = numbers[0], numbers[99]
    guess_count = 0
    while min <= max:
        med = int((min + max) / 2)
        if med == user_number:
            print(f"Your number is {user_number}! It took computer {guess_count} times to guess.")
            break
        elif user_number > med:
            min = med + 1
            guess_count += 1
        elif user_number < med:
            max = med - 1
            guess_count += 1


user_number = int(input("Choose your number: "))
print(f'Computer will now try to guess the number...')
binarySearch()
