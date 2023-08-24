                                   #BMI 2.0


height=input("What`s your height(m): ")
weight=input("What`s your weight(kg): ")
element_1=float(height)
element_2=float(weight)
BMI=(element_2/(element_1 ** 2))
print("Your BMI is : ")
print(float(BMI))
if BMI<= 18.5:
      print("Under weight")
elif BMI <= 25:
    print("normal weight")
elif BMI <= 30:
    print("OverWeight")
elif BMI <=35:
    print ("Obese") 
          
else:
      print("Clinically Obese!") 