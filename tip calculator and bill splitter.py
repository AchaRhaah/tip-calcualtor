# a program to calculate the tip and bill of each person
bill=float(input("what was the total bill:"))
howManyPeople=int(input("how many people are to split the bill:"))
tipPercentage=int(input("what percentage of the bill do you want to give as tip:"))
BillWithTip=((tipPercentage/100)*bill)+bill
billPerPerson=BillWithTip/howManyPeople
print(BillWithTip)
totalRoundedBill=round(BillWithTip,2)
print(totalRoundedBill)
print(f"bill paid per person is{billPerPerson}")
