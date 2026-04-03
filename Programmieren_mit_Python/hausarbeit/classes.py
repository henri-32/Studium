import math as m
from enum import Enum
from abc import ABC, abstractmethod


# Basisklasse
class GameObject(ABC):
    def __init__(
        self,
        x: int,
        y: int,
        movable: bool,
        ID: int = 0,
        width: int = 10,
        height: int = 10,
        **kwargs,
    ) -> None:
        self._ID = ID
        self._x_pos = x
        self._y_pos = y
        self._width = width
        self._height = height

        # Kennzeichnet, ob das Objekt noch im Spiel aktiv ist.
        self._is_alive = True

        # Beweglichkeit wird als Zustand geführt (keine eigene Subklasse),
        # damit sie sich im Spiel dynamisch ändern kann.
        self._movable = movable

        # Geschwindigkeit und Ausrichtung bilden die 2D-Bewegung ab.
        # Beide Werte starten bei 0.
        self._speed = 0

        # Heading: Ausrichtung des Objekts in Grad relativ zur 2D-Spielwelt.
        self._heading = 0

        # Ermöglicht kooperative Vererbung.
        super().__init__(**kwargs)

    # ====================================================
    # Public API
    # ====================================================
    def set_velocity(self, speed: int, heading_deg: int) -> None:
        """Setze Geschwindigkeit und Ausrichtung des Objekts."""
        if speed < 0:
            raise ValueError("speed may not be negative")
        else:
            self._speed = speed
        # Alternativ wäre eine Normalisierung mit Modulo denkbar. 
        # Der strikte Check macht jedoch fehlerhafte API-Nutzung früh sichtbar.
        if heading_deg < 0 or heading_deg >= 360:
            raise ValueError("heading must be 0 to 359")
        else:
            self._heading = heading_deg

    @abstractmethod
    def update(self) -> None:
        """Aktualisiere den Objektzustand pro Tick."""
        if self._movable:
            self._apply_velocity()

    # Nur lesende Properties.
    @property
    def x(self) -> int:
        return self._x_pos

    @property
    def y(self) -> int:
        return self._y_pos

    @property
    def velocity(self) -> tuple[int, int]:
        return (self._speed, self._heading)

    @property
    def can_move(self) -> bool:
        return self._movable

    @property
    def is_alive(self) -> bool:
        return self._is_alive

    # Berechnete Sicht:
    # Gibt alle Rasterkoordinaten zurück, die das Objekt belegt.
    @property
    def occupied_space(self) -> set[tuple[int, int]]:
        space = set()
        x_max = self.x + self._width
        y_max = self.y + self._height

        for i in range(int(self.x), int(x_max)):
            for j in range(int(self.y), int(y_max)):
                space.add((i, j))

        return space

    # ====================================================
    # Hilfsmethoden
    # ====================================================
    def _apply_velocity(self) -> None:
        """Wende Geschwindigkeit und Ausrichtung auf die Position an."""
        # Umrechnung von Heading (Grad) in kartesische Bewegung.
        self._x_pos += int(self._speed * m.cos(m.radians(self._heading)))
        self._y_pos += int(self._speed * m.sin(m.radians(self._heading)))


# Basisklasse
class DamageModel(ABC):
    class DamageState(Enum):
        OK = 3
        DAMAGED = 2
        UNMANEUVERABLE = 1
        DESTROYED = 0

    def __init__(self, max_health: int, **kwargs) -> None:
        self._max_health = max_health
        self._health = max_health
        self._damage_state = self.DamageState.OK

        # Auch hier kooperative Vererbung ermöglichen.
        super().__init__(**kwargs)

    def damage(self, damage: int) -> None:
        self._health = max(0, self._health - damage)

    # TODO DamageState Unmaneuverable semantisch bedenklich, wenn DamageModel
	# Auch für nicht movable Klassen integriert wird.
    def update(self) -> None:
        relative_damage = (self._health / self._max_health) * 100

        if relative_damage > 50:
            self._damage_state = self.DamageState.OK

        elif relative_damage > 25:
            self._damage_state = self.DamageState.DAMAGED

        elif relative_damage > 0:
            self._damage_state = self.DamageState.UNMANEUVERABLE

        else:
            self._damage_state = self.DamageState.DESTROYED

    @abstractmethod
    def apply_damage_to_abilities(self) -> None:
        pass

    @abstractmethod
    def check_for_collision(self) -> None:
        pass


class CollisionModel:
    # Arbeitet auf der zentralen Liste aller Spielobjekte.
    def __init__(self, objects_list: list[GameObject]) -> None:
        self._objects_list = objects_list

    # Bewusst ohne konkrete Typannotation:
    # Rückgabe und object_to_check hängen vom Aufrufer ab.
    def check_for_collision(
        self, object_to_check: GameObject
    ) -> GameObject | None:
        """Prüfe Kollisionen und gib das kollidierende Objekt zurück."""
        # Enthält alle Koordinaten, die das anfragende Objekt belegt.
        position_check_list = []
        for i in object_to_check.occupied_space:
            position_check_list.append(i)
        # Vergleiche mit allen anderen Objekten.
        for obj in self._objects_list:
            # Eigene Instanz und tote Objekte überspringen.
            if obj is object_to_check or obj.is_alive is False:
                continue

            for i in obj.occupied_space:
                if i in position_check_list:
                    return obj

#TODO War hier als Beispiel für Komposition, könnte aber eher auch als 
# Fähigkeit modelliert werden, welche direkt eine API zur verfügung stellt, da 
# gerade jede Cannon integrierende Klasse selber shoot definieren muss, was
# wiederum self.cannon.shoot aufruft. Da wäre abstrakte Klasse mit interface
# vielleicht Sinniger

class Cannon:
    def __init__(
        self,
        capacity: int,
        collision_model: CollisionModel,
        objects_list: list[GameObject],
    ) -> None:
        self.capacity = capacity
        self.collision_model = collision_model
        self.objects_list = objects_list

    def shoot(self, x: int, y: int, heading: int) -> None:
        aim = heading - 90
        if aim < 0:
            aim += 360

        shot = CannonBall(
            x=x,
            y=y,
            collision_model=self.collision_model,
            objects_list=self.objects_list,
        )

        shot.set_velocity(20, aim)


class Rock(GameObject):
    def __init__(self, ID: int, x: int, y: int, width: int, height: int):
        # Rocks sind statische Objekte.
        super().__init__(
            ID=ID, x=x, y=y, movable=False, width=width, height=height
        )

    # Keine Bewegung; Methode nur wegen abstrakter Basisklasse.
    def update(self) -> None:
        pass


class SandBank(GameObject):
    def __init__(self, ID: int, x: int, y: int, width: int, height: int):
        # Wie Rock: statisch.
        super().__init__(
            ID=ID, x=x, y=y, movable=False, width=width, height=height
        )

    def update(self) -> None:
        pass


class CannonBall(GameObject):
    def __init__(
        self,
        x: int,
        y: int,
        collision_model: CollisionModel,
        objects_list: list[GameObject],
    ) -> None:
        super().__init__(x=x, y=y, movable=True)
        objects_list.append(self)
        self._collision_model = collision_model

    def check_for_collision(self) -> None:
        collision_object = self._collision_model.check_for_collision(self)
        if collision_object is None or isinstance(collision_object, SandBank):
            return
        else:
            self._is_alive = False

    def update(self) -> None:
        super().update()
        self.check_for_collision()


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
        collision_model: CollisionModel,
        game_objects: list[GameObject],
    ) -> None:
        # Ships sind grundsätzlich beweglich.
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

    # Ship-Geschwindigkeit ist Teil des Klassenverhaltens und wird
    # über den Schadenszustand beeinflusst, nicht direkt extern gesetzt.
    def set_heading(self, heading: int) -> None:
        super().set_velocity(self._speed, heading)

    def check_for_collision(self) -> None:
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

    def shoot(self) -> None:
        self._cannon.shoot(self.x, self.y, self._heading)

    def apply_damage_to_abilities(self) -> None:
        # Leitet den Schadenszustand auf Fähigkeiten ab.
        if self._damage_state is self.DamageState.DAMAGED:
            self.set_velocity(int(self._speed / 2), self._heading)
        if self._damage_state is self.DamageState.UNMANEUVERABLE:
            self._movable = False
        if self._damage_state is self.DamageState.DESTROYED:
            self._is_alive = False

    def update(self) -> None:
        super().update()
        self.check_for_collision()
        self.apply_damage_to_abilities()


class Fortress(GameObject, DamageModel):
    def __init__(
        self,
        ID: int,
        x: int,
        y: int,
        width: int,
        height: int,
        max_health: int,
        collision_model: CollisionModel,
        game_objects: list[GameObject],
    ) -> None:
        # Fortress ist ebenfalls unbeweglich.
        super().__init__(
            ID=ID,
            x=x,
            y=y,
            movable=False,
            width=width,
            height=height,
            max_health=max_health,
        )
        self._collision_model = collision_model
        self._cannon = Cannon(
            capacity=500,
            collision_model=collision_model,
            objects_list=game_objects,
        )

    def check_for_collision(self) -> None:
        collision_object = self._collision_model.check_for_collision(self)
        if isinstance(collision_object, CannonBall):
            self.damage(50)

    def apply_damage_to_abilities(self) -> None:
        if self._damage_state is self.DamageState.DESTROYED:
            self._is_alive = False

    def update(self) -> None:
        super().update()
        self.check_for_collision()
        DamageModel.update(self)
        self.apply_damage_to_abilities()

    def shoot(self) -> None:
        self._cannon.shoot(self.x, self.y, 0)
        self._cannon.shoot(self.x, self.y, 90)
        self._cannon.shoot(self.x, self.y, 180)
        self._cannon.shoot(self.x, self.y, 270)
