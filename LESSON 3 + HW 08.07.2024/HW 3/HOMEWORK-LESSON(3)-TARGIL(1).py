# HOMEWORK LESSON 3 TARGIL 1

# Write a program that gets an
# id (str) ,
# fname , lname (str)
# height (float)
# year of birth (int)
# print all back

# self bonus add if else terms

# START

id: str = str(input("whats your id number?"));
fname: str = str(input("whats your first name?"));
lname: str = str(input("last name please?"));
height: float = float(input("whats your height?"));
yob: str = str(input("what year where you born?"));

print(f"#ID: {id} NAME: {fname} {lname} Height: {height} Year of birth: {yob}");

balance: float = float(input("What is your current bank balance?"));

if balance < 100000:
    print("Not valid");

else:
    print("valid");

# END




# whats your id number?1
# whats your first name?daniel
# last name please?mizrahi
# whats your height?1.75
# what year where you born?1997
# ID: 1 NAME: daniel mizrahi Height: 1.75 Year of birth: 1997
# What is your current bank balance?50000
# Not valid
