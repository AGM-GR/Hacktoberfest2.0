def calculo_fuerza(kilos):
    F = 0
    F2= 0
    R = 10
    d = 70
    r = 30

    print("Cantidad introducida en kilos: " + str(kilos))

    F = (R * r) / d
    F2 = (R * 2 * r) / d 

    print("La fuerza es " + str(F) + "\n")
    print("La fuerza necesaria para mover un objeto que pesa el doble es " + str(F2) + "\n")
