import random 

numero_secreto = random.randint(1, 50)
intentos=1
num=int(input("intenta adivinar el numero secreto(1-50)"))
while True:
   
    if num>numero_secreto:
        print("numero secreto es menor que ",num)
        num=int(input("ingresa otro numero: "))
        
        intentos=intentos+1
    elif num<numero_secreto:
        
        print("numero secreto es mayor que ",num)
        num=int(input("ingresa otro numero: "))
        intentos=intentos+1    

    elif num==numero_secreto:
        print("felicidades, adivinaste el numero secreto en tan solo ",intentos," intentos")    
        break
