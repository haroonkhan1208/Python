import random;

user = input("Enter your choice : ");

comp = random.randint(0, 10);

computer = "";

if(comp <= 3):
    computer = "stone";

elif(comp > 3 and comp <= 6):
    computer = "paper";

else:
    computer = "seccissor";

if(computer == "paper" and user == "seccissor"):
    print("User won the game. User took ", user, " and computer took ", computer);

elif(computer == "seccissor" and user == "paper"):
    print("Computer won the game . User took ", user, " and computer took ", computer );

elif(computer == "stone" and user == "paper"):
    print("User won the game. User took ", user, " and computer took ", computer );

elif(computer == "paper" and user == "stone"):
    print("Computer won the game. User took ", user, " and Computer took ", computer);
 
elif(computer == "stone" and user == "seccissor"):
    print("Computer won the game. User took ", user, " and Computer took ", computer);

elif(computer == "seccissor" and user == "stone"):
    print("User won the game. User took ", user, " and Computer took ", computer);

elif(computer == user):
    print("Match draw. User took ", user, " and computer took ", computer);

else:
    print("Invalid input. User took ", user, " and computer took ", computer);