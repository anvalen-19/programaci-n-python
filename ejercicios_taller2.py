
#EJERCICIO 1***********************
import math

def volumen_solido(r1, r2, h):
    # Volumen de la media esfera
    volumen_media_esfera = (2/3) * math.pi * (r1 ** 3)
    # Volumen del cono
    volumen_cono = (1/3) * math.pi * (r2 ** 2) * h
    # Volumen total
    volumen_total = volumen_media_esfera + volumen_cono
    return volumen_total
# Valores de pprueba 
r1 = 3
r2 = 4
h = 9/2  # División normal

# Llamamos la función
volumen = volumen_solido(r1, r2, h)
print(f"El volumen del sólido es: {volumen} unidades cúbicas")
h_entera = 9//2  # División entera

volumen_con_h_entero = volumen_solido(r1, r2, h_entera)
print(f"El volumen del sólido usando división entera es: {volumen_con_h_entero:} unidades cúbicas")

#EJERCICIO 2***********************
import math

def area_lateral_vagon(a, b, r):
    # Área lateral del rectángulo
    area_rectangulo = 2 * a * b
    # Área lateral de las ruedas
    area_ruedas = 4 * math.pi * r
    # Área lateral total
    area_total = area_rectangulo + area_ruedas
    return area_total
# Ejemplo (prueba)
a = 4
b = 10
r = 10

area = area_lateral_vagon(a, b, r)
print(f"El área lateral del vagón es: {area: } unidades cuadradas")

#EJERCICIO #3*******************
import math

def suma(a, b):
    return a + b
def area_rectangulo(a, b):
    return 2 * a * b
def area_circulo(r):
    return 2 * math.pi * r
def area_carro2D(a1, b1, a2, b2, r1, r2):
    area_RECTANGULO_inferior = area_rectangulo(a1, b1)
    area_RECTANGULO_superior = area_rectangulo(a2, b2)
    area_rueda1 = area_circulo(r1)
    area_rueda2 = area_circulo(r2)
    
    # SE SUMA todo
    area_total = suma(
        suma(area_RECTANGULO_inferior, area_RECTANGULO_superior),
        suma(area_rueda1, area_rueda2)
    )
    
    return area_total
# prueba valores
a1 = 2
b1 = 6
a2 = 4
b2 = 8
r1 = 1
r2 = 0.4

area = area_carro2D (a1, b1, a2, b2, r1, r2)
print(f"El área lateral del carro es: {area:} unidades cuadradas")


#PROBLEMAS****

# Problema 1: Cantidad de carne de aves en kilos
def calcular_carne_aves(N, M, K):
    carne_total = (N * 6) + (M * 7) + (K * 1)
    return carne_total

#datos de experimentación*******
N = 3  # gallinas
M = 2  # gallos
K = 5  # pollitos 

total_carne = calcular_carne_aves(N, M, K)
print(f"La cantidad total de carne es: {total_carne} kilos")

#problema 2
def calcular_vueltas(P, M, H, B):

    Gastos_totales = (P * 300) + (M * 3300) + (H * 350)
    cambio = B - Gastos_totales
    return cambio

#práctica
P = 5  # panes
M = 2  # bolsas de leche
H = 12 # huevos
B = 20000  # dinero entregado (pago)

resultado = calcular_vueltas(P, M, H, B)

if resultado >= 0:
    print(f"sobran {resultado} pesos de cambio.")
else:
    print(f"faltan {-resultado} pesos para completar la compra.")

#problema 3
def calcular_pago_final():

    P = float(input("Ingrese el monto prestado (en pesos): "))
    tasa_interes = 0.03  # 3% mensual
    meses = 2

    monto_final = P * (1 + tasa_interes) ** meses

    print(f"El monto total a pagar después de 2 meses es: {monto_final:} pesos")

# Llamar la función
calcular_pago_final()

