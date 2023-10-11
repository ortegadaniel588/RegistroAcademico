from Modelos.Inscripcion import Inscripcion
from Repositorios.RepositorioInscripcion import RepositorioInscripcion


class ControladorInscripcion():
    def __init__(self):
        # Se crea una instancia del RepositorioEstudiante para interactuar con la base de datos
        self.repositorioInscripcion = RepositorioInscripcion()

    def index(self):
        # Retorna todos los estudiantes existentes en la base de datos
        return self.repositorioInscripcion.findAll()

    def create(self, infoInscripcion):
        # Crea un nuevo objeto Estudiante a partir de la información recibida
        nuevoInscripcion = Inscripcion(infoInscripcion)

        # Guarda el nuevo estudiante en la base de datos utilizando el repositorio
        return self.repositorioInscripcion.save(nuevoInscripcion)

    def show(self, id):
        # Obtiene un estudiante por su ID desde la base de datos utilizando el repositorio
        elInscripcion = Inscripcion(self.repositorioInscripcion.findById(id))

        # Retorna los atributos del estudiante como un diccionario
        return elInscripcion.__dict__

    def update(self, id, infoInscripcion):
        # Obtiene el estudiante actual por su ID desde la base de datos utilizando el repositorio
        inscripcionActual = Inscripcion(self.repositorioEstudiante.findById(id))

        # Actualiza los atributos del estudiante con la información recibida
        inscripcionActual.id = infoInscripcion["id"]
        inscripcionActual.ano = infoInscripcion["ano"]
        inscripcionActual.semestre = infoInscripcion["semestre"]
        inscripcionActual.nota_final = infoInscripcion["nota_final"]

        # Guarda los cambios del estudiante actualizado en la base de datos utilizando el repositorio
        return self.repositorioInscripcion.save(inscripcionActual)

    def delete(self, id):
        # Elimina un estudiante por su ID desde la base de datos utilizando el repositorio
        return self.repositorioInscripcion.delete(id)
