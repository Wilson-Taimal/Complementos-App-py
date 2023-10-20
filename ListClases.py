import math

#--- CLASES GANCHO DE TIRO ---#
# ---------------------------------------------------------------------------------------- #
class Materiales():
    def __int__(self):
        self.fy = 1.0           # Fluencia de acero de refuerzo _ [MPa]
        self.u = 1.0            # Coeficiente de rodadura
        self.phiv = 1.0         # Factor de reducción a cortante
        self.phif = 1.0         # Factor de reducción a flexión

class Geometria():
    def __int__(self):
        self.b = 1.0            # Altura libre del gancho _ [cm]
        self.s = 1.0            # Distancia entre ejes de las barras del gancho _ [cm]
        self.Ze = 1.0           # Módulo de la sección elástico
        self.Zp = 1.0           # Modulo de la sección plástico
        self.Smin = 1.0         # Distancia mínima al borde
        self.Cmin = 1.0         # Distamcia mínima entre barras: ≤ a 1" = 6*db. ; > a 1" = 8*db.

        #- Zapata aislada -#
        self.A1 = 1.0
        self.A2 = 1.0
        self.B1 = 1.0
        self.B2 = 1.0
        self.C1 = 1.0
        self.C2 = 1.0
        self.BL = 1.0
        self.AP = 1.0
        self.HS = 1.0
        self.HL = 1.0
        self.HP = 1.0
        self.HT = 1.0

    def Ec_Ze(self, db):
        Ze = (math.pi * db**3)/32
        return Ze

    def Ec_Zp(self, db):
        Zp = (4/3) * ((db/2)**3)
        return Zp

class Refuerzo():
    def __int__(self):
        self.barra = 1.0        # Barras de refuerzo a usar: 5/8, 3/4, 7/8, 1, 1-1/8, 1-1/4, 1-3/8, 1-3/4
        self.db = 1.0           # Diámetro de la barra _ [cm]
        self. Asb = 1.0         # Área de la sección transversal de barra
        self.n = 1.0            # Cantidad de barras a emplear

    def f_db(self, barra):
        match barra:
            case '1/4':
                db = 0.64
            case '3/8':
                db = 0.95
            case '1/2':
                db = 1.27
            case '5/8':
                db = 1.59
            case '3/4':
                db = 1.91
            case '7/8':
                db = 2.22
            case '1':
                db = 2.54
            case '1-1/8':
                db = 2.87
            case '1-1/4':
                db = 3.23
            case '1-3/8':
                db = 3.58
            case '1-3/4':
                db = 4.30
        return db

    def f_As(self, barra):
        match barra:
            case '1/4':
                Asb = 0.32
            case '3/8':
                Asb = 0.71
            case '1/2':
                Asb = 1.29
            case '5/8':
                Asb = 1.99
            case '3/4':
                Asb = 2.84
            case '7/8':
                Asb = 3.87
            case '1':
                Asb = 5.10
            case '1-1/8':
                Asb = 6.45
            case '1-1/4':
                Asb = 8.19
            case '1-3/8':
                Asb = 10.06
            case '1-3/4':
                Asb = 14.52
        return Asb

class Cargas():
    def __int__(self):
        self.Fa = 1.0           # Fuerza aplicada al gancho _ [kN]
        self.N = 1.0            # Fuerza Normal, peso total del equipo _ [kN]
        self.M = 1.0            # Momento generado en la base del gancho  _ [kN.cm]
        self.T = 1.0            # Fuerza a tracción _ [kN]
        self.C = 1.0            # Fuerza a compresión _ [kN]

class Desarrollo():
    def __int__(self):
        self.FM = 1.0           # Factor de mayoración
        self.Fu = 1.0           # Fuerza mayorada aplicada al gancho _ [kN]
        self.Vu = 1.0           # Cortante ultima _ [kN]
        self.Mu = 1.0           # Momento flector último _ [kN.cm]
        self.Vn = 1.0           # Cortante nominal _ [kN]
        self.Mn = 1.0           # Momento nominal _ [kN]
        self.Esf_v = 1.0        # Esfuerzo a cortante _ [kN]
        self.Esf_t = 1.0        # Esfuerzo a tracción _ [kN]

    def Ec_Fu(self, Fa, FM):
        Fu = Fa * FM
        return Fu

    def Ec_Vn(self, phiv, fy, n, Asb):
        Vn = phiv * (fy/10) * n * Asb
        return Vn

    def Ec_Mn(self, phif, fy, n, Zp):
        Mn = phif * (fy/10) * n * Zp
        return Mn


#--- CLASES ESTRUCTURA ZAPATA AISLADA ---#
# ---------------------------------------------------------------------------------------- #
class Suelo():
    def __int__(self):
        self.rs = 1.0           # Peso especifico del material del lleno _ [kN/m³]
        self.phis = 1.0         # Ángulo de fricción del suelo
        self.Kp = 1.0           # Coeficiente empuje pasivo del suelo
        self.Fp = 1.0           # Fuerza del empuje pasivo _ [kN]
        self.H = 1.0            # Altura total del suelo _ [m]

    def Ec_Kp(self, phis):
        Kp = (math.tan(math.radians(45+phis/2)))**2
        return Kp

    def Ec_Fp(self, rs, Kp, H):
        Fp = 0.5*rs*Kp*H**2
        return Fp

class Estructura():
    def __int__(self):
        self.WE = 1.0           # Peso de la estructura _ [kN]
        self.WS = 1.0           # Peso del suelo _ [kN]
        self.Ma = 1.0           # Momenta actuante _ [kN.m]
        self.Mr = 1.0           # Momento resistente [kN.m]
        self.FS = 1.0           # Factor de seguridad al volcamiento
        self.HFa = 1.0          # Altura punto de aplicación de la carga _ [m]

    def Ec_WE(self, B1, B2, HP, A1, A2, HL):
        Vp = B1*B2*HP
        Vl = A1*A2*HL
        WE = (Vp + Vl) * 24
        return WE

    def Ec_WS(self, A1, A2, B1, B2, HS, rs):
        Vs = ((A1*A2) - (B1*B2)) * HS
        WS = Vs * rs
        return WS

    def Ec_Ma(self, Fa, HFa):
        Ma = Fa * HFa
        return Ma

    def Ec_Mr(self, WE, WS, Fp, H, A1, A2):
        WT = WE + WS
        Mr = (Fp * H/3) + (WT * min(A1, A2)/2)
        return Mr


#--- CLASES VERIFICACIÓN RIELES ---#
# ---------------------------------------------------------------------------------------- #
class Riel():
    def __int__(self):
        self.tipo = 1.0         # Tipo de riel
        self.Esf_t = 1.0        # Esfuerzo de trabajo. Los valores típicos son: 12.26, 15.44, 17.70, 19.98
        self.N_ruedas = 1.0     # NUmero de ruedas
        self.FM = 1.0           # Factor de mayoración
        self.Pa = 1.0           # Fuerza aplicada _ [kN]
        self.Pu = 1.0           # Fuerza mayorada _ [kN]
        self.Wx = 1.0           # Modulo de resistencia del riel _ [kN]
        self.L = 1.0            # Separacion entre platinas _ [cm]
        self.Pn = 1.0           # Fuerza que resiste el riel _ [kN]
        self.phi = 1.0          # Factor de resistencia del riel
        self.Calidad = 1.0      # Calidad: ASCE 60 (TR30), ASCE 75 (TR37), ASCE 90 (TR45), 115RE (TR57)
        self.Tension = 1.0      # Tensión de rotura _ [kN/cm²]
        self.Limite = 1.0       # Limite elastico _ [kN/cm²]

    def Calidad_Acero (self, Esf_t):
        match Esf_t:
            case 12.26:
                Calidad = 'R-500'
            case 15.44:
                Calidad = 'R-700'
            case 17.70:
                Calidad = 'R-800'
            case 19.98:
                Calidad = 'R-900'
        return Calidad

    def Tension_Rotura (self, Esf_t):
        match Esf_t:
            case 12.26:
                Tension = 54.03
            case 15.44:
                Tension = 68.05
            case 17.70:
                Tension = 78.05
            case 19.98:
                Tension = 88.06
        return Tension

    def Limite_Elastico (self, Esf_t):
        match Esf_t:
            case 12.26:
                Limite = 29.72
            case 15.44:
                Limite = 37.42
            case 17.70:
                Limite = 42.93
            case 19.98:
                Limite = 48.44
        return Limite

    def Mod_Resistencia (self, tipo):
        match tipo:
            case 'ASCE 60 (TR30)':
                Wx = 108.50
            case 'ASCE 75 (TR37)':
                Wx = 149.10
            case 'ASCE 90 (TR45)':
                Wx = 205.82
            case '115RE (TR57)':
                Wx = 297.00
        return Wx



