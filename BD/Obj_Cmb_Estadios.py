class Obj_Cmb_Estadios:
    def __init__(self, obj_cmb_estadios):
        self.Id = obj_cmb_estadios[0]
        self.estadios = obj_cmb_estadios[1]

    # override
    def __repr__(self):
        return "('{}','{}')".format(self.Id, self.estadios)

    def valor(self):
        return self.estadios

    def valor_Insert(self):
        return self.Id, self.estadios

    def valor_Update(self):
        return self.estadios, self.Id

    def valor_new(self):
        return self.Id, self.estadios

    def clave_primaria(self):
        return self.Id,
