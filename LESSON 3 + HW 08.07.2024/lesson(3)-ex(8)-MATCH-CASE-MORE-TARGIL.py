# LESSON 3 EX 8

# MATCH CASE
# write a match case program for cards
# 2..10, 11=J, 12=Q, 13=K, 14=A, 15=JOKER
# START

card_id: int = int(input("Enter a card number (2-14):"))

match card_id:
    case 1:
        print("mono mono");
    case 2:
        print("due pistoli");
    case 3:
        print("three hearts bro");
    case 4:
        print("its just four");
    case 5:
        print("yup five");
    case 6:
        print("six broooo");
    case 7:
        print("its just a 7");
    case 8:
        print("eight balls");
    case 9:
        print("i dont like 9 spades");
    case 10:
        print("my type a tenner");
    case 11:
        print("prince j");
    case 12:
        print("queen laquisha");
    case 13:
        print("king avigdor");
    case 14:
        print("ass pras shel ha pizuzia");
    case 15:
        print("joker cries");
    case _:
        print("what bro?")

# END


# Enter a card number (2-14):13
# king avigdor


# Enter a card number (2-14):18
# what bro?




# START

# MORE OPTIONS IN MATCH CASE


card_id: int = int(input("Enter a card number (2-14):"))

match card_id:
    case 2 | 3 | 4 | 5 | 6 | 7 |8 | 9 | 10:
        print(card_id)
    case 11:
        print("prince j");
    case 12:
        print("queen laquisha");
    case 13:
        print("king avigdor");
    case 14:
        print("ass pras shel ha pizuzia");
    case 15:
        print("joker cries");
    case _:
        print("what bro?")



# END



# Enter a card number (2-14):5
# yup five
# Enter a card number (2-14):5
# 5