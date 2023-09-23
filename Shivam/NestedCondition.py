num = int(input("Enter a number : "));

if(num <= 10):
    print("Yes.. It is smaller or equal to 10");

    if(num <= 5):
        print("Yes.. It is smaller than or equal to 5");

        if(num <= 3):
            print("Yes.. It is smaller than or equal to 3");
        
            if(num <= 1):
                print("Yes.. It is smaller than or equal to 1");

            else:
                print("Number is greater than 1");
        
        else:
            print("Number is greater than 3");
    
    else:
        print("Number is greater than 5");

else:
    print("Invalid Input");