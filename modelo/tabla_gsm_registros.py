from modelo.Obj_Gsm_Registros import Obj_Gsm_Registros
# funciones de la tabla registroGSM


#funcion que crea la tabla registroGSM
def create_table_Gsm_Registros(conn):
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS 'registroGSM' (`ano`INTEGER,`mano`INTEGER,`estadio`TEXT,`fecha`TEXT,`litros`INTEGER,`sul0`TEXT,`Sul1`	TEXT,`sul2`	TEXT,`sul3`	TEXT,`sul4`	TEXT,`sul5`	TEXT,`can0`	INTEGER,`can1`	INTEGER,`can2`	INTEGER,`can3`	INTEGER,`can4`	INTEGER,`can5`	INTEGER,`dos0`	INTEGER,`dos1`	INTEGER,`dos2`	INTEGER,`dos3`	INTEGER,`dos4`	INTEGER,`dos5`	INTEGER,PRIMARY KEY(`ano`,`mano`));""")
    conn.commit()
    cursor.close()

#funcion que crea los registros para un año inicado registroGSM
def populate_table_Gsm_Registros(conn,ano):
    cursor=conn.cursor()
    leer_sql   ='''SELECT * FROM registroGSM WHERE ano=? and mano=?;'''
    insert_sql ='''INSERT INTO registroGSM (ano ,mano ,estadio ,fecha ,litros ,sul0 ,Sul1 ,sul2 ,sul3 ,sul4 ,sul5 ,can0 ,can1 ,can2 ,can3 ,can4 ,can5 ,dos0 ,dos1 ,dos2 ,dos3 ,dos4 ,dos5) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);'''
    resultado=[]
    for mano in range (16):
        registro=Obj_Gsm_Registros((ano,mano,'NULL','NULL','NULL','NULL','NULL','NULL','NULL','NULL','NULL','NULL','NULL','NULL','NULL','NULL','NULL','NULL','NULL','NULL','NULL','NULL','NULL'))
        cursor.execute(leer_sql,[ano,mano])
        if cursor.fetchone() is None:
            #insertamos el registro en la base de datos
            cursor.execute(insert_sql,registro.valor_Insert())
            conn.commit()
            resultado.append(True)
        else:
            resultado.append(False)

    return resultado

#funcion que lee los registros de la tabla registroGSM
def select_Gsm_Registros(conn,ano):
    cursor=conn.cursor()
    cursor.execute('SELECT * FROM registroGSM WHERE ano=?;',[ano,])
    conn.commit()
    resultado = cursor.fetchall()
    cursor.close()
    return resultado

#funcion que inserta / actualiza un registro para la tabla registroGSM
def insertar_Gsm_Registros(conn,registro):
    cursor=conn.cursor()
    leer_sql   ='''SELECT * FROM registroGSM WHERE ano=? and mano=?;'''
    insert_sql ='''INSERT INTO registroGSM (ano ,mano ,estadio ,fecha ,litros ,sul0 ,Sul1 ,sul2 ,sul3 ,sul4 ,sul5 ,can0 ,can1 ,can2 ,can3 ,can4 ,can5 ,dos0 ,dos1 ,dos2 ,dos3 ,dos4 ,dos5) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);'''
    update_sql ='''UPDATE registroGSM SET estadio=?,fecha=?,litros=?,sul0=?,Sul1=?,sul2=?,sul3=?,sul4=?,sul5=?,can0=?,can1=?,can2=?,can3=?,can4=?,can5=?,dos0=?,dos1=?,dos2=?,dos3=?,dos4=?,dos5=? WHERE ano=? and mano=?;'''
    cursor.execute(leer_sql,registro.clave_primaria())
    if cursor.fetchone==None:
        #insertamos el registro en la base de datos
        cursor.execute(insert_sql,registro.valor_Insert())
        resultado="registro insertado en registroGSM"
    else:
        #actualizamos el registro en la base de datos
        cursor.execute(update_sql,registro.valor_Update())
        resultado="registro actualizado en registroGSM"
    return resultado