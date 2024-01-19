import random
import string


def generate_password(length):

    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation


    all_characters = lowercase_letters + uppercase_letters + digits + special_characters


    length = max(length, 8)


    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password


def main():

    try:
        length = int(input("Enter the desired password length: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return


    password = generate_password(length)
    print(f"\nGenerated Password: {password}")


if __name__ == "__main__":
    main()

