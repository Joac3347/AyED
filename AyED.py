from datetime import date

class Usuarios:
    def __init__(self) -> None:
        self.CodUsuario = 0
        self.NombreUsuario = ""
        self.ClaveUsuario = ""
        self.TipoUsuario = ""

class Locales:
    def __init__(self) -> None:
        self.CodLocal = 0
        self.NombreLocal = ""
        self.UbiLocal = ""
        self.RubroLocal = ""
        self.CodUsuario = 0
        self.Estado = ""

class Promociones:
    def __init__(self) -> None:
        self.CodPromo = 0
        self.TextoPromo = ""
        self.FechaDesdePromo = ""
        self.FechaHastaPromo = ""
        self.DiaSemana = [0] * 6 
        self.Estado = ""
        self.CodLocal = 0

class Uso_Promocion:
    def __init__(self) -> None:
        self.CodCliente = 0
        self.CodPromo = 0
        self.FechaUsoPromo = ""

class Novedades:
    def __init__(self) -> None:
        self.CodNovedad = 0
        self.TextoNovedad = ""
        self.FechaDesdeNovedad = ""
        self.FechaHastaNovedad = ""
        self.TipoUsuario = ""
        self.Estado = ""


AFU = "C:\TP3"
AFL = "C:\TP3"
AFP = "C:\TP3"
AFUP = "C:\TP3"
AFN = "C:\TP3"

ALU = open(AFU,"b + w")
ALL = open(AFL, "b + w")
ArrayUsuarios = [0] * 50

for i in range(50): 
  ArrayUsuarios[i] =  Usuarios()

ArrayUsuarios[0].CodUsuario = 1
ArrayUsuarios[0].NombreUsuario = "admin"
ArrayUsuarios[0].ClaveUsuario = 12345
ArrayUsuarios[0].TipoUsuario = "administrador"


print("1. Ingresar con usuario registrado")
print("2. Registrarse como cliente")
print("3. Salir")
