a = -1
l = 0
m = 0
s = input().split()

t = s.index('0')
s = s[0:t]

for i in range(len(s)):
    k = int(s[i])

    if a == k:
        l += 1
    else:
        a = k
        m = max(m, l)
        l = 1
m = max(m, l)
print(m)