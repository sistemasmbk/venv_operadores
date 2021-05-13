import psycopg2
import psycopg2.extras

class Conexion:
    
    __user = "postgress"
    __password = "P0stgr3s**"
    __host="cursos.cdvqfedytrah.us-east-1.rds.amazonaws.com"
    __port = "5432"
    __database="cursos"
    conexion = None
    cursor = None
    
    def __init__(self):
        pass
    
    def conectar(self):
        try:
            if self.conexion == None :
                self.conexion = psycopg2.connect(
                    user = self.__user,
                    password = self.__password,
                    host = self.__host,
                    port = self.__port,
                    database = self.__database
                )
                self.cursor = self.conexion.cursor(cursor_factory=psycopg2.extras.DictCursor)
        except Exception as e:
            print("Error: Error de conexion: ",e)
        else:
            print("¡Conexión establecida!")
    
    def desconectar(self):
        try:
            if self.conexion != None and self.cursor != None :
                self.cursor.close()
                self.conexion.close()
                self.conexion = None
                self.cursor = None
            elif self.conexion != None and self.cursor == None:
                self.conexion.close()
                self.conexion = None
            elif self.conexion == None and self.cursor != None:
                self.cursor.close()
                self.cursor = None
        except Exception as e:
            print("Error: Error de desconexion: ",e)
        else:
            print("¡Conexión cerrada!")    
            
    def hay_conexion(self):
        print("Hay conexion") if self.conexion != None else print("No hay conexion")
        print("Hay cursor") if self.cursor != None else print("No hay cursor")
    
#Casos de prueba 

if __name__ == "__main__":
    bd = Conexion()
    bd.conectar()
    bd.hay_conexion()
    bd.desconectar()
    bd.hay_conexion()
    
    