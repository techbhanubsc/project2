print("Welcome to the tip calculator!")
bill=float(input("What was the total bill?"))
tip=int(input("How much tip would you like to give?(in percentage)"))
no_of_people=int(input("How many people to split the bill?"))
print("Each person should pay : " ,str((bill+(bill*(tip/100)))/no_of_people)+"$")


#From this we got to know about type conversion,mathematical operations,input values