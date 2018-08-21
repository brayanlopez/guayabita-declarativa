import random
import sys
sys.setrecursionlimit(10000)
def calcularApuesta(cuenta1, cuenta2):
    if cuenta1>cuenta2:
        return random.randint(0, cuenta2)
    else:
        return random.randint(0, cuenta1)
def iniciar(cuenta1, cuenta2, dado, apuesta, codigo, previa, jugador):
    if cuenta1 == 0 or cuenta2 == 0:
        #si se cumple esto es por que alguna de las dos cuentas quedaron en 0 por lo que se debe terminar el juego
        if cuenta1 == 0:
            print("el jugador 2 ha vencido")
            print(cuenta1, cuenta2)
        else:
            print("el jugador 1 ha vencido")
            print(cuenta1, cuenta2)
        pass
    else:
        if codigo == 0:
            #el codigo 0 sirve para jugar el primer turno y establecer la apuesta
            print("estableciendo apuesta")
            if jugador == 1:
                print("turno jugador 1")
                print(cuenta1, cuenta2)
                input()
                iniciar(cuenta1-calcularApuesta(cuenta1, cuenta2), cuenta2-calcularApuesta(cuenta1, cuenta2), random.randint(1,6), 2*calcularApuesta(cuenta1, cuenta2), 1, 0,1)
            else:
                print("turno jugador 2")
                print(cuenta1, cuenta2)
                input()
                iniciar(cuenta1-calcularApuesta(cuenta1, cuenta2), cuenta2-calcularApuesta(cuenta1, cuenta2), random.randint(1,6), 2*calcularApuesta(cuenta1, cuenta2), 1, 0,2)
        elif codigo == 1:
            #el codigo 1 es para decidir que se hace despues de la primera tirada, si pierde con 1, 6; si gana con 4 o si apuesta o no con cualquier otro
            print("lanzando el dado la primera vez")
            print(dado)
            if dado == 1 or dado == 6:
                if jugador == 1:
                    print("pierde jugador 1")
                    print(cuenta1, cuenta2)
                    input()
                    iniciar(cuenta1, cuenta2+apuesta,random.randint(1,6),0,0,0,2)
                       
                else :
                    print("pierde jugador 1")
                    print(cuenta1, cuenta2)
                    input()
                    iniciar(cuenta1+apuesta, cuenta2,random.randint(1,6),0,0,0,1)
                    
            elif dado == 4 :
                if jugador == 1:
                    print("gana jugador 1")
                    print(cuenta1, cuenta2)
                    input()
                    iniciar(cuenta1+apuesta, cuenta2, random.randint(1,6), 0, 0, 0,2)
                    
                else:
                    print("pierde jugador 1")
                    print(cuenta1, cuenta2)
                    input()
                    iniciar(cuenta1, cuenta2+apuesta, random.randint(1,6), 0, 0, 0,1)       
                    
            else:
                if(random.randint(0,1)==0):
                    if jugador == 1:
                        print("el jugador 1 no apuesta nada")
                        print(cuenta1, cuenta2)
                        input()
                        iniciar(cuenta1, cuenta2,random.randint(1,6),apuesta,2,dado,1)
                        
                    else:
                        print("el jugador 2 no apuesta nada")
                        print(cuenta1, cuenta2)
                        input()
                        iniciar(cuenta1, cuenta2,random.randint(1,6),apuesta,2,dado,2)
                        
                else:
                    if jugador == 1:
                        print("el jugador 1 aumenta")
                        print(cuenta1, cuenta2)
                        input()
                        iniciar(cuenta1-calcularApuesta(cuenta1, cuenta2), cuenta2 - calcularApuesta(cuenta1, cuenta2), random.randint(1,6), apuesta + 2*calcularApuesta(cuenta1, cuenta2), 2,dado,1)
                        
                    else:
                        print("el jugador 2 aumenta")
                        print(cuenta1, cuenta2)
                        input()
                        iniciar(cuenta1-calcularApuesta(cuenta1, cuenta2), cuenta2 - calcularApuesta(cuenta1, cuenta2), random.randint(1,6), apuesta + 2*calcularApuesta(cuenta1, cuenta2), 2,dado,2)
                        
        elif codigo == 2:
            #lanzamiento final en el que se compara con el lanzamiento previo para saber si gana o si pierde
            print("lanzando el dado la segunda vez")
            if dado > previa:
                if jugador == 1:
                    print("gana jugador 1")
                    print(cuenta1, cuenta2)
                    input()
                    iniciar(cuenta1+apuesta, cuenta2, random.randint(1,6), 0,0,0,2)
                    
                else:
                    print("gana jugador 2")
                    print(cuenta1, cuenta2)
                    input()
                    iniciar(cuenta1, cuenta2+apuesta, random.randint(1,6), 0,0,0,1)
                    
            else:
                if jugador == 1:
                    print("pierde jugador 1")
                    print(cuenta1, cuenta2)
                    input()
                    iniciar(cuenta1, cuenta2+apuesta, random.randint(1,6),0,0,0,2)
                    
                else:
                    print("pierde jugador 2")
                    print(cuenta1, cuenta2)
                    input()
                    iniciar(cuenta1+apuesta, cuenta2, random.randint(1,6),0,0,0,1)
                    
#el juego inicialmente le asigna un monto aleatorio entre 1 y 5000 unidades a cada jugador con el cual pueden apostar
iniciar(random.randint(1,5000),random.randint(1,5000), 0,0,0,0,random.randint(1,2))
