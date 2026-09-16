#fibonacci
a = 0
b = 1
n = int(input("ingrese un numero: "))
for i in range(0, n+1):
    print(a)
    c = a + b
    a = b
    b = c