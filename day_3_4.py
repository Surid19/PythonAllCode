Year=int(input("Which year you want to check ?" ))

if Year%4==0 :
    if Year%100==0:
        if Year%400==0:
            print("A leap year")
        else:
            print("Not a leap year")
    else:
        print( "A leap year")  
else:
    print("Not a leap year")
    