import random;

user = int(input("Enter the number : "));
computer = random.randint(1,6);

if(user == computer):
    print("User Won The Ganme");
else:
    print("User Lost The Game And The Correct Number Is : ", computer);


