# LESSON 3 TARGIL 7 {BONUS}


# CHALLENGE # PART A

# dannys mother got pizza for everyone
# every friend gets an equal amount of full slices
# danny had 4 friends
# for 3 slices every friend got 0 and there left 3
# for 4 slices every friend got 1 and there left 0
# for 6 slices every friend got 1 and there left 2
# for 8 slices every friend got 2 and there left 0

# write a program that gets the input of
# a number of pizza slices
# how manny each friend got
# and how much left

# START

pizza: int = int(input("yo what up? delivery of how many slices you said???"));

if pizza % 4 == 0:
    print(f"each boy received {pizza // 4} slices of pizza!");
else:
    print(f"each boy received {pizza // 4} slices of pizza! , and {pizza % 4} more pizza in the fridge for later");







# END

# yo what up? delivery of how many slices you said???8
# each boy received 2 slices of pizza!

# CHALLENGE # PART B

# write a program that gets the input of
# how many friends danny got
# how manny slices delivered
# and how much each one got



# START


pizza: int = int(input("yo what up? delivery of how many slices you said???"));
friends: int = int(input("how manny will you be?"));
if pizza % friends == 0:
    print(f"each boy received {pizza // friends} slices of pizza!");
else:
    slices_leftovers: int = pizza % friends;
    print(f"each boy received {pizza // friends} slices of pizza! , and {slices_leftovers} more slices in the fridge for later");


# END

# yo what up? delivery of how many slices you said???20
# how manny will you be?6
# each boy received 3 slices of pizza! , and 2 more slices in the fridge for later