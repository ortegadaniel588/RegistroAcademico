from Modelos.Materia import Materia
from Repositorios.RepositorioMateria import RepositorioMateria


class ControladorMateria():
    def __init__(self):
        # Se crea una instancia del RepositorioEstudiante para interactuar con la base de datos
        self.repositorioMateria = RepositorioMateria()

    def index(self):
        # Retorna todos los estudiantes existentes en la base de datos
        return self.repositorioMateria.findAll()

    def create(self, infoMateria):
        # Crea un nuevo objeto Estudiante a partir de la información recibida
        nuevoMateria = Materia(infoMateria)

        # Guarda el nuevo estudiante en la base de datos utilizando el repositorio
        return self.repositorioMateria.save(nuevoMateria)

    def show(self, id):
        # Obtiene un estudiante por su ID desde la base de datos utilizando el repositorio
        elMateria = Materia(self.repositorioEstudiante.findById(id))

        # Retorna los atributos del estudiante como un diccionario
        return elMateria.__dict__

    def update(self, id, infoMateria):
        # Obtiene el estudiante actual por su ID desde la base de datos utilizando el repositorio
        materiaActual = Materia(self.repositorioMateria.findById(id))

        # Actualiza los atributos del estudiante con la información recibida
        materiaActual.id = infoMateria["id"]
        materiaActual.nombre = infoMateria["nombre"]
        materiaActual.creditos = infoMateria["creditos"]

        # Guarda los cambios del estudiante actualizado en la base de datos utilizando el repositorio
        return self.repositorioMateria.save(materiaActual)

    def delete(self, id):
        # Elimina un estudiante por su ID desde la base de datos utilizando el repositorio
        return self.repositorioMateria.delete(id)
