# -*- coding: utf-8 -*-

import sys
import os
import datetime
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from app_2.app.BD import BD_inicio,iniciar_bd,conectar_bd,cerrar_bd,BD_convertir
from app_2.code.Botonera import Botonera
from app_2.code.modal import Modal
from app_2.app.informe1 import informe_gsm
sys.path.append("./")



class Ventana:
    """
    *******************************************************************************
        clase que inicia la ventana principal dando asi la funcionalidad basica
    *******************************************************************************
    """
    """
    *************************
        variables de clase
    *************************
    """
    ventana_principal = None    # La ventana
    ventana_modal     = None    # El modal
    Sulfatos    = None          # el array con los sulfatos del año
    Estadios    = None          # el array con los estadios para el combo de estadios
    Mano        = None          # el array con los datos de la self.Mano correspondiente
    Registro    = None

    Liststore   = None          # La lista donde se almacenann los datos del tree view
    treeview    = None          # widget que contiene las filas de list store
    menu        = None          # widget que contiene la barra de botones con la configuracion y las self.Manos
    layout      = None
    scroll      = None
    Ano         = None

    def __init__(self):
        """
        ******************************************************************
            fucion que inicializa la ventana principal carga
            la GUI la base de datos y hace las operaciones pertinentes
        ******************************************************************
        """
        self.ventana_principal = Gtk.Window(Gtk.WindowType.TOPLEVEL)
        self.ventana_principal.set_position(Gtk.WindowPosition.CENTER)
        self.ventana_principal.set_title("Adeneira el mejor albariño que puedas imaginar")
        self.ventana_principal.set_size_request(640, 480)
        self.ventana_principal.connect("delete_event", self.ventana_close_event)
        # iniciamos los array
        self.Mano = []
        self.Sulfatos = []
        self.Estadios = []
        self.Registroegistro = []

        self.now = datetime.datetime.now()
        self.Ano=self.now.year
        # arrancamos la Base de Datos
        self.BD()
        self.GUI()
        # Barras de desplazamiento para el contenedor
        self.scroll = Gtk.ScrolledWindow()
        self.scroll.add(self.treeview)
        #creacion de la botonera
        self.menu = Botonera()
        self.menu.botones_asignar_senales(self, self.Registro,self.Sulfatos,self.Estadios)


        # creacion del layout
        self.layout = Gtk.VBox(False, 0)
        self.layout.pack_start(self.menu.return_botonera(), False, False, 3)
        self.layout.pack_start(self.scroll, True, True, 3)
        self.ventana_principal.add(self.layout)

        self.ventana_principal.show_all()

    def GUI(self):
        """
        ************************************************************
            fucion que inicializa la interfaz grafica de usuario
        *************************************************************
        """
        """
        ************************************************************
            definicion y seteo de la variable liststore     
        *************************************************************
        """
        self.Liststore = Gtk.ListStore(str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str)
        self.Liststore.append((self.Mano[0]))
        self.Liststore.append((self.Mano[1]))
        self.Liststore.append((self.Mano[2]))
        self.Liststore.append((self.Mano[3]))
        self.Liststore.append((self.Mano[4]))
        self.Liststore.append((self.Mano[5]))
        self.Liststore.append((self.Mano[6]))
        self.Liststore.append((self.Mano[7]))
        self.Liststore.append((self.Mano[8]))
        self.Liststore.append((self.Mano[9]))
        self.Liststore.append((self.Mano[10]))
        self.Liststore.append((self.Mano[11]))
        self.Liststore.append((self.Mano[12]))

        # el contenedor de las filas
        self.treeview = Gtk.TreeView()
        # moldear el contenedor
        self.treeview.set_model(self.Liststore)

        # Crear la columna para la lista
        self.treeview.append_column(Gtk.TreeViewColumn('Sulfatos', Gtk.CellRendererText(), text=0))
        self.treeview.append_column(Gtk.TreeViewColumn('0', Gtk.CellRendererText(), text=1))
        self.treeview.append_column(Gtk.TreeViewColumn('1', Gtk.CellRendererText(), text=2))
        self.treeview.append_column(Gtk.TreeViewColumn('2', Gtk.CellRendererText(), text=3))
        self.treeview.append_column(Gtk.TreeViewColumn('3', Gtk.CellRendererText(), text=4))
        self.treeview.append_column(Gtk.TreeViewColumn('4', Gtk.CellRendererText(), text=5))
        self.treeview.append_column(Gtk.TreeViewColumn('5', Gtk.CellRendererText(), text=6))
        self.treeview.append_column(Gtk.TreeViewColumn('6', Gtk.CellRendererText(), text=7))
        self.treeview.append_column(Gtk.TreeViewColumn('7', Gtk.CellRendererText(), text=8))
        self.treeview.append_column(Gtk.TreeViewColumn('8', Gtk.CellRendererText(), text=9))
        self.treeview.append_column(Gtk.TreeViewColumn('9', Gtk.CellRendererText(), text=10))
        self.treeview.append_column(Gtk.TreeViewColumn('10', Gtk.CellRendererText(), text=11))
        self.treeview.append_column(Gtk.TreeViewColumn('11', Gtk.CellRendererText(), text=12))
        self.treeview.append_column(Gtk.TreeViewColumn('12', Gtk.CellRendererText(), text=13))
        self.treeview.append_column(Gtk.TreeViewColumn('13', Gtk.CellRendererText(), text=14))
        self.treeview.append_column(Gtk.TreeViewColumn('14', Gtk.CellRendererText(), text=15))
        self.treeview.append_column(Gtk.TreeViewColumn('15', Gtk.CellRendererText(), text=16))
        #self.treeview.append_column(Gtk.TreeViewColumn('16', Gtk.CellRendererText(), text=17))
        #self.treeview.append_column(Gtk.TreeViewColumn('17', Gtk.CellRendererText(), text=18))

    def BD(self):

        Ruta= BD_inicio()
        # sino existe la ruta archivo entonces procedemos a crear la base de datos
        # creamos las tablas sulfatos y estaios con los valores por defecto
        if (not (os.path.isfile(Ruta))):
            iniciar_bd(Ruta)
        conn = conectar_bd(Ruta)
        cursor = conn.cursor()
        # generamos las consultas para la BD
        select_estdios = "SELECT * FROM estadios;"
        select_sulfatos = "SELECT * FROM sulfatos;"
        select_treewiev = "select * from treewiev where Ano like'" + str(self.Ano) + "_%';"
        select_Registros = "select * from registros where Ano like'" + str(self.Ano) + "_%';"
        # ejecutamos las consultas en a bd
        cursor.execute(select_estdios)
        reg_estadios = cursor.fetchall()
        cursor.execute(select_sulfatos)
        reg_sulfatos = cursor.fetchall()
        cursor.execute(select_treewiev)
        reg_treewiev = cursor.fetchall()
        cursor.execute(select_Registros)
        reg_Registros=cursor.fetchall()
        # añadmos un registro neutro a la GUI para indicar que no hay selecionado nada
        reg_estadios.insert(0, (0, "Selecione una mano"))
        reg_sulfatos.insert(0, (0, "Selecione un sulfato"))
        cerrar_bd(conn)

        self.Estadios = BD_convertir(reg_estadios, "estadios")
        self.Sulfatos = BD_convertir(reg_sulfatos, "sulfatos")
        self.Mano     = BD_convertir(reg_treewiev, "treewiev")

        self.Registro = BD_convertir(reg_Registros,"registros")

    def insertar_bd(self,datos):
        print(str(datos[2]+"_"+str(datos[1])))
        ano=str(datos[2]+"_"+str(datos[1]))
        Ruta = BD_inicio()
        # sino existe la ruta archivo entonces procedemos a crear la base de datos
        # creamos las tablas sulfatos y estaios con los valores por defecto
        if (not (os.path.isfile(Ruta))):
            iniciar_bd(Ruta)
        conn = conectar_bd(Ruta)
        cursor = conn.cursor()
        sql_registros="""
           UPDATE registros
           SET mano = ?,Ano = ?,estadio = ?,fecha = ?,litros = ?,sulfatos0 = ?,sulfatos1 = ?,sulfatos2 = ?,sulfatos3 = ?,sulfatos4 = ?,sulfatos5 = ?,dosis0 = ?,dosis1 = ?,dosis2 = ?,dosis3 = ?,dosis4 = ?,dosis5 = ?,can0 = ?,can1 = ?,can2 = ?,can3 = ?,can4 = ?,can5 = ? 
           WHERE ID=?;
        """
        sql_treewiev = """
                   UPDATE treewiev
                   SET Ano = ?,sulfato = ?,M0 = ?,M1 = ?,M2 = ?,M3 = ?,M4 = ?,M5 = ?,M6 = ?,M7 = ?,M8 = ?,M9 = ?,M10 = ?,M11 = ?,M12 = ?,M13 = ?,M14 = ?,M15 = ? 
                   WHERE ID=?;
                """
        cursor.execute(sql_registros, (datos[1],ano,datos[3],datos[4] ,datos[5],datos[6][0],datos[6][1],datos[6][2],datos[6][3],datos[6][4],datos[6][5],datos[7][0],datos[7][1],datos[7][2],datos[7][3],datos[7][4],datos[7][5],datos[8][0],datos[8][1],datos[8][2],datos[8][3],datos[8][4],datos[8][5],datos[0]))
        select_treewiev = "select * from treewiev where Ano like'" + str(self.Ano) + "_%';"
        cursor.execute(select_treewiev)
        reg_treewiev = cursor.fetchall()
        self.Mano = BD_convertir(reg_treewiev, "treewiev_entrada")
        print(self.Mano)
        print(self.Liststore)
        print(len(self.Mano))
        for value in range(0,len(self.Mano)):
            print(self.Liststore[value][8],self.Liststore[value][9],self.Liststore[value][10])
            id=self.Mano[value][0]
            #print(id)
            cursor.execute(sql_treewiev, (
                self.Mano[value][1], self.Liststore[value][0], self.Liststore[value][1], self.Liststore[value][2], self.Liststore[value][3], self.Liststore[value][4], self.Liststore[value][5], self.Liststore[value][6],
                self.Liststore[value][7], self.Liststore[value][8],self.Liststore[value][9], self.Liststore[value][10], self.Liststore[value][11], self.Liststore[value][12], self.Liststore[value][13], self.Liststore[value][14], self.Liststore[value][15],
                self.Liststore[value][16], id))

        conn.commit()
        cerrar_bd(conn)

    def show(self):
        """
        ************************************
            funcion para mostar el modal
        ************************************
        """
        self.ventana_principal.show_all()
        return True

    def hide(self, widget, callback_data=None):
        """
        *************************************
            funcion para ocultar el modal
        *************************************
        """
        self.ventana_principal.hide()
        return True


    def ventana_close_event(self,*args):
        Gtk.main_quit()
        return False

    def main(self):
        Gtk.main()


if __name__ == "__main__":
    miventana = Ventana()
    miventana.main()

