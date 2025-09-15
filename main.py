
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


print("Welcome to the Elite 101 Chatbot!")
name = input("Enter your name:  ")
age = input("Hello " + name + ", what is your age? " )
print("Welcome " + name +". What a wonderful age it is to be " + age + "!")
print("")

cycle = 1
print("How may I assist you today? Please choose the number of an option listed below.")
def Option_one():
    print("Option One")
def Option_two():
    print("Option Two")
def Option_three():
    print("Option Three")
def Exit_chatbot():
    print("Exit")
    cycle = 0

chatbot_options = ["1. Option 1", "2. Option 2", "3. Option 3", "4. Exit Chatbot"]
for option in chatbot_options:
    print(option)
user_choice = input("Option chosen: ")

while cycle ==1:
    if user_choice ==1:
        Option_one()
    elif user_choice==2:
        Option_two()
    elif user_choice==3:
        Option_three()
    else:
        break
print("Good bye " + name + ". Have a great rest of your day!")
