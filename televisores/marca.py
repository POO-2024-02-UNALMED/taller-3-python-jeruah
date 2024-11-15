class Marca:
    # _nombre: str
    def __init__(self, nombre) -> None:
        self._nombre = nombre

    def getNombre(self) -> str:
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre