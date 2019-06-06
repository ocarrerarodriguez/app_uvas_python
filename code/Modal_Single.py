# -*- coding: utf-8 -*-
# formulario para inroducir datos en gastos de sulato por mano-> GSM
#
from gi.repository import Gtk, Gdk, Gio, Pango
import sys


class Modal_Single:
    """
    ***************************************************************
        funcion que inicializa el objeto modal sin poder usarlo
    ***************************************************************
    """

    def __init__(self):
        self.Dialog = Gtk.Window()
        self.Dialogo = Gtk.Window(Gtk.WindowType.TOPLEVEL)
        self.Dialog.connect('delete-event', self.hide)  # ocultamos el dialogo
        self.Dialog.resize(500, 350)
        self.estadios = None
        self.Ventana_Principal = None

    """
    **************************************************************
        funcion que inicializa el modal con paso de argumentos    
    **************************************************************
    """

    def setup_modal(self, estadios, sulfatos, ventana, mano=0, ano=2000):
        self.estadios = estadios
        self.Ventana_Principal = ventana
        self.sulfaos=sulfatos
        self.ano=ano
        self.mano=mano
        #
        self.crear_objetos()
        # definir_propiedades_cmb(sulfatos,estadios)
        self.asignar_propiedades(self.estadios,self.sulfaos, self.Ventana_Principal)
        self.construir_layout()

    """
    *****************************************************
            funcion que crea los widgets para el modal   
    *****************************************************
    """
    def definir_propiedades_cmb(self,sulfatos,estadios):
        # combo estadio
        for estadio in estadios:
            self.cmb_estadios.append_text(estadio)

        # combo sulfatos
        for sulfato in sulfatos:
            self.cmb_sul_0.append_text(sulfato)
            self.cmb_sul_1.append_text(sulfato)
            self.cmb_sul_2.append_text(sulfato)
            self.cmb_sul_3.append_text(sulfato)
            self.cmb_sul_4.append_text(sulfato)
            self.cmb_sul_5.append_text(sulfato)

        self.cmb_estadios.set_active(0)
        self.cmb_sul_0.set_active(0)
        self.cmb_sul_1.set_active(0)
        self.cmb_sul_2.set_active(0)
        self.cmb_sul_3.set_active(0)
        self.cmb_sul_4.set_active(0)
        self.cmb_sul_5.set_active(0)



    """
    *****************************************************
        funcion que crea los widgets para el modal   
    *****************************************************
    """

    def crear_objetos(self):
        # etiquetas
        self.lbl_titulo = Gtk.Label()
        self.lbl_fecha = Gtk.Label()
        self.lbl_litros = Gtk.Label()
        self.lbl_sulfato = Gtk.Label()
        self.lbl_cantidad = Gtk.Label()
        self.lbl_dosis = Gtk.Label()
        self.lbl_cantidad_0 = Gtk.Label()
        self.lbl_cantidad_1 = Gtk.Label()
        self.lbl_cantidad_2 = Gtk.Label()
        self.lbl_cantidad_3 = Gtk.Label()
        self.lbl_cantidad_4 = Gtk.Label()
        self.lbl_cantidad_5 = Gtk.Label()
        self.lbl_gr_0 = Gtk.Label()
        self.lbl_gr_1 = Gtk.Label()
        self.lbl_gr_2 = Gtk.Label()
        self.lbl_gr_3 = Gtk.Label()
        self.lbl_gr_4 = Gtk.Label()
        self.lbl_gr_5 = Gtk.Label()

        # combos
        self.cmb_estadios = Gtk.ComboBoxText()
        self.cmb_sul_0 = Gtk.ComboBoxText()
        self.cmb_sul_1 = Gtk.ComboBoxText()
        self.cmb_sul_2 = Gtk.ComboBoxText()
        self.cmb_sul_3 = Gtk.ComboBoxText()
        self.cmb_sul_4 = Gtk.ComboBoxText()
        self.cmb_sul_5 = Gtk.ComboBoxText()

        # textos editables
        self.txt_fecha = Gtk.Entry()
        self.txt_litros = Gtk.Entry()
        self.txt_dosis_0 = Gtk.Entry()
        self.txt_dosis_1 = Gtk.Entry()
        self.txt_dosis_2 = Gtk.Entry()
        self.txt_dosis_3 = Gtk.Entry()
        self.txt_dosis_4 = Gtk.Entry()
        self.txt_dosis_5 = Gtk.Entry()

        # lineas/botones
        self.line2 = Gtk.Separator()
        self.btn_guardarcambios = Gtk.Button.new_with_label("Guardar cambios")

    """
    *********************************************************
        funcion que cambia las propiedades de lso widgets   
    *********************************************************
    """

    def asignar_propiedades(self, estadios,sulfaos, ventana):
        # propiedad para centrar los widgts de tipo label
        self.lbl_titulo.set_justify(Gtk.Justification.CENTER)
        self.lbl_fecha.set_justify(Gtk.Justification.CENTER)
        self.lbl_sulfato.set_justify(Gtk.Justification.CENTER)
        self.lbl_cantidad.set_justify(Gtk.Justification.CENTER)
        self.lbl_dosis.set_justify(Gtk.Justification.CENTER)
        self.lbl_cantidad_0.set_justify(Gtk.Justification.CENTER)
        self.lbl_cantidad_1.set_justify(Gtk.Justification.CENTER)
        self.lbl_cantidad_2.set_justify(Gtk.Justification.CENTER)
        self.lbl_cantidad_3.set_justify(Gtk.Justification.CENTER)
        self.lbl_cantidad_4.set_justify(Gtk.Justification.CENTER)
        self.lbl_cantidad_5.set_justify(Gtk.Justification.CENTER)
        self.lbl_gr_0.set_justify(Gtk.Justification.CENTER)
        self.lbl_gr_1.set_justify(Gtk.Justification.CENTER)
        self.lbl_gr_2.set_justify(Gtk.Justification.CENTER)
        self.lbl_gr_3.set_justify(Gtk.Justification.CENTER)
        self.lbl_gr_4.set_justify(Gtk.Justification.CENTER)
        self.lbl_gr_5.set_justify(Gtk.Justification.CENTER)
        # definir el texto y los atributos para la etiqueta gr
        self.lbl_gr_0.set_text('<span size="xx-large">gr</span>')
        self.lbl_gr_1.set_text('<span size="xx-large">gr</span>')
        self.lbl_gr_2.set_text('<span size="xx-large">gr</span>')
        self.lbl_gr_3.set_text('<span size="xx-large">gr</span>')
        self.lbl_gr_4.set_text('<span size="xx-large">gr</span>')
        self.lbl_gr_5.set_text('<span size="xx-large">gr</span>')
        self.lbl_fecha.set_text('<span size="medium">fecha</span>')
        self.lbl_litros.set_text('<span size="medium">litros</span>')
        self.lbl_sulfato.set_text('<span size="medium">sulfatos</span>')
        self.lbl_dosis.set_text('<span size="medium">dosis</span>')
        self.lbl_cantidad.set_text('<span size="medium">cantidad</span>')
        # definicion de la propiedad para poder usar las cadenas pango

        self.lbl_fecha.set_use_markup(True)
        self.lbl_litros.set_use_markup(True)
        self.lbl_sulfato.set_use_markup(True)
        self.lbl_cantidad.set_use_markup(True)
        self.lbl_dosis.set_use_markup(True)
        self.lbl_cantidad_0.set_use_markup(True)
        self.lbl_cantidad_1.set_use_markup(True)
        self.lbl_cantidad_2.set_use_markup(True)
        self.lbl_cantidad_3.set_use_markup(True)
        self.lbl_cantidad_4.set_use_markup(True)
        self.lbl_cantidad_5.set_use_markup(True)
        self.lbl_gr_0.set_use_markup(True)
        self.lbl_gr_1.set_use_markup(True)
        self.lbl_gr_2.set_use_markup(True)
        self.lbl_gr_3.set_use_markup(True)
        self.lbl_gr_4.set_use_markup(True)
        self.lbl_gr_5.set_use_markup(True)

        self.definir_propiedades_cmb(sulfaos,estadios)
        self.lbl_titulo.set_text('<span color="#993401"size="xx-large">' + "Mano " + str(self.mano) + " del Año " + str(
            self.ano) + " " + self.cmb_estadios.get_active_text() + '</span>')
        self.lbl_titulo.set_use_markup(True)
        self.cmb_estadios.connect('changed', self.on_changed_cmb_estadios,[self.ano,self.mano])
        self.btn_guardarcambios.connect("clicked", self.btn_guardarcambios_on_click,ventana)

    """
    ****************************
        asignacion al layout
    ****************************
    """

    def construir_layout(self):
        # Create layout and add widgets
        # grid layout sobre el que iran todos los controles
        self.Layout = Gtk.Grid()

        self.Layout.attach(self.lbl_titulo, 0, 0, 7, 1)
        self.Layout.attach(self.cmb_estadios, 7, 0, 3, 1)

        self.Layout.attach(self.lbl_fecha, 0, 1, 3, 1)
        self.Layout.attach(self.lbl_litros, 6, 1, 4, 1)

        self.Layout.attach(self.txt_fecha, 0, 2, 3, 1)
        self.Layout.attach(self.txt_litros, 6, 2, 4, 1)

        self.Layout.attach(self.lbl_sulfato, 0, 3, 3, 1)
        self.Layout.attach(self.lbl_dosis, 3, 3, 3, 1)
        self.Layout.attach(self.lbl_cantidad, 7, 3, 3, 1)

        self.Layout.attach(self.cmb_sul_0, 0, 4, 3, 1)
        self.Layout.attach(self.txt_dosis_0, 3, 4, 3, 1)
        self.Layout.attach(self.lbl_cantidad_0, 7, 4, 2, 1)
        self.Layout.attach(self.lbl_gr_0, 9, 4, 2, 1)

        self.Layout.attach(self.cmb_sul_1, 0, 5, 3, 1)
        self.Layout.attach(self.txt_dosis_1, 3, 5, 3, 1)
        self.Layout.attach(self.lbl_cantidad_1, 7, 5, 2, 1)
        self.Layout.attach(self.lbl_gr_1, 9, 5, 2, 1)

        self.Layout.attach(self.cmb_sul_2, 0, 6, 3, 1)
        self.Layout.attach(self.txt_dosis_2, 3, 6, 3, 1)
        self.Layout.attach(self.lbl_cantidad_2, 7, 6, 2, 1)
        self.Layout.attach(self.lbl_gr_2, 9, 6, 2, 1)

        self.Layout.attach(self.cmb_sul_3, 0, 7, 3, 1)
        self.Layout.attach(self.txt_dosis_3, 3, 7, 3, 1)
        self.Layout.attach(self.lbl_cantidad_3, 7, 7, 2, 1)
        self.Layout.attach(self.lbl_gr_3, 9, 7, 2, 1)

        self.Layout.attach(self.cmb_sul_4, 0, 8, 3, 1)
        self.Layout.attach(self.txt_dosis_4, 3, 8, 3, 1)
        self.Layout.attach(self.lbl_cantidad_4, 7, 8, 2, 1)
        self.Layout.attach(self.lbl_gr_4, 9, 8, 2, 1)

        self.Layout.attach(self.cmb_sul_5, 0, 9, 3, 1)
        self.Layout.attach(self.txt_dosis_5, 3, 9, 3, 1)
        self.Layout.attach(self.lbl_cantidad_5, 7, 9, 2, 1)
        self.Layout.attach(self.lbl_gr_5, 9, 9, 2, 1)
        self.Layout.attach(self.btn_guardarcambios, 8, 10, 2, 1)

        # Set dialog layout into window
        self.Dialog.add(self.Layout)

    """
    ************************************
        funcion para mostar el modal
    ************************************
    """

    def show(self):
        self.Dialog.show_all()

    """
    *************************************
        funcion para ocultar el modal
    *************************************
    """

    def hide(self,widget, callback_data=None):
        self.Dialog.hide()

    """
    ****************************************************************
        funcion para el evento click en el boton guardar cambios 
    ****************************************************************
    """

    def btn_guardarcambios_on_click(self,widget, ventana, callback_data=None):
        #print("cerrando modal")
        # pasar datos a la ventana principal
        # recogemos los sulfatos del modal
        sul=["","","","","",""]
        in_sul=[0,0,0,0,0,0]
        i=0
        x=0
        in_sul[0]=0
        in_sul[1]=0
        in_sul[2]=0
        in_sul[3]=0
        in_sul[4]=0
        in_sul[5]=0

        sul[0]=self.cmb_sul_0.get_active_text()
        sul[1]=self.cmb_sul_1.get_active_text()
        sul[2]=self.cmb_sul_2.get_active_text()
        sul[3]=self.cmb_sul_3.get_active_text()
        sul[4]=self.cmb_sul_4.get_active_text()
        sul[5]=self.cmb_sul_5.get_active_text()
        # obtenemos las posicones en el tree view
        for x in range(0, len(sul)):
            for y in range(0, 13):
                if(self.sulfaos[y] == sul[x]):
                    in_sul[x]=y

        # print(in_sul[0])
        print(in_sul[0])
        print(in_sul[1])
        print(in_sul[2])
        print(in_sul[3])
        print(in_sul[4])
        print(in_sul[5])
        if(in_sul[0]!=0 or in_sul[1]!=0 or in_sul[2]!=0 or in_sul[3]!=0 or in_sul[4]!=0 or in_sul[5]!=0):
            # si coincide el sul[0] con el sulfato colocar el indice del sulfato+el indice de la mano
            # colocamos la cantidad en el sitio adecuad en el tree view
            # añado uno a a mano para colocarlo en el tree view por culpa de la columna de sulfatos
            if (in_sul[0] != 0 ):
                self.Ventana_Principal.liststore[in_sul[0]][self.mano+1]= self.txt_dosis_0.get_text()
            if (in_sul[1] != 0):
                self.Ventana_Principal.liststore[in_sul[1]][self.mano+1]= self.txt_dosis_1.get_text()
            if (in_sul[2] != 0):
                self.Ventana_Principal.liststore[in_sul[2]][self.mano+1]= self.txt_dosis_2.get_text()
            if (in_sul[3] != 0):
                self.Ventana_Principal.liststore[in_sul[3]][self.mano+1]= self.txt_dosis_3.get_text()
            if (in_sul[4] != 0):
                self.Ventana_Principal.liststore[in_sul[4]][self.mano+1]= self.txt_dosis_4.get_text()
            if (in_sul[5] != 0):
                self.Ventana_Principal.liststore[in_sul[5]][self.mano+1]= self.txt_dosis_5.get_text()
        # hacer no visible la ventana actual
        self.hide(self,)

    """
    ****************************************************************
        funcion para pasar los datos al modal 
    ****************************************************************
    """

    def Set_datos(self, mano=0, ano=2000, can0=0, can1=0, can2=0, can3=0, can4=0, can5=0):
        self.Dialog.set_title("Modal " + str(mano))

        self.lbl_cantidad_0.set_text('<span >' + can0 + '</span>')
        self.lbl_cantidad_1.set_text('<span >' + can1 + '</span>')
        self.lbl_cantidad_2.set_text('<span >' + can2 + '</span>')
        self.lbl_cantidad_3.set_text('<span >' + can3 + '</span>')
        self.lbl_cantidad_4.set_text('<span >' + can4 + '</span>')
        self.lbl_cantidad_5.set_text('<span >' + can5 + '</span>')
    def on_changed_cmb_estadios(self,*args):
        #print(args)
        self.lbl_titulo.set_text('<span color="#993401"size="xx-large">' + "Mano " + str(args[1][1]) + " del Año " + str(
            args[1][0]) + " " + self.cmb_estadios.get_active_text() + '</span>')
        self.lbl_titulo.set_use_markup(True)
