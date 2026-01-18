"""
Simple Interest Calculator = (p *r *t )/100
p = principal amount
r = rate of interest
t = time period in years
"""
p = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest :"))
t = float(input("Enter the time period in years: "))
simple_interest = (p * rate* t )/100
print("The Simple Interest is : ", simple_interest)
