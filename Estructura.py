import numpy as np
import pandas as pd
from ListClases import *

mat = Materiales()
geo = Geometria()
sue = Suelo()
est = Estructura()
car = Cargas()

############## GEOMETRÍA ZAPATA AISLADA ##############
geo.B1 = 0.70
geo.B2 = 0.70
geo.C1 = 0.90
geo.C2 = 0.90
geo.BL = 0.10
geo.AP = 0.10
geo.HS = 1.50
geo.HL = 0.40

sue.rs = 20
sue.phis = 30
car.Fa = 178.34

Factor = 1.0

geo.A1 = geo.B1 + (2 * geo.C1)
geo.A2 = geo.B2 + (2 * geo.C2)
geo.HP = geo.HS + geo.AP + geo.BL
geo.HT = geo.HP + geo.HL


############## CHEQUEO AL VOLCAMIENTO ##############
sue.H = geo.HS + geo.HL
sue.Kp = sue.Ec_Kp(sue.phis)
sue.Fp = sue.Ec_Fp(sue.rs, sue.Kp, sue.H)
est.WE = est.Ec_WE(geo.B1, geo.B2, geo.HP, geo.A1, geo.A2, geo.HL )
est.WS = est.Ec_WS(geo.A1, geo.A2, geo.B1, geo.B2, geo.HS, sue.rs)
est.HFa = geo.HT
est.Ma = est.Ec_Ma(car.Fa, est.HFa)
est.Mr = est.Ec_Mr(est.WE, est.WS, sue.Fp, sue.H, geo.A1, geo.A2)

if (est.Mr/est.Ma >= Factor):
    est.FS = 'Ok'
else:
    est.FS = 'No cumple'


############## REPORTE EXCEL ##############
P0 = ' GEOMETRÍA '
P1 = ' A1: Longitud zapata dir x '
P2 = ' A2: Longitud zapata dir y '
P3 = ' B1: Longitud pedestal dir x '
P4 = ' B2: Longitud pedestal dir y '
P5 = ' C1: Distancia al borde dir x '
P6 = ' C2: Distancia al borde dir y '
P7 = ' BL: Borde libre '
P8 = ' AP: Acabado de patio '
P9 = ' HS: Altura del suelo '
P10 = ' HL: Espesor de la zapata '
P11 = ' HP: Altura pedestal '
P12 = ' HT: Altura total '
P13 = '  '
P14 = ' CHEQUEO A VOLCAMIENTO '
P15 = ' γs: Densidad material de lleno '
P16 = ' øs: Angulo de fricción del suelo '
P17 = ' Kp: coeficiente de empuje pasivo '
P18 = ' Fp: Fuerza del empuje pasivo '
P19 = ' Fa : Fuerza aplicada al gancho '
P20 = ' Wt : Peso total de la cimentación '
P21 = ' Ws : Peso del suelo '
P22 = ' Ma: momento actuante '
P23 = ' Mr: momento resistente '
P24 = f' F.S. al volcamiento ≥ {Factor} '

V0 = '  '
V1 = geo.A1
V2 = geo.A2
V3 = geo.B1
V4 = geo.B2
V5 = geo.C1
V6 = geo.C2
V7 = geo.BL
V8 = geo.AP
V9 = geo.HS
V10 = geo.HL
V11 = round(geo.HP, 2)
V12 = round(geo.HT, 2)
V13 = '  '
V14 = '  '
V15 = sue.rs
V16 = sue.phis
V17 = round(sue.Kp, 2)
V18 = round(sue.Fp, 2)
V19 = car.Fa
V20 = round(est.WE, 2)
V21 = round(est.WS, 2)
V22 = round(est.Ma, 2)
V23 = round(est.Mr, 2)
V24 = round(est.Mr/est.Ma, 2)

U0 = '  '
U1 = ' [m] '
U2 = ' [m] '
U3 = ' [m] '
U4 = ' [m] '
U5 = ' [m] '
U6 = ' [m] '
U7 = ' [m] '
U8 = ' [m] '
U9 = ' [m] '
U10 = ' [m] '
U11 = ' [m] '
U12 = ' [m] '
U13 = '  '
U14 = '  '
U15 = ' [kN/m³] '
U16 = ' [°] '
U17 = ' [-] '
U18 = ' [kN] '
U19 = ' [kN] '
U20 = ' [kN] '
U21 = ' [kN] '
U22 = ' [kN.m] '
U23 = ' [kN.m] '
U24 = est.FS

parametro = np.array([P0,P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,P13,P14,P15,P16,P17,P18,P19,P20,P21,P22,P23,P24])
valor= np.array([V0,V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24])
unidad = np.array([U0,U1,U2,U3,U4,U5,U6,U7,U8,U9,U10,U11,U12,U13,U14,U15,U16,U17,U18,U19,U20,U21,U22,U23,U24])

print('\nDISEÑO ZAPATA AISLADA PARA GANCHO DE TIRO')
print('--------------------------------------------------------------')
datos = {'PARÁMETRO': parametro, 'VALOR': valor, 'UNIDAD': unidad}
df = pd.DataFrame(datos)
#print(df.head())
print (df.loc[1:])
print('---------------------------------------------------------------')

with pd.ExcelWriter('D:\APP_REPORTES\Reporte_Zapata.xlsx') as writer:
    df.to_excel(writer, sheet_name='Zapata', index=False, float_format="%.2f")

print ('\n!!! Datos guardados con exitos ¡¡¡')

