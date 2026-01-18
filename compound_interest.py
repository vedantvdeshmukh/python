"""
amount = p(1 + r/100)**t
compound interest = amount - p
"""
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest :")) 
time = float(input("Enter the time periods in years: "))
amount = principal * pow(1 + rate / 100, time)
amount = round(amount, 2)
print("The total amount after {time} years is :{amount}".format(time=time, amount=amount))
compound_interest = amount - principal 
print("The Compound Interest is : ", compound_interest) 