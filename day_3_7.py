#Rollarcostar ride Bill


height=int(input("What`s your height?(cm)  "))

if height>=120:
      print("You can ride the rollarcostar")
      bill=0
      age=int(input("What`s your age ?  "))
      if age<12:
        bill=5
        print("Pay 5 dollar")
      elif age<= 18:
        bill=7
        print("pay 7 dollar")
      elif age >=45 and 55>=age:
          print("Free Ride")  
      else:
        bill=12
        print("Pay 12 dollar")
        
picture=input("Wanna take a picture ? Y or N \n")
if picture == "Y":
   bill +=3
   print(f"your bill is ${bill}")
               
else:
     print("You can`t ride the rollarcostar")