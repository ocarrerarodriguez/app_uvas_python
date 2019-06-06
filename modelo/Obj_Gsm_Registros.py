class Obj_Gsm_Registros:
    def __init__(self, Obj_Gsm_Registros):
        self.ano = Obj_Gsm_Registros[0]
        self.mano = Obj_Gsm_Registros[1]
        self.estadio = Obj_Gsm_Registros[2]
        self.fecha = Obj_Gsm_Registros[3]
        self.litros = Obj_Gsm_Registros[4]
        self.sul0 = Obj_Gsm_Registros[5]
        self.sul1 = Obj_Gsm_Registros[6]
        self.sul2 = Obj_Gsm_Registros[7]
        self.sul3 = Obj_Gsm_Registros[8]
        self.sul4 = Obj_Gsm_Registros[9]
        self.sul5 = Obj_Gsm_Registros[9]
        self.can0 = Obj_Gsm_Registros[10]
        self.can1 = Obj_Gsm_Registros[11]
        self.can2 = Obj_Gsm_Registros[12]
        self.can3 = Obj_Gsm_Registros[13]
        self.can4 = Obj_Gsm_Registros[14]
        self.can5 = Obj_Gsm_Registros[15]
        self.dos0 = Obj_Gsm_Registros[16]
        self.dos1 = Obj_Gsm_Registros[17]
        self.dos2 = Obj_Gsm_Registros[18]
        self.dos3 = Obj_Gsm_Registros[19]
        self.dos4 = Obj_Gsm_Registros[20]
        self.dos5 = Obj_Gsm_Registros[21]

    @property
    def sulfatos_utilizados(self):
        return (self.sul0, self.sul1, self.sul2, self.sul3, self.sul4, self.sul5)

    @property
    def cantidad_utilizada(self):
        return (self.can0, self.can1, self.can2, self.can3, self.can4, self.can5)

    def __repr__(self):
        return "('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
            self.ano, self.mano, self.estadio, self.fecha, self.litros, self.sul0, self.sul1, self.sul2, self.sul3,
            self.sul4, self.sul5, self.can0, self.can1, self.can2, self.can3, self.can4, self.can5, self.dos0,
            self.dos1, self.dos2, self.dos3, self.dos4, self.dos5)

    @property
    def valor(self):
        return self.ano, self.mano, self.estadio, self.fecha, self.litros, self.sul0, self.sul1, self.sul2, self.sul3, self.sul4, self.sul5, self.can0, self.can1, self.can2, self.can3, self.can4, self.can5, self.dos0, self.dos1, self.dos2, self.dos3, self.dos4, self.dos5

    def valor_Insert(self):
        return self.ano, self.mano, self.estadio, self.fecha, self.litros, self.sul0, self.sul1, self.sul2, self.sul3, self.sul4, self.sul5, self.can0, self.can1, self.can2, self.can3, self.can4, self.can5, self.dos0, self.dos1, self.dos2, self.dos3, self.dos4, self.dos5

    def valor_Update(self):
        return self.estadio, self.fecha, self.litros, self.sul0, self.sul1, self.sul2, self.sul3, self.sul4, self.sul5, self.can0, self.can1, self.can2, self.can3, self.can4, self.can5, self.dos0, self.dos1, self.dos2, self.dos3, self.dos4, self.dos5, self.ano, self.mano

    def valor_new(self):
        return self.ano, self.mano, self.estadio, self.fecha, self.litros, self.sul0, self.sul1, self.sul2, self.sul3, self.sul4, self.sul5, self.can0, self.can1, self.can2, self.can3, self.can4, self.can5, self.dos0, self.dos1, self.dos2, self.dos3, self.dos4, self.dos5


    def clave_primaria(self):
        return self.ano, self.mano
