rows = int(input("Enter the numbers of rows :"))
number = 1

print("floyd's triangle")

for i in range(1 , rows + 1):
   
    for j in range(i , 1+i):
        print(number , end=' ')
        number= number + 1
    print()
