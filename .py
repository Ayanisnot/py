def calc_circumference(radius):
    pi = 3.1416
    circumference = 2 * pi * radius
    return circumference


r = float(input("enter the radius of the circle :"))
c = calc_circumference(r)
print("The answer is" , c)
