# -*- coding: utf-8 -*-
import os
import sqlite3
from app_2.BD.Obj_Cmb_Estadios import Obj_Cmb_Estadios
from app_2.BD.Obj_Cmb_Sulfatos import Obj_Cmb_Sulfatos
from app_2.BD.Obj_Treewiev_Mano import Obj_Treewiev_Mano
from app_2.BD.Obj_registro_mano import Obj_Registro_Mano
#from app_2.DB.tabla_gsm_vista.py impot *

"""
************************************************************************************************
la ruta se crea en tres pasos
-1  nombre del directorio con "os.Path.dirname(__file__)"
-2 concateno la ruta relativa con "os.Path.join()"
-3 colapso la ruta con "os.Path.normpath()"

con estos pass creo una ruta relativa a la base de datos
concatenando el directorio actual con ciertos comandos para llegar al archivo de la base de datos
************************************************************************************************ 
"""
def BD_inicio():

    Direc=os.path.dirname(__file__)
    Ruta = os.path.normpath(os.path.join(Direc, '..', 'BD', "uvas.db"))
    return (Ruta)

def conectar_bd(ruta_file):
    """"
    ****************************************
        metodo que abre la base de datos
    ****************************************
    """
    #print('conexion con el archivo '+ruta_file)
    return sqlite3.connect(ruta_file)

def cerrar_bd(connexion):
    """"
    ******************************************
        metodo que cierra la base de datos
    ******************************************
    """
    #print('cerrar conexion con el archivo ')
    connexion.close()

def crear_tablas(conn):
    """"
    ******************************************************
        metodo que crea las tablas en la Base de Datos
    ******************************************************
    """
    cursor = conn.cursor()
    tabla_sulfatos = "CREATE TABLE IF NOT EXISTS `sulfatos` (`id` INTEGER,`sulfatos` TEXT, PRIMARY KEY(`id`));"
    tabla_estadios = "CREATE TABLE IF NOT EXISTS `estadios` (`id` INTEGER, `estadio` TEXT, PRIMARY KEY(`id`));"
    tabla_treewiev = "CREATE TABLE IF NOT EXISTS`treewiev`  (`ID` INTEGER, `Ano`TEXT,`sulfato` TEXT, `M0` TEXT, `M1` TEXT, `M2` TEXT, `M3` TEXT, `M4` TEXT , `M5` TEXT , `M6` TEXT , `M7` TEXT , `M8` TEXT , `M9` TEXT , `M10` TEXT, `M11` TEXT, `M12` TEXT, `M13` TEXT, `M14` TEXT, `M15` TEXT, PRIMARY KEY(`ID`));"
    tabla_registros="CREATE TABLE IF NOT EXISTS`registros`  (`ID` INTEGER, `mano` INTEGER,`Ano`TEXT ,`estadio` INTEGER, `fecha` TEXT, `litros` TEXT, `sulfatos0` INTEGER, `sulfatos1` INTEGER , `sulfatos2` INTEGER , `sulfatos3` INTEGER , `sulfatos4` INTEGER, `sulfatos5` INTEGER, `dosis0` TEXT , `dosis1` TEXT, `dosis2` TEXT, `dosis3` TEXT, `dosis4` TEXT, `dosis5` TEXT, `can0` TEXT , `can1` TEXT, `can2` TEXT, `can3` TEXT, `can4` TEXT, `can5` TEXT, PRIMARY KEY(`ID`));"
    cursor.execute(tabla_sulfatos);
    cursor.execute(tabla_estadios);
    cursor.execute(tabla_treewiev);
    cursor.execute(tabla_registros);
    conn.commit()
    #print("tablas creadas")

def iniciar_tablas(conn):
    """"
    ***********************************************************************
        metodo que crea los registros de las tablas en la Base de Datos
    ***********************************************************************
    """
    cursor = conn.cursor()
    tabla_sulfatos_insert= "INSERT INTO `sulfatos` (id,sulfatos) VALUES"
    tabla_sulfatos_values= "(0,'Branda'), (1,'Cupra'), (2,'Laitri'), (3,'Greetnal'), (4,'Dynali'), (5,'Lainzufre WG'), (6,'Festival'), (7,'Estuder Plus Pro'), (8,'Caldo Lainco'), (9,'Micene mancoceb(80%)'), (10,'Bayfolan Potasio'), (11,'Epsonita'), (12,'Switch');"
    tabla_estadios_insert = "INSERT INTO `estadios` (id,estadio) VALUES"
    tabla_estadios_values = "(0,'Yemas Inchadas'), (1,'Inicio Brotacion'), (2,'Hojas Extendidas'), (3,'Racimos Visibles'), (4,'Inicio Floracion'), (5,'Mitad Floracion'), (6,'Final Floracion'), (7,'Tamaño Perdigon'), (8,'Tamaño Guisante'), (9,'Cierre Racimo'), (10,'Inicio Envero'), (11,'Final Envero'), (12,'Inicio Madurcion'), (13,'Final Maduracion'), (14,'Pos Venvimia'), (15,'Ultima Mano Sulfato'), (16,'Repeticion por Lluvia'), (17,'Repeticon por Mildeo');"
    tabla_treewiev_insert = "INSERT INTO `treewiev` (ID,Ano,Sulfato,M0,M1,M2,M3,M4,M5,M6,M7,M8,M9,M10,M11,M12,M13,M14,M15) VALUES"

    tabla_treewiev_values = """

    (0,'2019_0','fechas'               ,'00/00','00/01','00/02','00/03','00/04','00/05','00/06','00/07','00/08','00/09','00/10','00/11','00/12','00/13','00/14','00/15'),
    (1,'2019_1','Cupra'                ,'5','10','15','20','25','0','0','0','0','0','0','0','0','0','0','0'),
    (2,'2019_2','Laitri'               ,'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'),
    (3,'2019_3','Greetnal'             ,'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'),
    (4,'2019_4','Dynali'               ,'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'),
    (5,'2019_5','Lainzufre WG'         ,'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'),
    (6,'2019_6','Festival'             ,'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'),
    (7,'2019_7','Estuder Plus Pro'     ,'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'),
    (8,'2019_8','Caldo Lainco'         ,'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'),
    (9,'2019_9','Micene mancoceb(80%)' ,'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'),
    (10,'2019_10','Bayfolan Potasio'   ,'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'),
    (11,'2019_11','Epsonita'           ,'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'),
    (12,'2019_12','Switch'             ,'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'),
    (13,'2018_0','fechas'              ,'00/00','00/01','00/02','00/03','00/04','00/05','00/06','00/07','00/08','00/09','00/10','00/11','00/12','00/13','00/14','00/15'),
    (14,'2018_1','Cupra'               ,'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'),
    (15,'2018_2','Laitri'              ,'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'),
    (16,'2018_3','Greetnal'            ,'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'),
    (17,'2018_4','Dynali'              ,'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'),
    (18,'2018_5','Lainzufre WG'        ,'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'),
    (19,'2018_6','Festival'            ,'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'),
    (20,'2018_7','Estuder Plus Pro'    ,'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'),
    (21,'2018_8','Caldo Lainco'        ,'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'),
    (22,'2018_9','Micene mancoceb(80%)','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'),
    (23,'2018_10','Bayfolan Potasio'   ,'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'),
    (24,'2018_11','Epsonita'           ,'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'),
    (25,'2018_12','Switch'             ,'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0')  
    ;
    """
    tabla_registro_insert = "INSERT INTO `registros` VALUES"
    tabla_registro_values ="""
    (0,0,'2019_0',1,'00/00/2019','200',1,2,3,4,5,6,'100','100','100','100','100','100','200','200','200','200','200','200'),
    (1,1,'2019_1',2,'00/00/2019','200',1,2,3,4,5,6,'100','100','100','100','100','100','200','200','200','200','200','200'),
    (2,2,'2019_2',3,'00/00/2019','400',1,2,3,4,5,6,'100','100','100','100','100','100','400','400','400','400','400','400'),
    (3,3,'2019_3',4,'00/00/2019','400',1,2,3,4,5,6,'100','100','100','100','100','100','400','400','400','400','400','400'),
    (4,4,'2019_4',5,'00/00/2019','600',1,2,3,4,5,6,'100','100','100','100','100','100','600','600','600','600','600','600'),
    (5,5,'2019_5',6,'00/00/2019','600',1,2,3,4,5,6,'100','100','100','100','100','100','600','600','600','600','600','600'),
    (6,6,'2019_6',7,'00/00/2019','800',1,2,3,4,5,6,'100','100','100','100','100','100','800','800','800','800','800','800'),
    (7,7,'2019_7',8,'00/00/2019','800',1,2,3,4,5,6,'100','100','100','100','100','100','800','800','800','800','800','800'),
    (8,8,'2019_8',1,'00/00/2019','800',1,2,3,4,5,6,'100','100','100','100','100','100','800','800','800','800','800','800'),
    (9,9,'2019_9',2,'00/00/2019','800',1,2,3,4,5,6,'100','100','100','100','100','100','800','800','800','800','800','800'),
    (10,10,'2019_10',3,'00/00/2019','800',1,2,3,4,5,6,'100','100','100','100','100','100','800','800','800','800','800','800'),
    (11,11,'2019_11',4,'00/00/2019','800',1,2,3,4,5,6,'100','100','100','100','100','100','800','800','800','800','800','800'),
    (12,12,'2019_12',5,'00/00/2019','800',1,2,3,4,5,6,'100','100','100','100','100','100','800','800','800','800','800','800'),
    (13,13,'2019_13',6,'00/00/2019','800',1,2,3,4,5,6,'100','100','100','100','100','100','800','800','800','800','800','800'),
    (14,14,'2019_14',7,'00/00/2019','800',1,2,3,4,5,6,'100','100','100','100','100','100','800','800','800','800','800','800'),
    (15,15,'2019_15',8,'00/00/2019','800',1,2,3,4,5,6,'100','100','100','100','100','100','800','800','800','800','800','800'),
    (16,16,'2019_16',9,'00/00/2019','800',1,2,3,4,5,6,'100','100','100','100','100','100','800','800','800','800','800','800');
    """
    cursor.execute((tabla_sulfatos_insert+tabla_sulfatos_values));
    cursor.execute((tabla_estadios_insert+tabla_estadios_values));
    cursor.execute((tabla_treewiev_insert + tabla_treewiev_values));
    cursor.execute((tabla_registro_insert + tabla_registro_values));
    conn.commit()
    #print("registros insertados")

def iniciar_bd(ruta):
    conn = conectar_bd(ruta)
    crear_tablas(conn)
    iniciar_tablas(conn)
    #print("pasando por aqui")
def BD_convertir(reg,tabla):
    salida=[]
    obj_sul = None
    obj_est = None
    obj_tre = None
    obj_reg = None

    if (tabla=="sulfatos"):
        for sulfato in reg:
            obj_sul= Obj_Cmb_Sulfatos (sulfato)
            salida.append(obj_sul.valor())

    if (tabla=="estadios"):
        for estadio in reg:
            obj_est= Obj_Cmb_Estadios (estadio)
            salida.append(obj_est.valor())

    if (tabla=="treewiev_entrada"):
        for treewiev in reg:
            obj_tre= Obj_Treewiev_Mano (treewiev)
            salida.append(obj_tre.clave_primaria())
    if (tabla=="treewiev"):
        for treewiev in reg:
            obj_tre= Obj_Treewiev_Mano (treewiev)
            salida.append(obj_tre.valor())

    if (tabla == "registros"):
        for registro in reg:
            obj_reg = Obj_Registro_Mano(registro)
            salida.append(obj_reg.valor())
    #print(salida)
    return (salida)



