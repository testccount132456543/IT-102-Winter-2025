"""
This script asks the user if today is a good day and includes a 
function to print through a iteration x - 10
"""

def send_message():
    """
    Prints a positive message and says yeah it is 10 times
    """
    for _ in range(10):
        print("Yeah it is!")

# Ask user if today is good y/n
response = input("Is today a good day?: y/n ").lower()


if response == 'y':
    # Call function to print
    send_message()

elif response == 'n':
    print("Maybe tomorrow will be better")


else:
    print("Please reinput to ensure that I have the correct response.")
    