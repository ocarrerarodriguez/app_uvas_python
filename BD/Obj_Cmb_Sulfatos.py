class Obj_Cmb_Sulfatos:
    def __init__(self, Obj_Cmb_Sulfatos):
        self.Id = Obj_Cmb_Sulfatos[0]
        self.sulfatos = Obj_Cmb_Sulfatos[1]

    # Override
    def __repr__(self):
        return "('{}','{}')".format(self.Id, self.sulfatos)

    def valor(self):
        return self.sulfatos

    def valor_Insert(self):
        return self.Id, self.sulfatos

    def valor_Update(self):
        return self.sulfatos, self.Id

    def valor_new(self):
        return self.Id, self.sulfatos

    def clave_primaria(self):
        return self.Id,
