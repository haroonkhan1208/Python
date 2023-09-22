available = int(input("Enter the avialable amount : "));
withdraw = int(input("Enter the withdraw amount : "));

if(available >= withdraw):
    print("your transtion is succcessful and the remaining balance : ", available - withdraw);

else:
    print("Insufficent amount. Available amount : ", available);

