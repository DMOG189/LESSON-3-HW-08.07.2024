# LESSON 3 EX 6

# if else signs

# we require age bigger than
# 18 and 100,000 balance




# START


age: int = int(input("what's your age?"));
balance: int = int(input("what's your balance?"));

# 1. if , and
# easiest way
# short-circuit logic: if 1st is false do not check 2nd

if age > 18 and balance 100_000:
    print("You are qualified for the program");
else:
    print("You ar NOT qualified for the program");



# if , or
# using or instead of and

if age <= 18 or balance <= 100_000:
    print("You ar NOT qualified for the program");
else:
    print("You are qualified for the program");



# if not , and not ;)
# check the same but with not

if not age <= 18 and not balance <= 100_000:
     print("You are qualified for the program");
 else:
     print("You ar NOT qualified for the program");



# nested if
# check age , only if bigger than 18 then check balance

if age > 18:
    if balance > 100_000:
        print("You are qualified for the program");
    else:
        print("You ar NOT qualified for the program");
else:
    print("You ar NOT qualified for the program");



# END

