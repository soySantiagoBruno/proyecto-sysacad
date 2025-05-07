from app.models import Facultad


class FacultadService:
    
    @staticmethod
    def crear_facultad(facultad: Facultad):
        return facultad