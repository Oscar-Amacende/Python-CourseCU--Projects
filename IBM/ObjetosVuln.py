class vulnerabilidad:
    def __init__ (self, nombre, severidad, descripcion):
        self.nombre = nombre
        self.severidad = severidad
        self.descripcion = descripcion

    def mostrarinfo(self):
        print(self.nombre)
        print(self.severidad)
        print(self.descripcion)

    def recomendar_acciones(self):
        if self.severidad == "Critica":
            recomendacion = "Aplicar parches de seguridad inmediatamente y revisar sistemas afectados."
            print(f"Accion recomendada: {recomendacion}")
        elif self.severidad == "Alta":
            recomendacion = "Realizar una auditoría de seguridad y aplicar medidas correctivas lo antes posible."
            print(f"Accion recomendada: {recomendacion}")
        elif self.severidad == "Media":
            recomendacion = "Monitorizar la actividad del sistema y planificar la aplicación de parches."
            print(f"Accion recomendada: {recomendacion}")
        elif self.severidad == "Baja":
            recomendacion = "Mantener bajo observación y revisar en el próximo ciclo de actualización."
            print(f"Accion recomendada: {recomendacion}")

obj1=vulnerabilidad("SQL Injection", "Alta", "Permite la ejecución de consultas SQL no autorizadas.")
obj2=vulnerabilidad("XSS", "Media", "Permite la ejecución de scripts en el navegador del usuario.")
obj3=vulnerabilidad("Desbordamiento de Buffer", "Crítica", "Permite la ejecución arbitraria de código.")

registro_vulnerabilidades=[obj1,obj2,obj3]
#Sin print, porque el objeto ya lo llama
#obj1.mostrarinfo()


print(f"Nombre: {obj1.nombre}")
print(f"Severidad: {obj1.severidad}")
print(f"Descripcion: {obj1.descripcion}")
obj1.recomendar_acciones()
#print(obj1.recomendar_acciones(self, recomendacion))
