
descuento=0
plan= float(input("seleciona un plan: 1,2 o 3 "))


if plan==1:
  precio=200 
elif plan==2:
  precio=300
elif plan==3:
  precio=400    
    
rango= str(input("eres premium: si o no "))
if rango=="si":
    descuento=0.10
else:
    descuento=0.05

descuento=(precio*descuento)

print("total a pagar: ",precio-descuento,"$")
    
    
