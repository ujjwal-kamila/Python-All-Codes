l = [1, 3, 5, 4, 2, 6]
print(l)
l.append(7)
print(l)
l[1] = 32
print(l)
l.sort()
print(l)
l.sort(reverse=True)
print(l)
l.reverse()
print(l)
print(l.index(1))
print(l.count(2))

m = l
m[0]=0
print(l)
m = l.copy()
m[0]=90
print(l)
print(m)

l.insert(1, 78)
print(l)
n = [100, 200]
l.extend(n)
print(l)
k= l+m
print(k)