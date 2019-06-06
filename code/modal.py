# -*- coding: utf-8 -*-
# formulario para inroducir datos en gastos de sulato por mano-> GSM
#
import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gdk, Gio, Pango
import sys
import time

class Modal:
    """
    *******************************************************************************
        clase que inicia la ventana modal para recoger datos
    *******************************************************************************
    """
    """
    *************************
        variables de clase
    *************************
    """
    ventana_principal = None            # La ventana
    ventana_modal = None                # El modal
    mano = None                         # mano del sulfato con la que estamos
    Ano=None                            # ano para hacer las onsultas a la bd
    Layout = Gtk.Grid()                 # layout delmodal para colocar los controles

    N_lbl = 6                           # numero de controles repetidos en la mano de sulfatos
    ID=None
    estadios = []                       # estadios para el combobox
    sulfatos = []                       # array con los datos de sulfatos para los combos box
    cantidad=[]
    dosis=[]
    litros=None
    fecha=None
    # etiquetas
    lbl_titulo = Gtk.Label()            # label para el titulo
    lbl_fecha = Gtk.Label()             # label para la fecha
    lbl_litros = Gtk.Label()            # label para litross
    lbl_sulfato = Gtk.Label()           #
    lbl_cantidad = Gtk.Label()          #
    lbl_dosis = Gtk.Label()             #
    lbl_cant = []                       # label para las cantidades
    lbl_gr = []                         # label para los gr
    # combos
    cmb_estadios = Gtk.ComboBox()       # combo para los estadios
    cmb_sul = []                        # array con los comnbobox de los sulfatos
    #textos editables
    txt_fecha = Gtk.Entry()             # campo entry para la fecha
    txt_litros = Gtk.Entry()            # campo enrty para los litros
    txt_dosis = []                      # array con los entry
    line=None                           # campo de separacion
    btn_close=None                      # boton de cierre del modal




    def __init__(self):
        """
        ***************************************************************
            funcion que inicializa el objeto modal sin poder usarlo
        ***************************************************************
        """
        self.ventana_modal = Gtk.Window()
        self.ventana_modal = Gtk.Window(Gtk.WindowType.TOPLEVEL)
        self.ventana_modal.set_title("ventana modal")
        self.ventana_modal.connect('delete-event', self.hide)  # ocultamos el dialogo
        self.ventana_modal.resize(500, 350)
        # funciones a ejecutar para crear el modal(sin parametros)
        self.crear_widgets()
        self.asignar_propiedades_gr()
        self.construir_layout()


    def show(self):
        """
        ************************************
            funcion para mostar el modal
        ************************************
        """
        self.ventana_modal.show_all()
        return True


    def hide(self, widget, callback_data=None):
        """
        *************************************
            funcion para ocultar el modal
        *************************************
        """
        self.ventana_modal.hide()
        #print(self.ventana_modal.hide())
        return (True)

    def crear_widgets(self):
        """
        *****************************************************
            funcion que crea los widgets para el modal
        *****************************************************
        """
        # defincion de label para cantidad y gr
        for value in range(0,self.N_lbl):
            self.lbl_cant.append(Gtk.Label())
            self.lbl_gr.append(Gtk.Label())

        # defincion de comboBox para sulfato
        for value in range(0, self.N_lbl):
            self.cmb_sul .append(Gtk.ComboBox())
        # defincion de comboBox para estadios
        self.cmb_estadios = Gtk.ComboBox()

        # defincion de entry para fecha y litros
        self.txt_fecha = Gtk.Entry()
        self.txt_litros = Gtk.Entry()
        # defincion de entry para dosis
        for value in range(0, self.N_lbl):
            self.txt_dosis.append(Gtk.Entry())

        # defincion de botton para cerrar el botton
        self.btn_close = Gtk.Button.new_with_label("guardar cambios")

        self.btn_close.connect("clicked", self.btn_guardarcambios_on_click, [self.ventana_principal, ])

    def asignar_propiedades_gr(self):

        # definir el texto y los atributos para la etiqueta gr
        # definimos las propidades para centar y usar las cadenas pango
        for value in range(0, self.N_lbl):
            self.lbl_gr[value].set_text('<span size="xx-large">gr</span>')
            self.lbl_gr[value].set_justify(Gtk.Justification.CENTER)
            self.lbl_gr[value].set_use_markup(True)

    def asignar_propiedades_cant(self, cantidad):

        # definir el texto y los atributos para la etiqueta gr
        # definimos las propidades para centar y usar las cadenas pango
        for value in range(0, self.N_lbl):
            self.lbl_cant[value].set_text('<span size="xx-large">'+cantidad[value]+'</span>')
            self.lbl_cant[value].set_justify(Gtk.Justification.CENTER)
            self.lbl_cant[value].set_use_markup(True)

    def asignar_propiedades_dosis(self, dosis):

        # definir el texto y los atributos para la etiqueta gr
        # definimos las propidades para centar y usar las cadenas pango
        for value in range(0, self.N_lbl):
            self.txt_dosis[value].set_text(dosis[value])

    def modificar_propiedades_cmb_sul(self,combo_box,desired_entries,selecion):
        model = combo_box.get_model()
        combo_box.set_model(None)
        #print(type(combo_box))
        #print(type(model))
        model.clear()

        for entry in desired_entries:
            model.append([entry])
        combo_box.set_model(model)
        combo_box.set_active(selecion)

    def asignar_propiedades__cmb_sul(self,sulfatos,value,pos):
        sulfatos_store = Gtk.ListStore(str)
        sulfatos_cell = Gtk.CellRendererText()
        for sulfato in range(0, (len(sulfatos) - 1)):  # (0,13)
            sulfatos_store.append((sulfatos[sulfato],))

        self.cmb_sul[pos].set_model(sulfatos_store)
        self.cmb_sul[pos].pack_start(sulfatos_cell, True)
        self.cmb_sul[pos].add_attribute(sulfatos_cell, 'text', 0)
        self.cmb_sul[pos].set_active(value)

    def asignar_propiedades_estadios(self,estadios,value):
        estadios_store = Gtk.ListStore(str)
        estadios_cell = Gtk.CellRendererText()

        for estadio in range(0, (len(estadios) - 1)):  # (0,13)
            estadios_store.append((estadios[estadio],))

        self.cmb_estadios.set_model(estadios_store)
        self.cmb_estadios.pack_start(estadios_cell, True)
        self.cmb_estadios.add_attribute(estadios_cell, 'text', 0)
        self.cmb_estadios.set_active(value)

    def asignar_propiedades_litros(self, litros):
        self.txt_litros.set_text(litros)

    def asignar_propiedades_fecha(self, fecha):
        #self.txt_fecha.set_text(fecha+"/"+str(self.Ano))
        self.txt_fecha.set_text(fecha)

    def asignar_propiedades_titulo(self,*args):
        self.lbl_titulo.set_text('<span color="#993401"size="xx-large">' + "Mano " + str(self.mano) + " del Año " + str(self.Ano) + " " + str(self.estadios[self.cmb_estadios.get_active()]) + '</span>')#
        self.lbl_titulo.set_justify(Gtk.Justification.CENTER)
        self.lbl_titulo.set_use_markup(True)

    def calcular_cantidad(self, cantidad, dosis, litros):
        if (int(litros)==0):
            cantidad =["0","0","0","0","0","0"]
        else:
            for value in range(0,self.N_lbl):
                cantidad[value]=str(int(litros) * int(dosis[value])//100)

        return cantidad


    def construir_layout(self):
        """
        ****************************
            asignacion al layout
        ****************************
        """
        # grid layout sobre el que iran todos los controles

        self.Layout.attach(self.lbl_titulo, 0, 0, 7, 1)
        self.Layout.attach(self.cmb_estadios, 7, 0, 3, 1)

        self.Layout.attach(self.lbl_fecha, 0, 1, 3, 1)
        self.Layout.attach(self.lbl_litros, 6, 1, 4, 1)

        self.Layout.attach(self.txt_fecha, 0, 2, 3, 1)
        self.Layout.attach(self.txt_litros, 6, 2, 4, 1)

        self.Layout.attach(self.lbl_sulfato, 0, 3, 3, 1)
        self.Layout.attach(self.lbl_dosis, 3, 3, 3, 1)
        self.Layout.attach(self.lbl_cantidad, 7, 3, 3, 1)

        for value in range(0,self.N_lbl):
            self.Layout.attach(self.cmb_sul[value], 0, (value+4), 3, 1)
            self.Layout.attach(self.txt_dosis[value], 3, (value+4), 3, 1)
            self.Layout.attach(self.lbl_cant[value], 7, (value+4), 2, 1)
            self.Layout.attach(self.lbl_gr[value], 9, (value+4), 2, 1)

        self.Layout.attach(self.btn_close, 8, 10, 2, 1)

        self.ventana_modal.add(self.Layout)

    def cargar_datos_modal(self,ID, estadios,sulfatos,cantidad,dosis,cmb_sulfatos, cmb_esadios,fecha,litros,mano,ano):
        self.ID=ID
        self.sulfatos = sulfatos
        self.estadios=estadios
        self.cantidad=cantidad
        self.dosis=dosis
        self.fecha=fecha
        self.litros=litros
        self.Ano = ano
        self.mano = mano


        if (self.cmb_sul[0].get_active() == int(-1)):
            self.asignar_propiedades__cmb_sul(self.sulfatos,cmb_sulfatos[0],0)
            self.modificar_propiedades_cmb_sul(self.cmb_sul[0], self.sulfatos, cmb_sulfatos[0])
        else:
            self.modificar_propiedades_cmb_sul(self.cmb_sul[0], self.sulfatos, cmb_sulfatos[0])
        if (self.cmb_sul[1].get_active() == int(-1)):
            self.asignar_propiedades__cmb_sul(self.sulfatos,cmb_sulfatos[1],1)
            self.modificar_propiedades_cmb_sul(self.cmb_sul[1], self.sulfatos, cmb_sulfatos[1])
        else:
            self.modificar_propiedades_cmb_sul(self.cmb_sul[1], self.sulfatos, cmb_sulfatos[1])
        if (self.cmb_sul[2].get_active() == int(-1)):
            self.asignar_propiedades__cmb_sul(self.sulfatos,cmb_sulfatos[2],2)
            self.modificar_propiedades_cmb_sul(self.cmb_sul[2], self.sulfatos, cmb_sulfatos[2])
        else:
            self.modificar_propiedades_cmb_sul(self.cmb_sul[2], self.sulfatos, cmb_sulfatos[2])
        if (self.cmb_sul[3].get_active() == int(-1)):
            self.asignar_propiedades__cmb_sul(self.sulfatos,cmb_sulfatos[3],3)
            self.modificar_propiedades_cmb_sul(self.cmb_sul[3], self.sulfatos, cmb_sulfatos[3])
        else:
            self.modificar_propiedades_cmb_sul(self.cmb_sul[3], self.sulfatos, cmb_sulfatos[3])
        if (self.cmb_sul[4].get_active() == int(-1)):
            self.asignar_propiedades__cmb_sul(self.sulfatos,cmb_sulfatos[4],4)
            self.modificar_propiedades_cmb_sul(self.cmb_sul[4], self.sulfatos, cmb_sulfatos[4])
        else:
            self.modificar_propiedades_cmb_sul(self.cmb_sul[4], self.sulfatos, cmb_sulfatos[4])
        if (self.cmb_sul[5].get_active() == int(-1)):
            self.asignar_propiedades__cmb_sul(self.sulfatos,cmb_sulfatos[5],5)
            self.modificar_propiedades_cmb_sul(self.cmb_sul[5], self.sulfatos, cmb_sulfatos[5])
        else:
            self.modificar_propiedades_cmb_sul(self.cmb_sul[5], self.sulfatos, cmb_sulfatos[5])


        if (self.cmb_estadios.get_active() == int(-1)):
            self.asignar_propiedades_estadios(self.cmb_estadios,cmb_esadios)
            self.modificar_propiedades_cmb_sul(self.cmb_estadios, self.estadios, cmb_esadios)
        else:
            self.modificar_propiedades_cmb_sul(self.cmb_estadios, self.estadios, cmb_esadios)

        self.asignar_propiedades_litros(self.litros)
        self.asignar_propiedades_fecha(self.fecha)
        self.cantidad = self.calcular_cantidad(self.cantidad, self.dosis, self.litros)
        self.asignar_propiedades_cant(self.cantidad)
        self.asignar_propiedades_dosis(self.dosis)
        #
        #   termino de  construir el layout
        #
        self.cmb_estadios.connect('changed', self.on_changed_cmb_estadios, [self.Ano, self.mano])

        self.asignar_propiedades_titulo()

    def recoger_datos(self):
        res_sulfato=[0,0,0,0,0,0]
        self.estadios=self.cmb_estadios.get_active()
        self.litros=self.txt_litros.get_text()
        self.fecha=self.txt_fecha.get_text()

        for value in range(0,self.N_lbl):
            self.dosis[value]=self.txt_dosis[value].get_text()
            self.cantidad[value]=self.lbl_cant[value].get_text()
            res_sulfato[value]=self.cmb_sul[value].get_active()
        return(self.ID,self.mano,self.Ano,self.estadios,self.fecha,self.litros,res_sulfato,self.dosis,self.cantidad)

    def on_changed_cmb_estadios(self,*args):

        self.lbl_titulo.set_text('<span color="#993401"size="xx-large">' + "Mano " + str(args[1][1]) + " del Año " + str(
            args[1][0]) + " " + str(self.estadios[self.cmb_estadios.get_active()]) + '</span>')
        self.lbl_titulo.set_use_markup(True)

    def btn_guardarcambios_on_click(self,*args):
        datos=self.recoger_datos()
        print("cerrando modal")
        # pasar datos a la ventana principal
        # recogemos los sulfatos del modal
        sul=datos[6]
        #print(sul)
        #print(datos[8])
        #print(datos[7])
        dosis=self.calcular_cantidad(datos[8], datos[7], datos[5])

        datos[8][0] =dosis[0]
        datos[8][1] =dosis[1]
        datos[8][2] =dosis[2]
        datos[8][3] =dosis[3]
        datos[8][4] =dosis[4]
        datos[8][5] =dosis[5]
        # si coincide el sul[0] con el sulfato colocar el indice del sulfato+el indice de la mano
        # colocamos la cantidad en el sitio adecuad en el tree view
        # añado uno a a mano para colocarlo en el tree view por culpa de la columna de sulfatos

        if (sul[0] != 0 ):
            self.ventana_principal.Liststore[sul[0]][self.mano+1]= dosis[0]
        if (sul[1] != 0):
            self.ventana_principal.Liststore[sul[1]][self.mano+1]= dosis[1]
        if (sul[2] != 0):
            self.ventana_principal.Liststore[sul[2]][self.mano+1]= dosis[2]
        if (sul[3] != 0):
            self.ventana_principal.Liststore[sul[3]][self.mano+1]= dosis[3]
        if (sul[4] != 0):
            self.ventana_principal.Liststore[sul[4]][self.mano+1]= dosis[4]
        if (sul[5] != 0):
            self.ventana_principal.Liststore[sul[5]][self.mano+1]= dosis[5]
        #crear un registro en la bd
        self.ventana_principal.insertar_bd(datos)
        # hacer no visible la ventana actual
        self.hide(self,)



    def main(self):

        Gtk.main()


