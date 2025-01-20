# Ask user if today is good y/n
response = input("Is today a good day?: y/n ").lower()
if response == 'y':
    for _ in range(10):
        print("Yeah it is!")
elif response == 'n':
    print("Maybe tomorrow will be better")
else:
    print("Please reinput to ensure that I have the correct response.")
    