# LESSON 3 EX 7

# MATCH CASE
# when you have more cases on a single
# memory thread its better using match case

# EXAMPLE


# START


day: int = int(input("enter a day and get it in a string:"));

if day == 1:
    print("sunday");
elif day == 2:
    print("monday");
elif day == 3:
    print("tuesday");
elif day == 4:
    print("wednesday");
elif day == 5:
    print("thursday");
elif day == 6:
    print("friday");
elif day == 7:
    print("saturday");
elif day == "":
    print("invalid day");


# match case option
# case = else

day: int = int(input("enter a day and get it in a string:"));

match day:
    case 1:
        print("sunday");
    case 2:
        print("monday");
    case 3:
        print("tuesday");
    case 4:
        print("wednesday");
    case 5:
        print("thursday");
    case 6:
        print("friday");
    case 7:
        print("saturday");
    case _:
        print("invalid day");


# END

#enter a day and get it in a string:1
#sunday
#enter a day and get it in a string:1
#sunday


# MORE EXAMPLES FOR MATCH CASE USE


# match True:
#    case_ if age > 18 or balance < 100_00:
#      print("over 18")
#    case_ if age > 9:
#      print("over 9")
#    case_ if age > 2:
#      print("over 2")


# works like if and else



