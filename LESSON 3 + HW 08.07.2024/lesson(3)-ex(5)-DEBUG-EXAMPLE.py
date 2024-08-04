# LESSON 3 EX 5

# read number from  user
# print positive, negative or zero

# START

number: int = int(input("enter a number:"));

if number > 0:
    print(f"{number} is positive!");
else:
    if number < 0:
        print(f"{number} is negative!");
    else:
        print(f"{number} is zero!!!");

# BETTER WAY with elif

if number > 0:
    print(f"{number} is positive!");
elif number < 0:
    print(f"{number} is negative!");
else:
    print(f"{number} is zero!!!");


# END


# enter a number:8
# 8 is positive!
# 8 is positive!



# DEBUG EXPLANATION

# 1.mark the line you want to see in debug mode
# 2.press bug sign right side on the pycharm
# 3.run errors in debug mode by pressing broken
#   error sign in the debug console on the left