import random;

x = int(input("Enter the number : "));
y = random.randint(0,5);

if(x == y):
    print("number is match");
else:
    print("number is not match and the correct number is : ", y);


