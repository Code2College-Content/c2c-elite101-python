
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


from os import name


def get_user_name():
    return input("Please enter your name: ")

def greet_user(name):
    print(f"Welcome, {name}!")

def main():
    user_name = get_user_name()
    greet_user(user_name)

if __name__ == "__main__":
    main()
print("Hello and welcome to She's Happy Hair!")
print("We’re excited that you're interested in applying for a position with us.")
age = int(input(f"Hi {name}, how old are you? "))
print(f"Thanks for sharing, {name}!")
print("How can I assist you with your job application today?")

print("menu")
choice = input("Enter the number of your choice: ")
if choice == '1' and age >= 18:
        print("You are eligible to continue with the application.")
      # Or you can continue to next steps of the application process
choice == '2' and age < 18
print(f"Sorry, {name}. You must be 18 or older to apply. Best of luck in the future!")
          # End the program or offer a different response
choice == 3
print("You chose to talk to the manager. ") # Option to continue talking to the manager
print("Invalid choice or age not eligible. Please choose a valid option.")
