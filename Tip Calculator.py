bill=int(input("Enter your bill \nRs"))
tip=int(input("Enter your tip 12/15/18 \n"))
num=int(input("How many people took part in dinner \n"))
topay= (bill*tip/100)/num
print("Each person has to pay ",topay,"Rs")
