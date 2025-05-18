num = input("enter a number :")
count = 0
for ch in num:
     if ch.isdigit():
          count += 1
print("total digits:" , count)