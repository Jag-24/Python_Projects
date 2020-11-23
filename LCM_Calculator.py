

first = input("Please enter first integer: ")
first = int(first)
second = input("Please enter second integer: ")
second = int(second)

f = first
s = second
if f > s:
    z = f
else:
    z = s

while True:
    if((z % f == 0) and (z % s == 0)):
        lcm = z
        break
    z = z + 1

lcm = str(lcm)
print("Lowest Common Multiple: " + lcm)