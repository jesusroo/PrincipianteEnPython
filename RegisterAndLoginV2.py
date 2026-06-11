print("Bienvenido a nuestra pagina")
print("complete el registro para continuar navegando")
usuario=str(input("crea un nombre de usuario:\n "))
Email=str(input("ingresa un correo electronico:\n "))


tiene_numero=False
tiene_mayus=False
tiene_especial=False
while True:
    password=(input("ingresa tu contraseña\n"))
    if len(password)>=8:

        for caracter in password:
            if caracter.isdigit():
                tiene_numero=True
            if caracter.isupper():
                tiene_mayus=True
            if not caracter.isalnum():
                tiene_especial=True
        if (tiene_numero) and (tiene_mayus) and (tiene_especial):
            print("contraseña valida")
            break
            
        else:
            print("contraseña invalida")
            print("la contraseñá debe tener al menos 8 digitos, una mayuscula, un numero, y un caracter especial")
                    
while True:                  
    PasswordConfirm=str(input("confirma tu contraseña\n"))
    if PasswordConfirm==password:
        print("¡registro exitoso!")
        break
    else:
        print("Las contraseñas no coinciden")


print("inicia sesion")
email=str(input("ingresa tu correo:\n "))
password=str(input("ingresa tu contraseña:\n "))



if (email==Email ) and (password==password):
    print("bienvenido ", usuario)
else:
    print("email o contraseña incorrecta")

         
