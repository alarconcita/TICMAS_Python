#TRABAJO_FINAL
#Parte_1
'''
El empleado llamado Juan cobró 
300 dólares por mes desde enero a junio (6 meses --> 6*300), 
500 dólares de julio a octubre (4 meses --> 4*500), 
y 700 dólares por mes en noviembre y en diciembre (2 meses --> 2*700). 

En base al escenario propuesto, se le solicita a los estudiantes 
que creen un pequeño programa que calcule el sueldo promedio del empleado Juan. 
Además, se debe indicar sí Juan se encuentra cobrando 
un sueldo bajo, normal o mejor de lo normal, 
considerando las siguientes pautas:
a. Sueldo bajo: por debajo de 300 dólares.
b. Sueldo normal:  entre 300 a 900.
c. Sueldo mejor de lo normal: más de 900 dólares.

Tip: se debe utilizar estructuras condicionales.
'''
sueldo1 = (6*300) #enero a junio
sueldo2 = (4*500) #julio a octubre
sueldo3 = (2*700) #noviembre y diciembre
sueldo = sueldo1 + sueldo2 + sueldo3
print("El sueldo anual de Juan es " + str(sueldo))
prom = sueldo/12
print ("Y el promedio mensual es " + str(prom))

if prom < 300:
    print("El sueldo de Juan es bajo")
elif prom>=300 and prom<900:
    print("El sueldo de Juan es normal")
else:
    print("El sueldo de Juan es mejor de lo normal")
