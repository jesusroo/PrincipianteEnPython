print("Bienvenido a nuestra pagina")
print("complete el registro para continuar navegando")
usuario=str(input("crea un nombre de usuario:\n "))
Email=str(input("ingresa un correo electronico:\n "))
Password=str(input("crea una contraseña:\n ")) 
print("¡registro exitoso!") 

print("inicia sesion")
email=str(input("ingresa tu correo:\n "))
password=str(input("ingresa tu contraseña:\n "))



if (email==Email ) and (password==Password):
    print("bienvenido ", usuario)
else:
    print("email o contraseña incorrecta")
