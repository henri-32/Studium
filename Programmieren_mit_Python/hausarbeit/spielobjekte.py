from __future__ import annotations

from basisklassen import DamageModel, GameObject
from systemkomponenten import Cannon, CollisionModel


class Rock(GameObject):
    def __init__(self, ID: int, x: int, y: int, width: int, height: int):
        super().__init__(
            ID=ID, x=x, y=y, movable=False, width=width, height=height
        )

    def update(self) -> None:
        pass


class SandBank(GameObject):
    def __init__(self, ID: int, x: int, y: int, width: int, height: int):
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

    def set_heading(self, heading: int) -> None:
        super().set_velocity(self._speed, heading)

    def check_for_collision(self) -> None:
        collision_object = self._collision_model.check_for_collision(self)
        if collision_object is None:
            return
        if isinstance(collision_object, Ship):
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
        if self._damage_state is self.DamageState.DAMAGED:
            self.set_velocity(int(self._speed / 2), self._heading)
        if self._damage_state is self.DamageState.UNMANEUVERABLE:
            self._movable = False
        if self._damage_state is self.DamageState.DESTROYED:
            self._is_alive = False

    def update(self) -> None:
        super().update()
        self.check_for_collision()
        DamageModel.update(self)
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
