def longitud_palabra():
  palabra = input("Ingresa una palabra: ")

#Sacar la longitud de la palabra
  longitud = len(palabra)

#verificar que la longitud de la palabra tiene entre 4 y 8 letras
  if 4 <= longitud <= 8:
    print("La palabra es correcta.")
  elif longitud < 4:
    print(f"Hacen falta letras. Solo tiene {longitud} letras.")
  else:
    print(f"Sobran letras. Tiene {longitud} letras.")

    longitud_palabra()

    