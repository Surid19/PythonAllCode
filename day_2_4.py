print("Chillox Tip Calculator")
bill=input("What was the total bill ?")
bill_as_float=float(bill)
tip_percentage=input("Make sure tip percentage:")
tip_percentage_as_int=int(tip_percentage)  
tip_included_bill=bill_as_float+(tip_percentage_as_int/100)
persons=input("How many persons to pay Bill?  ")
persons_as_int=int(persons)
each_person_cost=int(tip_included_bill/persons_as_int)
print("Each person has to pay:  ")
print(each_person_cost)


