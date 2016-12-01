a = input()
b = input()
c = input()
p = int(a)
x = int(b, p)
k = int(c)
n = ''

while x > 0:
    y = str(x % k)
    for k in range (10, 37):
        if y == str(k):
            y = chr(55+int(y))

    n = y + n
    x = int(x / k)

print(n)
