from model import Model
from view import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def run(self):
        self.view.run()

    def login(self):
        username = self.view.username_entry.get()
        password = self.view.password_entry.get()
        if username == "diana" and password == "123":
            self.view.pantalla()
        else:
            self.view.show_message("Error", "Usuario o contraseña incorrectos")

    def logout(self):
        self.view.entrar()

    def agregar_paciente(self):
        nombre = self.view.prompt("Agregar Paciente", "Nombre:")
        apellido = self.view.prompt("Agregar Paciente", "Apellido:")
        edad = self.view.prompt("Agregar Paciente", "Edad:")
        identificacion = self.view.prompt("Agregar Paciente", "Identificación:")
        try:
            self.model.agregar_paciente(nombre, apellido, edad, identificacion)
            self.view.show_message("Éxito", "Paciente agregado exitosamente")
        except ValueError as e:
            self.view.show_message("Error", str(e))

    def buscar_paciente(self):
        buspa = self.view.prompt("Buscar Paciente", "Ingrese las primeras letras del nombre:")
        resultados = self.model.buscar_pacientes(buspa)
        if resultados:
            self.view.mostrar_resultados_busqueda(resultados)
        else:
            self.view.show_message("Resultados", "No se encontraron pacientes")

    def eliminar_paciente(self, identificacion):
        self.model.eliminar_paciente(identificacion)
        self.view.show_message("Éxito", "Paciente eliminado exitosamente")
        self.view.pantalla()
