decimal = int(input("enter a decimal number:"))

binary = ""
temp = decimal

if temp == 0:
   binary = "0"

else:
   while temp > 0:
     remainder = temp % 2
     binary = str(remainder) + binary
     temp //= 2

print("Binary number:" , binary)
