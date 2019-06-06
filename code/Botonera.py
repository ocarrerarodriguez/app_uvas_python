# -*- coding: utf-8 -*-
# widget que implementa una barra de botones que lanzalso modales de GSM
#
import sys
import os
from gi.repository import Gtk
sys.path.append("./")
from app_2.code.modal import Modal
from app_2.app.informe1 import informe_gsm


class Botonera:
    """
    *******************************************************************************
       widget que genera una barra de botones para el programa principal
    *******************************************************************************
    """
    """
    *************************
        variables de clase
    *************************
    """
    lay_Botonera = None     # layout que le devolveremos a la ventana principal
    N_Botones=17            #numero de botones en la Botonera
    Botones = []            # array con todos los botones de la botonera
    btn_Cadenas =[]         # array con el texto para los botones de la botonera
    btn_Imagenes = []       # array con la imagen para los botones de la botonera

    sulfatos=[]
    estadios=[]
    ventana = None          # puntero a la ventana principal de la app
    mano = None             #
    ano = None              #
    registros=[]
    """
    *********************************
        rutas empleadas en la app
    *********************************
    """
    img_sul = "../img/gui_sul_32.png"
    img_cog = "../img/gui_cog_32.png"
    ruta_pdf="../PDF/informePdf.pdf"

    def __init__(self):
        """
        ******************************************
            funcion que inicializa la botonera
        ******************************************
        """
        # La botonera
        self.lay_Botonera = Gtk.HBox()
        # los controles para la botonera
        for boton in range(0,self.N_Botones):
            self.Botones.append(Gtk.Button())

        # las btn_Cadenas para los botones
        for cadena in range(-1,self.N_Botones):
            if (cadena == -1):
                self.btn_Cadenas.append( "configuracion")
            else:
                self.btn_Cadenas.append("mano "+str(cadena))
        # las btn_Imagenes para los botones
        for cadena in range(0,self.N_Botones):
            if (cadena == 0):
                self.btn_Imagenes.append(self.img_cog)
            else:
                self.btn_Imagenes.append(self.img_sul)

        # llamamos a  la funcion para generar los layout
        self.init_botonera()

    def init_botonera(self):
        """
        ***************************************************************************************************
            funcion que genera los layouts. añade layouts a los botones.añade los botones a la botonera
        ***************************************************************************************************
        """
        # rutas a las imagenes

        for variable in range(0,self.N_Botones):
            if(variable==0):
                # modificamos los botones para que contengan la imagen y el texto asociado
                self.Botones[variable].add(self.layout_botton(self.img_cog, self.btn_Cadenas[variable]))

            else:
                # modificamos los botones para que contengan la imagen y el texto asociado
                self.Botones[variable].add(self.layout_botton(self.img_sul, self.btn_Cadenas[variable]))




    def layout_botton(self, archivodeimagen, etiqueta):
        """
        ******************************************************************
            funcion que fabrica el layout de los boones de la botonera
        ******************************************************************
        """
        # Creamos una caja horizontal
        caja = Gtk.VBox(False, 2)
        caja.set_border_width(2)

        # Creamos un objeto imagen
        imagen = Gtk.Image()
        imagen.set_from_file(archivodeimagen)

        # Creamos una etiqueta
        label = Gtk.Label(etiqueta)

        # Agregamos la imagen y la etiqueta a la caja
        caja.pack_start(imagen, False, False, 3)
        caja.pack_start(label, False, False, 3)
        # mostarmos la la imagen y la etiqueta
        imagen.show()
        label.show()
        return caja

    def return_botonera(self):
        """
        ******************************************************************
            funcion que devuelbe la botonera
        ******************************************************************
        """
        # añdir controles a la botonera
        for varia in range(0,self.N_Botones):
            self.lay_Botonera.add(self.Botones[varia])
        return self.lay_Botonera


    def botones_asignar_senales(self,ventana,registros,sulfatos,estadios):
        """
        ******************************************************************
           funcion que conecta los botones con las señales correspondientes
        ******************************************************************
        """

        # guardamos los estadios y sulfatos
        self.ventana = ventana
        self.mano =0
        self.registros=registros
        self.sulfatos=sulfatos
        self.estadios=estadios
        self.ventana.ventana_modal = Modal()
        #datos para el boton de configuracion
        datos_conf=[self.ruta_pdf,self.ventana.Liststore, 5, 4]
        #conectamos el boton configuracion con sus datos ala funcion on_configuracion_click
        self.Botones[0].connect("clicked", self.on_configuracion_click,datos_conf)
        # conectamos los botnones de la botonera con el evento cliked en la funcion on_boton_clicked()
        for boton in range(1,len(self.Botones)-1):
            #print(self.mano)
            datos=[self.registros[self.mano],self.sulfatos,self.estadios]
            self.Botones[boton].connect("clicked", self.on_boton_click, datos)
            self.mano += 1

    def on_boton_click(self, *args):
        """
        ******************************************************************
           funcion que conecta los botones con las señales correspondientes
        ******************************************************************
        """
        datos=[]
        datos = (args[1])
        registros = datos[0]
        sulfatos = datos[1]
        estadios = datos[2]
        print(registros)

        # inicio y muestro  el modal
        self.ventana.ventana_modal.ventana_principal = self.ventana
        self.ventana.ventana_modal.cargar_datos_modal(registros[0], estadios,sulfatos,registros[8],registros[7],registros[6], registros[3],registros[4],registros[5],registros[1],registros[2][:-2])
        #self.ventana.Modal.showall()
        self.ventana.ventana_modal.show()


    def on_configuracion_click(self,*args):
        informe_gsm(args[1][0], args[1][1],args[1][2],args[1][3])
