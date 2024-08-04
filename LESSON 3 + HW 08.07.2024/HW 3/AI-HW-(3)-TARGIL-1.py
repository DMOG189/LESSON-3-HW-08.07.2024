# this is how the ai did it



# Function to get user details
def get_user_details():
    user_id = input("Enter your ID: ")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    height = float(input("Enter your height (in meters): "))
    year_of_birth = int(input("Enter your year of birth: "))
    balance = float(input("Enter your account balance: "))

    return user_id, first_name, last_name, height, year_of_birth, balance


# Function to print user details and qualification status
def print_user_details(user_id, first_name, last_name, height, year_of_birth, balance):
    print("\nUser Details:")
    print(f"ID: {user_id}")
    print(f"First Name: {first_name}")
    print(f"Last Name: {last_name}")
    print(f"Height: {height} meters")
    print(f"Year of Birth: {year_of_birth}")
    print(f"Balance: {balance} ILS")

    if balance > 100000:
        print("Status: Qualified")
    elif height > 1.85:
        print("Status: Qualified")
    else:
        print("Status: Not Qualified")


# Main function
def main():
    user_id, first_name, last_name, height, year_of_birth, balance = get_user_details()
    print_user_details(user_id, first_name, last_name, height, year_of_birth, balance)


# Run the main function
if __name__ == "__main__":
    main()

# Enter your ID: 1
# Enter your first name: Daniel
# Enter your last name: Mizrahi
# Enter your height (in meters): 1.86
# Enter your year of birth: 1997
# Enter your account balance: 20000

# User Details:
# ID: 1
# First Name: Daniel
# Last Name: Mizrahi
# Height: 1.86 meters
# Year of Birth: 1997
# Balance: 20000.0 ILS
# Status: Qualified

# Process finished with exit code 0
