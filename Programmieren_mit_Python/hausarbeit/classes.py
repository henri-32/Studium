import math as m
from enum import Enum
from abc import abstractmethod


# Base Class
class GameObject:
    def __init__(
        self,
        ID: int,
        x: int,
        y: int,
        movable: bool,
        width=10,
        height=10,
        **kwargs,
    ):
        self._ID = ID
        self._x_pos = x
        self._y_pos = y
        self._width = width
        self._height = height

        # Flag um Objekte vom System aus löschen zu können
        self._existing = True

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
    def set_velocity(self, speed: int, heading_deg: int) -> None:
        """Ändert die Velocitydaten für self, welche als State in der Instanz
        gehalten werden"""
        if speed < 0:
            raise ValueError("speed may not be negative")
        self._speed = speed
        # Hier wäre auch eine Normalisierung des Inputs durch Modulus denkbar.
        # Durch den strikten Check soll logisch inkorrekte Nutzung der API
        # auffallen
        if heading_deg < 0 or heading_deg >= 360:
            raise ValueError("heading must be 0 to 359")

    @abstractmethod
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
    def occupied_space(self) -> set[tuple[int, int]]:
        space = set()
        x_max = self.x + self._width
        y_max = self.y + self._height

        for i in range(int(self.x), int(x_max)):
            for j in range(int(self.y), int(y_max)):
                space.add((i, j))

        return space

    # =========================================================
    # Helper functions
    # =========================================================
    def _apply_velocity(self):
        """Wendet die Velocitydaten auf self an"""
        # Umrechnung von heading (Grad) in kartesische Bewegung
        self._x_pos += int(self._speed * m.cos(m.radians(self._heading)))
        self._y_pos += int(self._speed * m.sin(m.radians(self._heading)))


# Base Class
class DamageModel:
    class DamageState(Enum):
        OK = 0
        DAMAGED = 1
        UNMANEUVERABLE = 2
        DESTROYED = 3

    def __init__(self, max_health: int, **kwargs):
        self.max_health = max_health
        self.health = max_health
        self.damage_state = self.DamageState.OK

        # Auch hier kooperative Vererbung möglich machen
        super().__init__(**kwargs)

    def damage(self, damage: int) -> None:
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

    @abstractmethod
    def check_for_collision(self):
        pass


class CollisionModel:
    # Braucht bei der Instanzierung der liste aller Game Objects
    def __init__(self, objects_list: list):
        self._objects_list = objects_list
        # Liste in welche Positionen (mit occupied Space) aller GameObjects
        # hält
        self._positions_list = []

    def update(self):
        """Aktualisiert die Positionen aller Gameobjects"""
        # Es werden immer nur die aktuellen Positionen verglichen
        self._positions_list.clear()
        for obj in self._objects_list:
            self._positions_list.append(obj.occupied_space)

    # Bewusst keine Typnotationen, da Rückgabe und object_to_check
    # je nach Caller und Path unterschiedlich sind
    def check_for_collision(self, object_to_check):
        """Ermöglicht Prüfung, ob die anfragende Instanz mit etwas
        zusammengestoßen ist. Wenn ja wird der Typ des Kollisionsobjekts
        zurückgegeben"""
        # In dieser Liste werden alle Koordinatenpaare, welches das anfragende
        # Objekt besetzt gehalten
        position_check_list = []
        for i in object_to_check.occupied_space:
            position_check_list.append(i)
        # Für jedes GameObject
        for obj in self._objects_list:
            # Wird jedes Koordinatenpaar mit allen Koordinaten Paaren des
            # Callers verglichen
            if obj is object_to_check:
                continue

            for i in obj.occupied_space:
                if i in position_check_list:
                    return obj


class Rock(GameObject):
    def __init__(self, ID: int, x: int, y: int, width: int, height: int):
        # Rocks sind statische Objekte, die sich nicht bewegen 
        super().__init__(ID, x, y, False, width, height)


class SandBank(GameObject):
    def __init__(self, ID: int, x: int, y: int, width: int, height: int):
        # Wie Rocks 
        super().__init__(ID, x, y, False, width, height)


class CannonBall(GameObject):
    def __init__(
        self,
        ID: int,
        x: int,
        y: int,
        collision_model,
        objects_list,
    ):
        super().__init__(ID=ID, x=x, y=y, movable=True)
        objects_list.append(self)
        self._collision_model = collision_model

    def check_for_collision(self):
        collision_object = self._collision_model.check_for_collision(self)
        if collision_object is not None:
            self._is_alive = False


class Cannon:
    def __init__(self, capacity, collision_model, objects_list):
        self.capacity = capacity
        self.collision_model = collision_model
        self.objects_list = objects_list

    def shoot(self, x, y, heading):
        aim = heading - 90
        shot = CannonBall(
            ID=23,
            x=x,
            y=y,
            collision_model=self.collision_model,
            objects_list=self.objects_list,
        )

        shot.set_velocity(20, aim)


class Fortress(GameObject, DamageModel):
    def __init__(
        self,
        ID: int,
        x: int,
        y: int,
        width: int,
        height: int,
        max_health: int,
        collision_model,
        game_objects,
    ):
        # Fortress ebefalls nicht movable
        super().__init__(
            ID=ID,
            x=x,
            y=y,
            movable=False,
            width=width,
            height=height,
            max_health=max_health,
        )
        self.collision_model = collision_model
        self._cannon = Cannon(
            capacity=500,
            collision_model=collision_model,
            objects_list=game_objects,
        )

    def update(self):
        super().update()
        DamageModel.update(self)
        collision_object = self.collision_model.check_for_collision(self)
        if isinstance(collision_object, CannonBall):
            self.damage(50)

    def shoot(self):
        self._cannon.shoot(self.x, self.y, 0)
        self._cannon.shoot(self.x, self.y, 90)
        self._cannon.shoot(self.x, self.y, 180)
        self._cannon.shoot(self.x, self.y, 270)


class Ship(GameObject, DamageModel):
    def __init__(
        self,
        ID: int,
        x: int,
        y: int,
        width: int,
        height: int,
        max_health: int,
        cannon_capacity: int,
        collision_model,
        game_objects,
    ):
        # Ships sind grundsätzlich movable
        super().__init__(
            ID=ID,
            x=x,
            y=y,
            movable=True,
            width=width,
            height=height,
            max_health=max_health,
        )

        self._speed = 5

        self._collision_model = collision_model

        self._cannon = Cannon(
            capacity=cannon_capacity,
            collision_model=collision_model,
            objects_list=game_objects,
        )

    # Ships haben keine veränderbare Geschwindigkeit, bei ihnen ist diese
    # Teil der Klasseneigenschaft und wird durch init methoden von Subklassen
    # in Kombination mit Schadensmodellen modelliert
    def set_heading(self, heading: int) -> None:
        super().set_velocity(self._speed, heading)

    # Direkten Zugriff auf die API der BaseClass wird verhindert, um
    # SetHeading API zu nutzen
    def set_velocity(self, speed: int, heading_deg: int) -> None:
        raise RuntimeError("Ships velocity is controlled via set course")

    def check_for_collision(self):
        collision_object = self._collision_model.check_for_collision(self)
        if collision_object is None:
            return
        elif isinstance(collision_object, Ship):
            self.damage(50)
        elif isinstance(collision_object, Rock):
            self.damage(1000)
        elif isinstance(collision_object, SandBank):
            self.damage(0)
            self._movable = False
        elif isinstance(collision_object, Fortress):
            self.damage(1000)
        elif isinstance(collision_object, CannonBall):
            self.damage(40)

    def shoot(self):
        self._cannon.shoot(self.x, self.y, self._heading)

    def update(self):
        super().update()
        self.check_for_collision()
        DamageModel.update(self)

        if self.damage_state is self.DamageState.DAMAGED:
            self.set_velocity(int(self._speed / 2), self._heading)
        if self.damage_state is self.DamageState.UNMANEUVERABLE:
            self._movable = False
        if self.damage_state is self.DamageState.DESTROYED:
            self._is_alive = False
