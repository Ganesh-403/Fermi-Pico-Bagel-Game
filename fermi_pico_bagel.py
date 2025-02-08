import random

def generate_number(length=3):
    digits = random.sample("0123456789", length)
    return "".join(digits)

def get_user_guess(length):
    while True:
        guess = input(f"Enter your {length}-digit guess (or 'q' to quit): ")
        if guess.lower() == 'q':
            print("Game exited. Thanks for playing!")
            exit()
        if len(guess) != length:
            print(f"Your guess must have exactly {length} digits. Try again.")
            continue
        if len(set(guess)) != len(guess):
            print("Duplicate digits are not allowed. Try again.")
            continue
        if not guess.isdigit():
            print("Only numeric values are allowed. Try again.")
            continue
        return guess

def play_game():
    original_number = generate_number(3)
    print("Welcome to Fermi Pico Bagel!")
    print("Try to guess the secret number. Type 'q' to quit at any time.")

    while True:
        guess_number = get_user_guess(len(original_number))

        output = []
        for i in range(len(original_number)):
            if guess_number[i] == original_number[i]:
                output.append('Fermi')
            elif guess_number[i] in original_number:
                output.append('Pico')

        if guess_number == original_number:
            print(" ".join(['Fermi'] * len(original_number)))
            print("You win!! 🎉")
            break

        if len(output) == 0:
            print("Bagel")
        else:
            print(" ".join(output))

if __name__ == "__main__":
    play_game()
