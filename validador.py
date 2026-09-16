def verificar():
    while True:
        print("Validador de usuario")
        user = str(input("Ingrese su usuario: "))
        clave = str(input("Ingrese su clave: "))
        if user == "estudiante" and clave == "pem2026":
            print("Credenciales correctas..")
            break 
        else:
            print("Error intente denuevo.....")