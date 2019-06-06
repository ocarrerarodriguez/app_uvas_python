"""
(10, 0, 2019, 1, '00/00/2019', '400', [1, 2, 3, 4, 5, 6], ['100', '100', '100', '100', '100', '100'], ['400', '400', '400', '400', '400', '400'])
ID mano ano estadios fecha litos sulfatos dosis cantidad
"""

class Obj_Registro_Mano:

    mano=None
    ano=2019
    estadios=0
    fecha="00/00/2019"
    litros="0"

    sulfatos = []
    dosis = []
    cantidad = []

    def __init__(self, registro):
        self.Id             = int(registro[0])
        self.Ano            = registro[1]
        self.mano           = registro[2]
        self.estadios       = registro[3]
        self.fecha          = str(registro[4])
        self.litros         = str(registro[5])
        self.sulfatos=[registro[6],registro[7],registro[8],registro[9],registro[10],registro[11]]
        self.dosis   =[registro[12],registro[13],registro[14],registro[15],registro[16],registro[17]]
        self.cantidad=[registro[18],registro[19],registro[20],registro[21],registro[22],registro[23]]

    # override
    def __repr__(self):
        return "('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(self.Id,self.Ano,self.mano,self.estadios,self.fecha,self.litros,self.sulfatos,self.dosis,self.cantidad)

    def valor(self):

        return [self.Id, self.Ano, self.mano, self.estadios, self.fecha, self.litros, self.sulfatos, self.dosis,self.cantidad]

    def valor_Insert(self):
        return self.Id,self.Ano,self.mano,self.estadios,self.fecha,self.litros,self.sulfatos,self.dosis,self.cantidad

    def valor_Update(self):
        return (self.Ano,self.mano,self.estadios,self.fecha,self.litros,self.sulfatos,self.dosis,self.cantidad), self.Id

    def valor_new(self):
        return self.Id,self.Ano, self.sulfatos,self.mano0,self.mano1,self.mano2,self.mano3,self.mano4,self.mano5,self.mano6,self.mano7,self.mano8,self.mano9,self.mano10,self.mano11,self.mano12,self.mano13,self.mano14,self.mano15,self.mano16

    def clave_primaria(self):
        return self.Id,self.Ano

