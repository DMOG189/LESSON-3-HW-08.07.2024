# HOMEWORK LESSON 3 TARGIL 3

# for an audio system
# input from user a db level (int)
# use "match case"


# START

volume = int(input("Enter volume level:"));

match volume:
    case 0:
        print("MUTE");
    case 1 | 2:
        print("very quiet");
    case 3:
        print("quiet");
    case 4:
        print("moderately quiet");
    case 5:
        print("medium");
    case 6:
        print("moderately loud");
    case 7:
        print("loud")
    case 8:
        print("very loud")
    case 9 | 10:
        print("extremely loud");
    case _:
        print("Invalid volume level")

# END


# Enter volume level:10
# extremely loud