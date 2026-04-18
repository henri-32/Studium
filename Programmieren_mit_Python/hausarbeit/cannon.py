from cannonball import CannonBall
from collision_model import CollisionModel
from game_object import GameObject


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
