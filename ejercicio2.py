r=int(input("Ingrese el radio:  "))
a= int(input("Ingrese el 1er lado del triangulo:"))
b= int(input("Ingrese el 2do lado del triangulo:"))
c= int(input("Ingrese el 3er lado del triangulo:"))

# Formulas
Cu= r*r
Ci= 3.1415*r*r
p= (a+b+c)/2
Tri= p*(p-a)*(p-b)*(p-c)
Tri2=Tri**0.5
ACi=str(Ci)
ACu=str(Cu)
ATri=str(Tri)
ATri2=str(Tri2)

print("Area del circulo es:  "+ ACi)
print("Area del cuadrado es:  "+ ACu)
print("Area del triangulo es:  "+ ATri2)
