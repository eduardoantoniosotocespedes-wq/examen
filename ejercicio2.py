print("""========TARIFADOR POR HORA==========
Seleccione su veiculo:
1.- Moto
2.- Auto
3.- Camion""")
veiculo = int(input("Responda aqui: "))
horas = int(input("ingrese las horas que se quedo: "))
if horas > 0:
    match veiculo:
        case 1:
            if horas > 4:
                pagar = horas * 5
                desceunto = pagar * 0.15
                total = pagar - desceunto
                print(f" descuento de 15% su monto a pagar es: {total}")
            else:
                pagar = horas * 5
                print(f"Su monto a pagar es: {pagar}")
        case 2:
            if horas > 4:
                pagar = horas * 10
                desceunto = pagar * 0.15
                total = pagar - desceunto
                print(f" descuento de 15% su monto a pagar es: {total}")
            else:
                pagar = horas * 10
                print(f"Su monto a pagar es: {pagar}")
        case 3:
            if horas > 4:
                pagar = horas * 20
                desceunto = pagar * 0.15
                total = pagar - desceunto
                print(f" descuento de 15% su monto a pagar es: {total}")
            else:
                pagar = horas * 20
                print(f"Su monto a pagar es: {pagar}")
        case _:
            print("opcion invalida")
else:
    print("horas invalidas")