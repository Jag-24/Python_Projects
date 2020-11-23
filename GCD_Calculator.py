

first = input("Please enter first integer: ")
first = int(first)
second = input("Please enter second integer: ")
second = int(second)

f = first
s = second
if f > s:
    z = s
else:
    z = f

while True:
    if((f % z == 0) and (s % z == 0)):
        gcd = z
        break

    z = z - 1

gcd = str(gcd)
print("Greatest Common Divisor: " + gcd)

