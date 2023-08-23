lr = int(input("Enter the lower range:\n"))
hr = int(input("Enter the upper range:\n"))
d = int(input("Enter the number to see the possible divisible numbers\n"))

for i in range(lr, hr + 1):
    if i % d == 0:
        print(i)

print("These numbers are all divisible by ", d)