from modelo.Obj_Cmb_Sulfatos import Obj_Cmb_Sulfatos


# funciones de la tabla sulfatos


# funcion que crea la tabla sulfatos
def create_table_sulfatos(conn):
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS 'sulfatos' (`id`INTEGER,`sulfatos`TEXT,PRIMARY KEY(`id`));""")
    conn.commit()
    cursor.close()


# funcion que crea los registros para un año inicado  sulfatos
def populate_table_sulfatos(conn):
    cursor = conn.cursor()
    sulfatos = ['Branda', 'Cupra', 'Laitri', 'Greetnal', 'Dynali', 'Lainzufre WG', 'Festival', 'Estuder Plus Pro',
                'Caldo Lainco', 'Micene mancoceb(80%)', 'Bayfolan Potasio', 'Epsonita', 'Switch']
    leer_sql = '''SELECT * FROM sulfatos WHERE id=?;'''
    insert_sql = '''INSERT INTO  sulfatos (id ,sulfatos) VALUES (?,?);'''
    resultado = []
    for sulfato in sulfatos:
        registro = Obj_Cmb_Sulfatos((sulfatos.index(sulfato), sulfato))
        cursor.execute(leer_sql, registro.clave_primaria())
        if cursor.fetchone() is None:
            # insertamos el registro en la base de datos
            cursor.execute(insert_sql, registro.valor_Insert())
            conn.commit()
            resultado.append(True)
        else:
            resultado.append(False)

    return resultado


# funcion que lee los registros de la tabla sulfatos
def select_registro_sulfatos(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM sulfatos ;')
    conn.commit()
    resultado = cursor.fetchall()
    cursor.close()
    return resultado
