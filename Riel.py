import numpy as np
import pandas as pd
from ListClases import *

car = Cargas()
riel = Riel()


############## VERIFICACIÓN RIELES ##############
riel.tipo = 'ASCE 75 (TR37)'
car.N = 891.74
riel.N_ruedas = 4.0
riel.phi = 0.90
riel.FM = 1.40
riel.L = 30
riel.Esf_t = 19.98

riel.Pa = car.N / riel.N_ruedas
riel.Pu = riel.Pa * riel.FM
riel.Wx = riel.Mod_Resistencia(riel.tipo)
riel.Pn = riel.phi * ((4 * riel.Esf_t * riel.Wx) / riel.L)
riel.Calidad = riel.Calidad_Acero(riel.Esf_t)
riel.Tension = riel.Tension_Rotura(riel.Esf_t)
riel.Limite = riel.Limite_Elastico(riel.Esf_t)

if (riel.Pn > riel.Pu):
    Chequeo  = 'Ok'
else:
    Chequeo = 'No cumple'


############## REPORTE EXCEL ##############
P0 = ' DETALLES '
P1 = ' σ: Esfuerzo de trabajo. '
P2 = ' Número de ruedas. '
P3 = ' Factor de mayoración. '
P4 = ' Pa: Fuerza aplicada. '
P5 = ' Pu: Fuerza última. '
P6 = '  '
P7 = ' Tipo riel. '
P8 = ' Wx: Módulo de resistencia del riel. '
P9 = ' L: separación entre platinas. '
P10 = ' ø. Factor de reducción de resistencia '
P11 = ' øPn: Resistencia del riel ø (4*σ*Wx) / L '
P12 = ' øPn > Pu '
P13 = '  '
P14 = ' RESUMEN '
P15 = ' Calidad del acero del riel. '
P16 = ' Tensión de rotura. '
P17 = ' Limite elástico. '

V0 = ' '
V1 = riel.Esf_t
V2 = riel.N_ruedas
V3 = riel.FM
V4 = round(riel.Pa, 2)
V5 = round(riel.Pu, 2)
V6 = '  '
V7 = riel.tipo
V8 = riel.Wx
V9 = riel.L
V10 = riel.phi
V11 = round(riel.Pn, 2)
V12 = Chequeo
V13 = '  '
V14 = '  '
V15 = riel.Calidad
V16 = round(riel.Tension, 2)
V17 = round(riel.Limite, 2)

U0 = ' '
U1 = ' [kN/cm²] '
U2 = ' [-] '
U3 = ' [-] '
U4 = ' [kN] '
U5 = ' [kN] '
U6 = '  '
U7 = '  '
U8 = ' [cm³] '
U9 = ' [cm] '
U10 = ' [-] '
U11 = ' [kN] '
U12 = ' [-] '
U13 = '  '
U14 = '  '
U15 = ' [-] '
U16 = ' [kN/cm²] '
U17 = ' [kN/cm²] '

parametro = np.array([P0,P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,P13,P14,P15,P16,P17])
valor= np.array([V0,V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17])
unidad = np.array([U0,U1,U2,U3,U4,U5,U6,U7,U8,U9,U10,U11,U12,U13,U14,U15,U16,U17])

print('\nVERIFICACIÓN RIEL')
print('--------------------------------------------------------------------------')
datos = {'PARÁMETRO': parametro, 'VALOR': valor, 'UNIDAD': unidad}
df = pd.DataFrame(datos)
#print(df.head())
print (df.loc[1:])
print('---------------------------------------------------------------------------')

with pd.ExcelWriter('D:\APP_REPORTES\Reporte_Riel.xlsx') as writer:
    df.to_excel(writer, sheet_name='Riel', index=False, float_format="%.2f")

print ('\n!!! Datos guardados con exitos ¡¡¡')