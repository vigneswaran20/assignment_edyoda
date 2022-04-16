#Write a Python program to count the number of even and odd numbers from a series of numbers.
l = (2,3,5,9,11,12,14)

x = 0
y = 0

for i in l: 
    if i % 2 == 0: 
        x+=1
    else: 
        y+=1          

print("Even : ", x) 
print("Odd : ", y)
