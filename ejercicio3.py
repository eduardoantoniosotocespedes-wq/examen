#Tabla de multiplicar
print("===Tabla de ultiplicar===")
while True:
    x = int(input("Porfavor ingrese un numero entre el 1 y el 10: "))
    if x <11 and x >0:
        for i in range (1, 13):
            print(f"{i} x {x} = {i*x}")
        break
    else:
        print("Error intente denuevo...")