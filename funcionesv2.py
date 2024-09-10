print("Mas sobre funciones")
# Aqui se escriben las funciones
def suma_ab(a,b):
    s=a+b
    return s
def resta_ab(a,b):
    r=a-b
    return r
def multip_ab(a,b):
    m=a*b
    return m
def div_ab(a,b):
    d=a/b
    return d
    
#Llamadas a funciones
print("----Calculando suma----")
n1=int(input("Ingresa el primer numero: "))
n2=int(input("Ingresa el segundo numero: "))
suma=suma_ab(n1,n2)
print(f"el resultado de {n1} + {n2} es: {suma}")

print("----Calculando resta----")
n3=int(input("Ingresa el primer numero: "))
n4=int(input("Ingresa el segundo numero: "))
rest=resta_ab(n1,n2)
print(f"el resultado de {n3} - {n4} es: {rest}")

print("----Calculando Multiplicacion----")
n5=int(input("Ingresa el primer numero: "))
n6=int(input("Ingresa el segundo numero: "))
mult=multip_ab(n5,n6)
print(f"el resultado de {n1} * {n2} es: {mult}")

print("----Calculando Division----")
n7=float(input("Ingresa el primer numero: "))
n8=float(input("Ingresa el segundo numero: "))
div=div_ab(n7,n8)
print(f"el resultado de {n7} * {n8} es: {div}")