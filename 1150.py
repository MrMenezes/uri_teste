a = int(input())
b = a
while b <= a:
    b = int(input())
i = 2
c = sum(list(range(a, a + i)))
while c < b:
    i = i + 1
    c = sum(list(range(a, a + i)))
print(i)
