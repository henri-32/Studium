from __future__ import annotations

import math as m
from abc import ABC, abstractmethod
from enum import Enum


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
        self._is_alive = True
        self._movable = movable
        self._speed = 0
        self._heading = 0
        super().__init__(**kwargs)

    def set_velocity(self, speed: int, heading_deg: int) -> None:
        if speed < 0:
            raise ValueError("speed may not be negative")
        self._speed = speed

        if heading_deg < 0 or heading_deg >= 360:
            raise ValueError("heading must be 0 to 359")
        self._heading = heading_deg

    @abstractmethod
    def update(self) -> None:
        if self._movable:
            self._apply_velocity()

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

    @property
    def occupied_space(self) -> set[tuple[int, int]]:
        space = set()
        x_max = self.x + self._width
        y_max = self.y + self._height

        for i in range(int(self.x), int(x_max)):
            for j in range(int(self.y), int(y_max)):
                space.add((i, j))
        return space

    def _apply_velocity(self) -> None:
        self._x_pos += int(self._speed * m.cos(m.radians(self._heading)))
        self._y_pos += int(self._speed * m.sin(m.radians(self._heading)))


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
        super().__init__(**kwargs)

    def damage(self, damage: int) -> None:
        self._health = max(0, self._health - damage)

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
