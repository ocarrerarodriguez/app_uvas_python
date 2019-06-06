
class Obj_Treewiev_Mano:
    def __init__(self, obj_treewiev_mano):
        self.Id         = obj_treewiev_mano[0]
        self.Ano        = obj_treewiev_mano[1]
        self.sulfatos   = obj_treewiev_mano[2]
        self.mano0      = obj_treewiev_mano[3]
        self.mano1      = obj_treewiev_mano[4]
        self.mano2      = obj_treewiev_mano[5]
        self.mano3      = obj_treewiev_mano[6]
        self.mano4      = obj_treewiev_mano[7]
        self.mano5      = obj_treewiev_mano[8]
        self.mano6      = obj_treewiev_mano[9]
        self.mano7      = obj_treewiev_mano[10]
        self.mano8      = obj_treewiev_mano[11]
        self.mano9      = obj_treewiev_mano[12]
        self.mano10     = obj_treewiev_mano[13]
        self.mano11     = obj_treewiev_mano[14]
        self.mano12     = obj_treewiev_mano[15]
        self.mano13     = obj_treewiev_mano[16]
        self.mano14     = obj_treewiev_mano[17]
        self.mano15     = obj_treewiev_mano[18]





    # override
    def __repr__(self):
        return "('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(self.Id, self.sulfatos,self.mano0,self.mano1,self.mano2,self.mano3,self.mano4,self.mano5,self.mano6,self.mano7,self.mano8,self.mano9,self.mano10,self.mano11,self.mano12,self.mano13,self.mano14,self.mano15)

    def valor(self):
        return [self.sulfatos,self.mano0,self.mano1,self.mano2,self.mano3,self.mano4,self.mano5,self.mano6,self.mano7,self.mano8,self.mano9,self.mano10,self.mano11,self.mano12,self.mano13,self.mano14,self.mano15]

    def valor_Insert(self):
        return self.Id,self.Ano, self.sulfatos,self.mano0,self.mano1,self.mano2,self.mano3,self.mano4,self.mano5,self.mano6,self.mano7,self.mano8,self.mano9,self.mano10,self.mano11,self.mano12,self.mano13,self.mano14,self.mano15


    def valor_Update(self):
        return (self.Ano,self.sulfatos,self.mano0,self.mano1,self.mano2,self.mano3,self.mano4,self.mano5,self.mano6,self.mano7,self.mano8,self.mano9,self.mano10,self.mano11,self.mano12,self.mano13,self.mano14,self.mano15,self.mano16), self.Id

    def valor_new(self):
        return self.Id,self.Ano, self.sulfatos,self.mano0,self.mano1,self.mano2,self.mano3,self.mano4,self.mano5,self.mano6,self.mano7,self.mano8,self.mano9,self.mano10,self.mano11,self.mano12,self.mano13,self.mano14,self.mano15,self.mano16

    def clave_primaria(self):
        return self.Id,self.Ano
