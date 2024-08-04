# LESSON 3 TARGIL 6 {BONUS}


# LIKE IN EX 1 ADD 2 MORE USERS
# Write a program that gets an
# id (str) ,
# fname , lname (str)
# height (float)
# year of birth (int)
# print all back FOR ALL USERS!!!


# START


id1: str = str(input("whats your id number?"));
fname1: str = str(input("whats your first name?"));
lname1: str = str(input("last name please?"));
height1: float = float(input("whats your height?"));
yob1: str = str(input("what year where you born?"));

id2: str = str(input("whats your id number?"));
fname2: str = str(input("whats your first name?"));
lname2: str = str(input("last name please?"));
height2: float = float(input("whats your height?"));
yob2: str = str(input("what year where you born?"));


print(f"#ID: {id1:<5} NAME: {fname1[:10]:<10} {lname1[:10]:<10} Height: {height1: .2f} Year of birth: {yob1:<15}");

print(f"#ID: {id2:<5} NAME: {fname2[:10]:<10} {lname2[:10]:<10} Height: {height2: .2f} Year of birth: {yob2:<15}");


# END


# whats your id number?1
# whats your first name?daniel
# last name please?mizrahi
# whats your height?1.75
# what year where you born?26
# whats your id number?2
# whats your first name?eyal
# last name please?nahmani
# whats your height?25
# what year where you born?1998
# #ID: 1     NAME: daniel     mizrahi    Height:  1.75 Year of birth: 1997
# #ID: 2     NAME: eyal       nahmani    Height:  1.75 Year of birth: 1998