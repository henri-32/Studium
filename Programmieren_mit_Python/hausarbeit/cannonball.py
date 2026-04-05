from collision_model import CollisionModel
from game_object import GameObject
from sandbank import SandBank


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
