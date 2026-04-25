def calcular_sal_hora(horas_t):
    total = horas_t * 25
    return total

def calcular_sal_full ():
    pass


while True:
    
    nombre = input("Ingrese su nombre: ")
    print ("Usted trabaja por Hora o Tiempo Completo? ")
    opcion = int (input("Ingrese 1: Salario por Hora o Ingrese 2: para Tiempo Completo: "))
    match opcion:
        case 1:
            horas_tra = int (input("Ingrese cuantas horas trabajo: "))
            resultado = calcular_sal_hora (horas_tra)
            print (f"{nombre} su salario fue de {resultado}")
        case _: pass
    con = input("Desea evaluar a otro empleado?  Y/N : ").lower()
    if con == "y":
        continue
    else:
        print ("Saliendo....")
        break

     
# mongo pass Rbu50wht4R0NeXIC

# 2 mongodb+srv://travelAdmin:<db_password>@cluster0.pgnu97m.mongodb.net/?appName=Cluster0