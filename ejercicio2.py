print("\t\tConversor\n")

opcion = 0
while opcion != 4:
    print("1.Covertir de grado a celsius a Fahrenheit")
    print("2.Covertir de Dolar a pesos")
    print("3.Covertir de metros a pies")
    print("4.Salir\n")
    opcion = int(input("Elegir opcion:"))

    if opcion == 1:
        cl = int(input("Introduzca cantidad de celsius: "))
        fr = (cl * 1.8) + 32
        print("la cantidad de Fahrenheit es: "+ str(fr))

    elif opcion ==2:
        dl = int(input("Digite la cantidad de Dolar: "))
        ps = (dl * 58.45)
        print("Su cantidad de pesos es: "+ str(ps))

    elif opcion ==3:
        mt = int(input("Cuantos metros desea convertir: "))
        pi = (mt * 3.2808)
        print("Su cantidad de pies es: "+ str(pi))



else : 
    print("\tADIOS!!")
    SystemExit