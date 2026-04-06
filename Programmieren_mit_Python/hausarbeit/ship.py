from cannon import Cannon
from cannonball import CannonBall
from collision_model import CollisionModel
from damage_model import DamageModel
from fortress import Fortress
from game_object import GameObject
from rock import Rock
from sandbank import SandBank


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
        DamageModel.update(self)
        self.apply_damage_to_abilities()
