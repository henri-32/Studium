import math as m


# Base Class 
class GameObject (): 
    def __init__ (self, x: int, y: int, movable: bool): 
        self._x_pos = x
        self._y_pos = y 
        self._movable = movable

        # Durch Speed und Heading lässt sich Bewegung im  2D
        # Raum darstellen diese werden stets mit 0 initialisiert
        self._speed = 0 
        
        # Heading ist hier die Ausrichtung des Objekts als Winkel in Grad
        # im Verhältnis zur Ausrichtung der 2D Spielwelt 
        self._heading = 0 

    def set_velocity (self, speed: int, heading: int) -> None: 
        """Ändert die Velocitydaten für self, welche als State in der Instanz
        gehalten werden"""
        if speed < 0: 
            raise ValueError ("speed may not be negative")
        self._speed = speed
        # Hier wäre auch eine Normalisierung des Inputs durch Modulus denkbar.
        # Durch den strikten Check soll logisch inkorrekte Nutzung der API 
        # auffallen 
        if heading < 0 or heading >= 360: 
            raise ValueError ("heading must be 0 to 359")
        self._heading = heading

    def update(self) -> None:
        """Aktualisiert alle states""" 
        if self._movable:
            self._apply_velocity()

    # readonly getter
    @property
    def x(self) -> int:
        return self._x_pos

    @property
    def y(self) -> int:
        return self._y_pos

    @property
    def can_move(self) -> bool:
        return self._movable

    def _apply_velocity(self):
        """Wendet die Velocitydaten auf self an""" 
        # Umrechnung von heading (Grad) in kartesische Bewegung 
        # mit math module
        self._x_pos += int(self._speed * m.cos(m.radians(self._heading)))
        self._y_pos += int(self._speed * m.sin(m.radians(self._heading)))


class Rock (GameObject):
    def __init__ (self, x: int, y: int, width: int, height: int):
        # Rocks sind generell nicht movable, deswegen mit False initialisiert  
        super().__init__(x, y, False) 
        self.width = width 
        self.height= height 

    # gibt ein set von Positionen zurück, auf welchen sich das Objekt 
    # befindet 
    @property
    def occupied_space (self) -> set[tuple[int, int]]:
        space = set()
        x_max = self.x + self.width
        y_max = self.y + self.height

        for i in range(int(self.x), int(x_max)):
            for j in range(int(self.y), int(y_max)):
                space.add((i, j))

        return space






                







