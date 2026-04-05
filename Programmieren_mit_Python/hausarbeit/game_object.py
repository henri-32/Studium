import math as m
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
