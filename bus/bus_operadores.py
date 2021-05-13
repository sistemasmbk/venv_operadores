from dao.dao_operadores import Dao_Operadores

class Bus:
    
    def __init__(self):
        print("Se creo el objeto bus")
    
    def obtener_operadores_todos(self):
        """Regresa una lista de objetos"""
        d = Dao_Operadores()
        try:
            d.conectar()
            return d.select_operadores_todos()
        except Exception as e:
            return "Error: No se pudo obtener la información." + e
        finally:
            d.desconectar()
            
    def obtener_operadores_por_clave(self,clave):
        """Regresa un solo objeto"""
        d = Dao_Operadores()
        try:
            d.conectar()
            return d.select_operadores_por_clave(clave)
        except Exception as e:
            return "Error: No se pudo obtener la información." + e
        finally:
            d.desconectar()
    
    def crear_operadores(self,clave,nombre):
        """Crea Registro de Operador"""
        d = Dao_Operadores()
        try:
            d.conectar()
            operador_a_buscar = d.select_operadores_por_clave(clave)
            if len(operador_a_buscar.clave)>0:
                return "Error: Ya existe Operador."
            else:
                operadores = d.insert_operadores(clave,nombre)
                if operadores == 1:
                    return "Clave: " + clave +" Nombre: " + nombre + " Datos insertados correctamente."
                else:
                    raise Exception
        except Exception as e:
            return "Error: No se pudo insertar la información."
        finally:
            d.desconectar()
    
    def modificar_nombre_operador(self,clave,nombre):
        d = Dao_Operadores()
        try:
            d.conectar()
            operador_a_buscar = d.select_operadores_por_clave(clave)
            if len(operador_a_buscar.clave)<1:
                return "Error: No existe el operador."
            else:
                operadores = d.update_operadores_nombre(clave,nombre)
                if operadores == 1:
                    return "Clave: " + clave +" se actualizó con el nombre: " + nombre + " correctamente."
                else:
                    raise Exception
        except Exception as e:
            return "Error: No se pudo actualizar la información." + e
        finally:
            d.desconectar()
            
    def eliminar_operadores(self,clave):
        d = Dao_Operadores()
        try:
            d.conectar()
            operadores = d.delete_operadores_clave(clave)
            if operadores == 1:
                return "Operador clave: " + clave + " se eliminó correctamente."
            else:
                raise Exception
        except Exception as e:
            return "Error: No se pudo actualizar la información." + e
        finally:
            d.desconectar()
    
#casos de prueba

