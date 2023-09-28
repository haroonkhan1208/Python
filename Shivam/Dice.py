fNum  = int(input("Enter the number  :  " ));
sNum  = int(input("Enter the number  ;  " ));

if( fNum <= 6 and sNum <= 6 ):
    add = fNum + sNum ;
    if(add >= 10):
        print("YES");

    else:
        print("No");
    
else:
    print("Invalid Input");