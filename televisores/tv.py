
class TV:
    _numTV = 0
    def __new__(cls, *args, **kwargs):
        cls._numTV += 1
        return super().__new__(cls)

    def __init__(self, marca, estado: bool):
        self._marca = marca
        self._estado = estado
        self._canal = 1
        self._precio = 500
        self._volumen = 1
        self._control = None

    def getEstado(self) -> bool:
        return self._estado

    def getMarca(self):
        return self._marca
    def setMarca(self, marca):
        self._marca = marca
    def getCanal(self) -> int:
        return self._canal
    def setCanal(self, canal:int):
        if self._estado and 1 <= canal <= 120:
            self._canal = canal
    def getPrecio(self) -> int:
        return self._precio
    def setPrecio(self, precio:int):
        self._precio = precio
    def getVolumen(self) -> int:
        return self._volumen
    def setVolumen(self, volumen: int):
        if self._estado and 0 <= volumen <= 7:
            self._volumen = volumen
    def getControl(self):
        return self._control
    def setControl(self, control):
        self._control = control

    def turnOn(self):
        self._estado = True
    def turnOff(self):
        self._estado = False

    def canalUp(self):
        self.setCanal(self._canal + 1)
    def canalDown(self):
        self.setCanal(self._canal - 1)
    def volumenUp(self):
        self.setVolumen(self._volumen + 1)
    def volumenDown(self):
        self.setVolumen(self._volumen - 1)

    @staticmethod
    def getNumTV():
        return TV._numTV

    @staticmethod
    def setNumTV(numTV:int):
        TV._numTV = numTV