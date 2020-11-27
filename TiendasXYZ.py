#Ingresaremos las variables para nuestro ejercicios
Valor=int(input("Ingrese el valor a pagar: "))
Descuento1 = 0.25
Descuento2 = 0.20
Descuento3 = 0.15

if Valor<=5000:
    print("El valor pagado es")
    print(Valor)
    print("El descuento a aplicar es: ")
    print(Descuento1)

    ValorDescuento = Valor * Descuento1
    ValorTotal = Valor - ValorDescuento

    print("El Valor por pagar es: ")
    print(ValorTotal)
else:
    if Valor