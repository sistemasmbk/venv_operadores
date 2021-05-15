from dao.dao_operadores import Dao_Operadores
from vo.respuesta import Respuesta
from vo.accion_operador import Accion_operador

class Bus:
    
    def __init__(self):
        print("Se creo el objeto bus")

    def serializar(self,objetos):
        json_resultado = []
        for objeto in objetos:
            if type(objeto) is str:
                json_resultado.append({"Resultado":objeto})
            else:
                objeto_dicc = {}
                for atributo in dir(objeto):
                    if not atributo.startswith("__"):
                        objeto_dicc[atributo] = getattr(objeto,atributo)
                if len(objeto_dicc) > 0:
                    json_resultado.append(objeto_dicc)
        return json_resultado

    def serializar_simple(self,objeto):
        if type(objeto) is str:
            return {"Resultado":objeto}
        else:
            objeto_dicc = {}
            for atributo in dir(objeto):
                if not atributo.startswith("__"):
                    objeto_dicc[atributo] = getattr(objeto,atributo)
            return objeto_dicc

    def obtener_operadores_todos(self):
        """Regresa una lista de objetos"""
        d = Dao_Operadores()
        try:
            d.conectar()
            operador = d.select_operadores_todos()
            return self.serializar(operador)
        except Exception as e:
            return [f"Error: No se pudo obtener la información. {e}",]            
        finally:
            d.desconectar()
            
    def obtener_operadores_por_clave(self,clave):
        """Regresa un solo objeto"""
        d = Dao_Operadores()
        try:
            d.conectar()
            operador = d.select_operadores_por_clave(clave)
            return self.serializar_simple(operador)
        except Exception as e:
            return [f"Error: No se pudo obtener la información. {e}",]            
        finally:
            d.desconectar()
    
    def crear_operadores(self,clave,nombre):
        """Crea Registro de Operador"""
        d = Dao_Operadores()
        try:
            d.conectar()
            operador_a_buscar = d.select_operadores_por_clave(clave)
            if len(operador_a_buscar.clave)>0:
                res = Respuesta()
                res.codigo = False
                res.mensaje = "Ya existe Operador. Accion no realizada"
                return self.serializar_simple(res)
            else:
                operadores = d.insert_operadores(clave,nombre)
                if operadores == 1:
                    res = Respuesta()
                    res.codigo = True
                    res.mensaje = "Clave: " + clave +" Nombre: " + nombre + " Datos insertados correctamente."
                    return self.serializar_simple(res)
                    # return "Clave: " + clave +" Nombre: " + nombre + " Datos insertados correctamente."
                else:
                    raise Exception
        except Exception as e:
            res = Respuesta()
            res.codigo = False
            res.mensaje = f"No se pudo insertar la información. {e}"
            return self.serializar_simple(res)
        finally:
            d.desconectar()
    
    def modificar_nombre_operador(self,clave,nombre):
        d = Dao_Operadores()
        try:
            d.conectar()
            operador_a_buscar = d.select_operadores_por_clave(clave)
            if len(operador_a_buscar.clave)<1:
                res = Respuesta()
                res.codigo = False
                res.mensaje = "No Existe el operador"
                return self.serializar_simple(res)
            else:
                operadores = d.update_operadores_nombre(clave,nombre)
                if operadores == 1:
                    res = Respuesta()
                    res.codigo = True
                    res.mensaje = "Clave: " + clave +" se actualizó con el nombre: " + nombre + " correctamente."
                    return self.serializar_simple(res)
                else:
                    raise Exception
        except Exception as e:
            res = Respuesta()
            res.codigo = False
            res.mensaje = "No se pudo actualizar la información."
            return self.serializar_simple(res)
        finally:
            d.desconectar()
            
    def eliminar_operadores(self,accion_operador):
        d = Dao_Operadores()
        try:
            if accion_operador.operador.clave == "001":
                res = Respuesta()
                res.codigo = False
                res.mensaje = "Operador clave: " + accion_operador.operador.clave + " no puede ser eliminado. usario: " + accion_operador.clave_usuario + " Nombre Usuario: " + accion_operador.nombre_usuario
                return self.serializar_simple(res)
            else:
                d.conectar()
                operadores = d.delete_operadores_clave(accion_operador.operador.clave)
                if operadores == 1:
                    res = Respuesta()
                    res.codigo = True
                    res.mensaje = "Operador clave: " + accion_operador.operador.clave + " se eliminó correctamente. usario: " + accion_operador.clave_usuario + " Nombre Usuario: " + accion_operador.nombre_usuario
                    # Bitacora
                    d.insert_bitacora(accion_operador.clave_usuario, accion_operador.nombre_usuario,"Eliminar")
                    return self.serializar_simple(res)
                else:
                    raise Exception
        except Exception as e:
            res = Respuesta()
            res.codigo = False
            res.mensaje = "No se encontro operador"
            return self.serializar_simple(res)
        finally:
            d.desconectar()
    
#casos de prueba

