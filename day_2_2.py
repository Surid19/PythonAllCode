height=input("What`s your height(m): ")
weight=input("What`s your weight(kg): ")
element_1=float(height)
element_2=float(weight)
BMI=(element_2/(element_1 ** element_1))
print("Your BMI is : ")
print(int(BMI))
if BMI<= 30:
      print("You are safe")  
else:
      print("Reduce your weight !")      


