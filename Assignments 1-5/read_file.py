"""
Create script to display information obtained from write_file.py

"""

# Function to read and dispaly file content
def read_and_display_file(filename="hackme.txt"):
    try:
        with open(filename, "r") as file:
            print("Here is some information to hack: ")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist")

#Call the function to read the file
read_and_display_file()

