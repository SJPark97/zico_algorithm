a = input()
a = a.upper()
b = dict()
for c in a:
    if c in b:
        b[c] += 1
    else:
        b[c] = 1
d = ''
e = 0
for i in b:
    if b[i] > e:
        d = i
        e = b[i]
    elif b[i] == e:
        d = '?'
print(d)