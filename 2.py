n = 0
s = input().split()
a = int(s[0])
b = int(s[1])
while a != 0 and b != 0:
    if a%2 == 0 and b%7 == 0:
        if len(str(a))>=3 or len(str(b))>=3:
            n+=1
    s = input().split()
    a = int(s[0])
    b = int(s[1])

print(n)