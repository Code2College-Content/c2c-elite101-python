
"""
    Welcome to Elite 101 this program is a starter for your chatbot project.
    The starter prompts the user to enter their name and then greets them with a personalized message.

    Functions:
        get_user_name(): Prompts the user to enter their name and returns it.
        greet_user(name): Prints a greeting message using the provided name.
        main(): Main function that orchestrates the user input and greeting process.

    Execution:
        When the script is run directly (not imported as a module), it will execute the main() function.
"""


def get_user_name():
    return input("Please enter your name: ")

def greet_user(name):
    print(f"Hello, {name}, how are you?")

def chat():
    print("\nMenu:")
    print("1: Store hours")
    print("2: Product availability")
    print("0: Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        print("We are open 9 AM to 8 PM.")
    elif choice == "2":
        print("That item is in stock.")
    elif choice == "0":
        print("Goodbye!")

def main():
    user_name = get_user_name()
    greet_user(user_name)
    chat():

if __name__ == "__main__":
    main()
