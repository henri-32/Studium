import math as m
from enum import Enum


# Base Class 
class GameObject (): 
    def __init__ (self, x: int, y: int, movable: bool, width=10, height = 10,
        **kwargs): 

            self._x_pos = x
            self._y_pos = y 
            self._width = width
            self._height = height

             # Flag für Beweglichkeit des Objektes. Bewusst keine Subklasse 
             # MovableGameObject, damit die Fähigkeit Beweglichkeit im Game 
             # dynamisch modelliert werden kann 
            self._movable = movable

            # Durch Speed und Heading lässt sich Bewegung im  2D
            # Raum darstellen diese werden stets mit 0 initialisiert
            self._speed = 0 
        
            # Heading ist hier die Ausrichtung des Objekts als Winkel in Grad
            # im Verhältnis zur Ausrichtung der 2D Spielwelt 
            self._heading = 0

            # Ermöglicht kooperative Vererbung
            super().__init__(**kwargs)

    # ==================================================== 
    # Public API 
    # ====================================================
    def set_velocity (self, speed: int, heading_deg: int) -> None: 
        """Ändert die Velocitydaten für self, welche als State in der Instanz
        gehalten werden"""
        if speed < 0: 
            raise ValueError ("speed may not be negative")
        self._speed = speed
        # Hier wäre auch eine Normalisierung des Inputs durch Modulus denkbar.
        # Durch den strikten Check soll logisch inkorrekte Nutzung der API 
        # auffallen 
        if heading_deg < 0 or heading_deg >= 360: 
            raise ValueError ("heading must be 0 to 359")
        self._heading = heading_deg

    def update(self) -> None:
        """Aktualisiert alle states""" 
        if self._movable:
            self._apply_velocity()

    # Readonly getter
    @property
    def x(self) -> int:
        return self._x_pos

    @property
    def y(self) -> int:
        return self._y_pos

    @property
    def can_move(self) -> bool:
        return self._movable

    # Computed view
    # Gibt ein set von Positionen zurück, auf welchen sich das Objekt 
    # befindet 
    @property
    def occupied_space (self) -> set[tuple[int, int]]:
        space = set()
        x_max = self.x + self._width
        y_max = self.y + self._height

        for i in range(int(self.x), int(x_max)):
            for j in range(int(self.y), int(y_max)):
                space.add((i, j))

        return space

    #=========================================================
    # Helper functions
    #=========================================================
    def _apply_velocity(self):
        """Wendet die Velocitydaten auf self an""" 
        # Umrechnung von heading (Grad) in kartesische Bewegung 
        # mit math module
        self._x_pos += int(self._speed * m.cos(m.radians(self._heading)))
        self._y_pos += int(self._speed * m.sin(m.radians(self._heading)))

# Base Class 
class DamageModel():
    class DamageState(Enum):
        OK = 0
        DAMAGED = 1
        UNMANEUVERABLE = 2
        DESTROYED = 3
        
    def __init__ (self, max_health: int, **kwargs):
        self.max_health = max_health
        self.health = max_health
        self.damage_state = self.DamageState.OK

        # Auch hier kooperative Vererbung möglich machen
        super().__init__(**kwargs)
        
    def damage (self, damage: int) -> None:
        self.health = max(0, self.health - damage)

    def update(self) -> None:
        relative_damage = (self.health / self.max_health) * 100
        
        if relative_damage > 50:
            self.damage_state = self.DamageState.OK

        elif relative_damage > 25: 
            self.damage_state = self.DamageState.DAMAGED

        elif relative_damage > 0:
            self.damage_state = self.DamageState.UNMANEUVERABLE

        else:
            self.damage_state = self.DamageState.DESTROYED
            

class Rock (GameObject):
    def __init__ (self, x: int, y: int, width: int, height: int):
        # Rocks sind generell nicht movable, deswegen mit False initialisiert
        # ohne setter method
        super().__init__(x, y, False, width, height) 


class SandBank (GameObject):
    def __init__ (self, x: int, y: int, width: int, height: int):
        # SandBanks ebenfalls nicht moveable
        super().__init__(x, y, False, width, height)


class Ship (GameObject, DamageModel):
    def __init__ (self, x: int, y: int, width: int, height: int,
        max_health: int):
            # Ships sind grundsätzlich movable
            super().__init__(
                x=x,
                y=y,
                movable=True,
                width=width,
                height=height,
                max_health=max_health
                )

    # Ships haben keine veränderbare Geschwindigkeit, bei ihnen ist diese
    # Teil der Klasseneigenschaft und wird durch init methoden von Subklassen 
    # in Kombination mit Schadensmodellen modelliert
    def set_heading (self, heading: int) -> None:
        super().set_velocity(self._speed, heading)

    # Direkten Zugriff auf die physischen Eigenschaften wird verhindert, um
    # SetHeading API zu nutzen 
    def set_velocity(self, speed: int, heading_deg: int) -> None:
        raise RuntimeError("Ships velocity is controlled via set course") 

                







