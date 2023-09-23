fNum = int(input("Enter the first number  : " ));
sign = (input("Enter the sign   :  " ))[0];
sNum = int(input("Enter the second number  :  " ));

if(sign == '+'):
    print(fNum , " ", sign , " " , sNum , " = " , fNum + sNum);

elif(sign == '-'):
    print(fNum , " " , sign , " " , sNum , " = " , fNum - sNum);

elif(sign == '*'):
    print(fNum , " " , sign , " " , sNum , " = " , fNum * sNum);

elif(sign == '/'):
    print(fNum , " " , sign , " " , sNum , " = " , fNum / sNum);

else:
    print("Invaild input");