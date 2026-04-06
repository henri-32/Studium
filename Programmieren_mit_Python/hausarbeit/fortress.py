from cannon import Cannon
from cannonball import CannonBall
from collision_model import CollisionModel
from damage_model import DamageModel
from game_object import GameObject


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
