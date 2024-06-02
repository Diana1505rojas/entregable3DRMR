import json
import os

class Model:
    def __init__(self):
        self.data_file = 'data.json'
        self.pacientes = self.cargar()

    def cargar(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                return json.load(file)
        return []

    def guardar(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.pacientes, file, indent=4)

    def agregar_paciente(self, nombre, apellido, edad, identificacion):
        if any(p['identificacion'] == identificacion for p in self.pacientes):
            raise ValueError("Identificación ya existente")
        nuevo_paciente = {
            'nombre': nombre,
            'apellido': apellido,
            'edad': edad,
            'identificacion': identificacion
        }
        self.pacientes.append(nuevo_paciente)
        self.guardar()

    def eliminar_paciente(self, identificacion):
        self.pacientes = [p for p in self.pacientes if p['identificacion'] != identificacion]
        self.guardar()

    def buscar_pacientes(self, buspa):
        buspa = buspa.lower()
        return [p for p in self.pacientes if p['nombre'].lower().startswith(buspa)]
