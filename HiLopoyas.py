import random
x = random.randint(1,10)
while True:
    a = input("introduce un número ")
    b = int(a)
    if x == b:
        print("Ganador!!1!")
        break
    elif b < x:
        print("El número secreto es mayor, prueba otra vez.")
    elif b > x:
        print("El número secreto es menor, prueba otra vez.")
    
