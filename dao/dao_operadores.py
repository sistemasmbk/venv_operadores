from bd.conexion import Conexion
from vo.operadores import Operadores
from dao.excepciones import Error_Logico

class Dao_Operadores(Conexion):
    
    __seleccionar_todo = "SELECT * FROM mabarak.operadores"
    __seleccionar_clave = "SELECT * FROM mabarak.operadores WHERE clave = %s"
    __insertar = "INSERT INTO mabarak.operadores(clave,nombre) VALUES (%s,%s)"
    __actualizar_nombre = "UPDATE mabarak.operadores SET nombre = %s WHERE clave = %s"
    __eliminar = "DELETE FROM mabarak.operadores WHERE clave = %s"
    
    def __init__(self):
        print("Se creo el objeto DAO")
    
    def select_operadores_todos(self):
        try:
            self.cursor.execute(self.__seleccionar_todo)
            registros = self.cursor.fetchall()
            operadores = []
            for registro in registros:
                operadores.append(Operadores(registro["clave"],registro["nombre"]))
            return operadores
        except Exception as e:
            print("Error: No se pudo obtener la información.",e) 
        
            
    def select_operadores_por_clave(self,clave):
        try:
            argumento = (clave,)
            self.cursor.execute(self.__seleccionar_clave,argumento)
            registro = self.cursor.fetchone()
            if registro != None:
                return Operadores(registro["clave"],registro["nombre"])
            else:
                raise Error_Logico
        except Error_Logico as el:
            print("Error: No tiene información",el)
            return Operadores("","")
        except Exception as e:
            print("Error: No se pudo obtener la información.",e)
    
    def insert_operadores(self,clave,nombre):
        try:
            argumento = (clave,nombre)
            self.cursor.execute(self.__insertar,argumento)
            self.conexion.commit()
            return self.cursor.rowcount
        except Exception as e:
            print("Error: No se pudo insertar la información.",e)  
            return 0
    
    def update_operadores_nombre(self,clave,nombre):
        try:
            argumento = (nombre,clave)
            self.cursor.execute(self.__actualizar_nombre,argumento)
            self.conexion.commit()
            return self.cursor.rowcount
        except Exception as e:
            print("Error: No se pudo actualizar la información.",e) 
            return 0 
    
    def delete_operadores_clave(self,clave):
        try:
            argumento = (clave,)
            self.cursor.execute(self.__eliminar,argumento)
            self.conexion.commit()
            return self.cursor.rowcount
        except Exception as e:
            print("Error: No se pudo eliminar la información.",e) 
            return 0 

    def insert_bitacora(self, clave_usuario, nombre_usuario, accion):
        print("Bitacora Registrada accion: " + accion + " realizado por : " + clave_usuario + "-" + nombre_usuario)