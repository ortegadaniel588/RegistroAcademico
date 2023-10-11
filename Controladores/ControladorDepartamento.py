from Modelos.Departamento import Departamento
from Repositorios.RepositorioDepartamento import RepositorioDepartamento


class ControladorDepartamento():
    def __init__(self):
        # Se crea una instancia del RepositorioEstudiante para interactuar con la base de datos
        self.repositorioEstudiante = RepositorioDepartamento()

    def index(self):
        # Retorna todos los estudiantes existentes en la base de datos
        return self.repositorioDepartamento.findAll()

    def create(self, infoDepartamento):
        # Crea un nuevo objeto Estudiante a partir de la información recibida
        nuevoDepartamento = Departamento(infoDepartamento)

        # Guarda el nuevo estudiante en la base de datos utilizando el repositorio
        return self.repositorioDepartamento.save(nuevoDepartamento)

    def show(self, id):
        # Obtiene un estudiante por su ID desde la base de datos utilizando el repositorio
        elDepartamento = Departamento(self.repositorioDepartamento.findById(id))

        # Retorna los atributos del estudiante como un diccionario
        return elDepartamento.__dict__

    def update(self, id, infoDepartamento):
        # Obtiene el estudiante actual por su ID desde la base de datos utilizando el repositorio
        departamentoActual = Departamento(self.repositorioDepartamento.findById(id))

        # Actualiza los atributos del estudiante con la información recibida
        departamentoActual.id = infoDepartamento["id"]
        departamentoActual.nombre = infoDepartamento["nombre"]

        # Guarda los cambios del estudiante actualizado en la base de datos utilizando el repositorio
        return self.repositorioDepartamento.save(departamentoActual)

    def delete(self, id):
        # Elimina un estudiante por su ID desde la base de datos utilizando el repositorio
        return self.repositorioDepartamento.delete(id)
