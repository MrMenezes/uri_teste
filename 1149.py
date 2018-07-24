lista = input().split(' ')
print(
    sum(map(sum, zip(list(range(int(lista[-1]))), [int(lista[0])] * int(lista[-1])))))
