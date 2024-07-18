# ferni = one number correct in the correct place
# pico = one number correct but in wrong order
#bagels = no numbers in place
import random
#-------------------------def functions--------------#
def rand_num_gen():
    random_array = []
    counter = 0

    while counter < 10:
        random_number = random.randint(0,9)
        if random_number not in random_array:
            random_array.append(random_number)
        counter += 1

    return random_array[:3]

def usr_input_condition_check():
    numbers = 0
    while True:
        user_input = input("Enter a 3 digit number or 'quit' to exit: \n")

        if user_input.lower() == "quit":
            print("Game quitting...")
            return None

        if not user_input.isdigit():
            print("Integer values are only accepted.\n")
            continue

        if len(user_input) != 3:
            if len(user_input) < 3:
                print("You have an insufficient amount of digits.\n")
            else:
                print("You have exceeded the amount of digits.\n")
            continue

        numbers = int(user_input)
        numbers = [int(digit) for digit in str(numbers)]
        return numbers



def engine(USR_INPUT_VAR, RANDOMLY_GENERATED_VAR):
    if USR_INPUT_VAR == RANDOMLY_GENERATED_VAR:
        return "You got it!"

    clues = []

    for i in range(len(USR_INPUT_VAR)):
        if USR_INPUT_VAR[i] == RANDOMLY_GENERATED_VAR[i]:
            clues.append("Ferni")
        elif USR_INPUT_VAR[i] in RANDOMLY_GENERATED_VAR:
            clues.append("Pico")

    if len(clues) == 0:
        return "Bagels"

    else:
        clues.sort()
        print(" ".join(clues))

def play_game():
    RANDOMLY_GENERATED_VAR = rand_num_gen()
    LIFE_ATTEMPTS = 10

    print("""
            The rules are simple:
    You must guess a three-digit number.
    You have ten attempts.
    The digits will never  duplicate.

    Ferni = one digit is correct in the correct place.
    Pico = One digit is correct but in the wrong place.
    Bagels = No digits are correct in the correct places.
    If you wish to quit the game, type "quit".
        """)

    for attempt in range(LIFE_ATTEMPTS):
        USR_INPUT_VAR = usr_input_condition_check()
        if USR_INPUT_VAR is None:
            return

        result = engine(USR_INPUT_VAR, RANDOMLY_GENERATED_VAR)
        print(result)
        print(f"Attempts remaining: {LIFE_ATTEMPTS - attempt - 1}")

        if result == "You got it!":
            print("Congratulations. You've figured it out!")
            break
    else:
        print(f"Sorry, you've run out of attempts. The correct number was {RANDOMLY_GENERATED_VAR}.")

    play_again = input("Do you wish to play again? yes or no: ").lower()
    if play_again == "yes":
        play_game()
    else:
        print("Thanks for playing!")
play_game()
