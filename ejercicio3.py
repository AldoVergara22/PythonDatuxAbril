first=input("Ingrese el primer numero:  ")
second=input("Ingrese elsegundo numero:  ")
third= input("Ingrese el tercer numero:  ")
a=int(first)
b= int(second)
c=int(third)

Suma= a+b+c
resta=a-b-c
multi= a*b*c
division= a/b/c
divInt= a//b/c
S= str(Suma)
R= str(resta)
M= str(multi)
div= str(division)
divI= str(divInt)

print("La suma es:"+ S)
print("La resta es:"+ R)
print("La multiplicación es:"+ M)
print("La divsión es:"+div)
print("La divsión entera es:"+divI)