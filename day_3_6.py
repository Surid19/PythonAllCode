print("Welcome to Python Pizza ")
bill=0
size=input("Which size do you want ? S , M, L")
if size=="S":
     bill=500
     print("Small pizza is 500 taka")
elif size=="M":
    bill=700
    print("Small pizza is 700 taka")
elif size=="L":
    bill=1000
    print("Small pizza is 1000 taka") 
    
    
    peparonni=input("Want peparonni ? Y or No")
    if peparonni=="Y":
     print("Select pizza")
     
    add_peparonni=input("Peparonni for which pizza ? S or M/L ")
if add_peparonni=="S":
    bill +=2
    print("Adding $2")
elif add_peparonni=="M/L":
    bill +=5
    print("Adding $5")
add_extra_cheese=input("Add extra cheese Y/N")
if add_extra_cheese == "Y":
   bill += 1
print(f"Your bill is {bill}")  