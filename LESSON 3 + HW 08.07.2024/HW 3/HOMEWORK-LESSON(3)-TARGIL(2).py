# HOMEWORK LESSON 3 TARGIL 2

# get an input from user for a graded test num (int)
# a.for 0 - 40 "try harder next time"
# b.for 41 - 60 "you're getting there, need some more work"
# c.for 61 - 80 "pretty good"
# d.for 81 - 95 "awesome!!!"
# e.for 96 - 100 - 40 "excellent!!!! YOU'RE A STAR!!!"
# f.for a number thats under 0 or over 100 print "illegal grade"


# START

grade: int = int(input("Please enter you're grade:"));

if 0 <= grade <= 40:
    print("try harder next time...");
elif 41 <= grade <= 60:
    print("you're getting there, need some more work");
elif 61 <= grade <= 80:
    print("pretty good");
elif 81 <= grade <= 95:
    print("awesome!!!");
elif 96 <= grade <= 100:
    print("excellent!!!! YOU'RE A STAR!!!");
else:
    print("grade illegal");

# END

# Please enter you're grade:-1
# grade illegal

# Please enter you're grade:86
# awesome!!!