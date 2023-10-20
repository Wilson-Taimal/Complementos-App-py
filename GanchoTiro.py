############## DISEÑO GANCHO DE TIRO ##############
import numpy as np
import pandas as pd
from ListClases import *
mat = Materiales()
geo = Geometria()
ref = Refuerzo()
car = Cargas()
des = Desarrollo()


############## PARÁMETROS INICIALES ##############
mat.u = 0.20
mat.fy = 420
mat.phiv = 0.75
mat.phif = 0.90
geo.b = 9.60
geo.s = 35.0
car.N = 891.70
ref.barra = '1-3/8'
ref.n = 2.0
des.FM = 1.0
ref.db = ref.f_db(ref.barra)
ref.Asb = ref.f_As(ref.barra)


############## DESARROLLO - CÁLCULO ##############
#- Cargas sobre el gancho -#
car.Fa = mat.u * car.N
car.M = car.Fa * geo.b
car.T = car.M / geo.s
car.C = -car.M / geo.s
des.Fu = des.Ec_Fu(car.Fa, des.FM)
des.Vu = 0.7403 * des.Fu
des.Mu = 0.24088 * des.Fu * geo.b

#- Chequeo de esfuerzos -#
des.Esf_v = des.Fu / (2 * ref.n * ref.Asb)
des.Esf_t = car.T / (ref.n * ref.Asb)

if (mat.fy > des.Esf_v):
   fy_mayor_Esfv = 'Ok'
else:
    fy_mayor_Esfv = 'No'

if (mat.fy > des.Esf_t):
   fy_mayor_Esft = 'Ok'
else:
    fy_mayor_Esft = 'No'

#- Chequeo segun Norma NSR-10 -#
des.Vn = des.Ec_Vn(mat.phiv, mat.fy, ref.n, ref.Asb)
geo.Ze = geo.Ec_Ze(ref.db)
geo.Zp = geo.Ec_Zp(ref.db)
des.Mn = des.Ec_Mn(mat.phif, mat.fy, ref.n, geo.Zp)

if (des.Vn > des.Vu):
   Vn_mayor_Vu = 'Ok'
else:
    Vn_mayor_Vu = 'No'

if (des.Mn > des.Mu):
   Mn_mayor_Mu = 'Ok'
else:
    Mn_mayor_Mu = 'No'

geo.Smin = 6*ref.db
if (ref.db <= 2.54):
    geo.Cmin = (6*ref.db) + ref.db
else:
    geo.Cmin = (8*ref.db) + ref.db

############## REPORTE ##############
P1 = ' PARÁMETRO '
P2 = ' μ: Coeficiente de rodadura '
P3 = ' N: Fuerza normal (peso del equipo) '
P4 = ' F: Fuerza aplicada al gancho '
P5 = ' b: Altura libre del gancho (brazo de la barra) '
P6 = ' S: Distancia entre ejes de barras rectas del gancho '
P7 = ' M: Momento generado en la base del gancho '
P8 = ' T: Fuerza a tracción '
P9 = ' C: Fuerza a compresión '
P10 = '  '
P11 = ' VERIFICACIÓN DE ESFUERZOS '
P12 = ' fy: Esfuerzo de fluencia  Acero ASTM A706  '
P13 = ' ø: Diámetro de barra de acero del gancho de tiro '
P14 = ' ø: Diámetro de barra de acero del gancho de tiro '
P15 = ' Ab: Sección transversal para  barra '
P16 = ' σv = V / 2 ∙ A, Esfuerzo a cortante '
P17 = ' σt = T / A, Esfuerzo a tracción  '
P18 = ' σv < fy '
P19 = ' σt < fy '
P20 = '  '
P21 = ' METODOLOGÍA LRFD – NSR 10: '
P22 = ' VERIFICACIÓN CORTANTE '
P23 = ' fy: Esfuerzo de fluencia  Acero ASTM A706  '
P24 = ' As: Área de acero del gancho de tiro  '
P25 = ' n: Cantidad de barras '
P26 = ' Factor de mayoración '
P27 = ' ø (Coeficiente de reducción) '
P28 = ' øVn = ø ∙ n ∙ fy ∙ As '
P29 = ' Vu: Cortante última: 0.7403*Fu '
P30 = ' Chequeo øVn > Vu '
P31 = '  '
P32 = ' VERIFICACIÓN POR FLEXIÓN LOCAL '
P33 = ' Mu: Momento flector último: 0.24088 ∙ Fu ∙ b '
P34 = ' ø: Coeficiente de reducción por flexión '
P35 = ' Módulo de la sección elástico: S = (π ∙ d³)/32  '
P36 = ' Módulo de la sección plástico: Zp = (4/3) ∙ r³ '
P37 = ' Momento nominal: øMn = ø ∙ fy ∙ n ∙ Zp '
P38 = ' Chequeo øMn > Mu '
P39 = '  '
P40 = ' Dist. mínima al borde '
P41 = ' Dist. mínima entre ejes de barras '


V1 = '  '
V2 = round(mat.u, 2)
V3 = round(car.N, 2)
V4 = round(car.Fa, 2)
V5 = round(geo.b, 2)
V6 = round(geo.s, 2)
V7 = round(car.M, 2)
V8 = round(car.T, 2)
V9 = round(car.C, 2)
V10 = '  '
V11 = '  '
V12 = mat.fy
V13 = ref.barra
V14 = ref.db
V15 = ref.Asb
V16 = round(des.Esf_v, 2)
V17 = round(des.Esf_t, 2)
V18 = fy_mayor_Esfv
V19 = fy_mayor_Esft
V20 = '  '
V21 = '  '
V22 = '  '
V23 = mat.fy
V24 = ref.Asb
V25 = ref.n
V26 = des.FM
V27 = mat.phiv
V28 = round(des.Vn, 2)
V29 = round(des.Vu, 2)
V30 = Vn_mayor_Vu
V31 = '  '
V32 = '  '
V33 = round(des.Mu, 2)
V34 = mat.phif
V35 = round(geo.Ze, 2)
V36 = round(geo.Zp, 2)
V37 = round(des.Mn, 2)
V38 = Mn_mayor_Mu
V39 = '  '
V40 = round(geo.Smin, 2)
V41 = round(geo.Cmin, 2)

U1 = '  '
U2 = ' [-] '
U3 = ' [kN] '
U4 = ' [kN] '
U5 = ' [cm] '
U6 = ' [cm] '
U7 = ' [kN.cm] '
U8 = ' [kN] '
U9 = ' [kN] '
U10 = '  '
U11 = '  '
U12 = ' [MPa] '
U13 = ' [in] '
U14 = ' [cm] '
U15 = ' [cm²] '
U16 = ' [kN/cm²] '
U17 = ' [kN/cm²] '
U18 = ' [-] '
U19 = ' [-] '
U20 = '  '
U21 = '  '
U22 = '  '
U23 = ' [MPa] '
U24 = ' [cm²] '
U25 = ' [-] '
U26 = ' [-] '
U27 = ' [-] '
U28 = ' [kN] '
U29 = ' [kN] '
U30 = ' [-] '
U31 = '  '
U32 = '  '
U33 = ' [kN.cm] '
U34 = ' [-] '
U35 = ' [cm³] '
U36 = ' [cm³] '
U37 = ' [kN.cm] '
U38 = ' [-] '
U39 = '  '
U40 = ' [cm] '
U41 = ' [cm] '

parametro = np.array([P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,P13,P14,P15,P16,P17,P18,P19,P20,P21,P22,P23,P24,P25,P26,P27,P28,P29,P30,P31,P32,P33,P34,P35,P36,P37,P38,P39,P40,P41])
valor= np.array([V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28,V29,V30,V31,V32,V33,V34,V35,V36,V37,V38,V39,V40,V41])
unidad = np.array([U1,U2,U3,U4,U5,U6,U7,U8,U9,U10,U11,U12,U13,U14,U15,U16,U17,U18,U19,U20,U21,U22,U23,U24,U25,U26,U27,U28,U29,U30,U31,U32,U33,U34,U35,U36,U37,U38,U39,U40,U41])

print('\nVERIFICACIÓN RESISTENCIA DEL GANCHO DE TIRO')
print('----------------------------------------------------------------------------')
datos = {'PARÁMETRO': parametro, 'VALOR': valor, 'UNIDAD': unidad}
df = pd.DataFrame(datos)
#print(df.head())
print (df.loc[1:])
print('----------------------------------------------------------------------------')

with pd.ExcelWriter('D:\APP_REPORTES\Reporte_GanchoTiro.xlsx') as writer:
    df.to_excel(writer, sheet_name='Gancho', index=False, float_format="%.2f")

print ('\n!!! Datos guardados con exitos ¡¡¡')





