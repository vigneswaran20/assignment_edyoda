
n = int(input("Input the number of terms:- "))
x =  0
y = 1
count = 0
print("Fibonacci sequence:")
while count < n:
    print(x)
    z = x + y
    x = y
    y = z
    count += 1
