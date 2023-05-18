import random

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("Elige un número del 1 al 100: "))

    while (numero_elegido != numero_aleatorio):
        if numero_elegido < numero_aleatorio:
            print("\nBusca un número mas grande")
        else:
            print("\nBusca un número más pequeño")
            
        numero_elegido = int(input("\nElige un número del 1 al 100: "))
        
    print("Has adivinado el número, felicidades")
    
    
if __name__ == "__main__":
    run()
