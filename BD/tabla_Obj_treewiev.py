from app_2.DB.modelo.Obj_treewiev import Obj_Treewiev_Mano
class tabla_gsm_vista():
    # funcion que crea la tabla registroGSM
    def create_table_Treewiev_Mano(conn):
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS`treewiev`  (`ID` INTEGER, `Ano`TEXT,`sulfato` TEXT, `M0` TEXT, `M1` TEXT, `M2` TEXT, `M3` TEXT, `M4` TEXT , `M5` TEXT , `M6` TEXT , `M7` TEXT , `M8` TEXT , `M9` TEXT , `M10` TEXT, `M11` TEXT, `M12` TEXT, `M13` TEXT, `M14` TEXT, `M15` TEXT, PRIMARY KEY(`ID`);""")
        conn.commit()
        cursor.close()

