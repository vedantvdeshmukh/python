a = float(input("Enter the length of side a of the triangle:"))
b = float(input("Enter the length of side b of the triangle:"))
c = float(input("Enter the length of side c of the triangle:"))

s = (a + b + c) / 2 
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("The area of the triangle is:", round(area, 2))
print("The Perimeter of the triangle is:", a + b + c)