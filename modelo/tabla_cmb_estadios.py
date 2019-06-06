from modelo.Obj_Cmb_Estadios import Obj_Cmb_Estadios
# funciones de la tabla estadios


# funcion que crea la tabla estadios
def create_table_estadios(conn):
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS 'estadios' (`id`INTEGER,`estadio`TEXT,PRIMARY KEY(`id`));""")
    conn.commit()
    cursor.close()


# funcion que crea los registros para un año inicado estadios
def populate_table_estadios(conn):
    cursor = conn.cursor()
    estadios = ['Yemas Inchadas', 'Inicio Brotacion', 'Hojas Extendidas', 'Racimos Visibles', 'Inicio Floracion',
                'Mitad Floracion', 'Final Floracion', 'Tamaño Perdigon', 'Tamaño Guisante', 'Cierre Racimo',
                'Inicio Envero', 'Final Envero', 'Inicio Madurcion', 'Final Maduracion', 'Pos Venvimia',
                'Ultima Mano Sulfato', 'Repeticion por Lluvia', 'Repeticon por Mildeo']
    leer_sql = '''SELECT * FROM estadios WHERE id=?;'''
    insert_sql = '''INSERT INTO estadios (id ,estadio) VALUES (?,?);'''
    resultado = []
    for estadio in estadios:
        registro = Obj_Cmb_Estadios((estadios.index(estadio), estadios))
        cursor.execute(leer_sql, registro.clave_primaria())
        if cursor.fetchone() is None:
            # insertamos el registro en la base de datos
            cursor.execute(insert_sql, registro.valor_Insert())
            conn.commit()
            resultado.append(True)
        else:
            resultado.append(False)


# funcion que lee los registros de la tabla registroGSM
def select_all_estadios(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM estadios ;')
    conn.commit()
    resultado = cursor.fetchall()
    cursor.close()
    return resultado
