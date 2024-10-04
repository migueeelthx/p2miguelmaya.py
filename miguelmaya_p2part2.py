def cuadrantes():
   #Solicitar al usuario que ingrese una coordenada
   x = float(input("Ingrese la coordenada X: "))
   y = float(input("Ingrese la coordenada Y: "))

#verificar que no escriban (0,0)
   if x == 0 or y == 0:
     print("Las coordenadas no pueden ser 0.")

#comparacion de cuadrantes con lo ingresado por el usuario
   else:

    if x > 0 and y > 0:
        print("El punto se encuentra en el cuadrante I.")
    elif x < 0 and y > 0:
        print("El punto se encuentra en el cuadrante II.")
    elif x < 0 and y < 0:
        print("El punto se encuentra en el cuadrante III.")
    elif x > 0 and y < 0:
        print("El punto se encuentra en el cuadrante IV.")

cuadrantes()