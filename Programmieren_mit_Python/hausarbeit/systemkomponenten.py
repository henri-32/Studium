from __future__ import annotations

from basisklassen import GameObject


class CollisionModel:
    def __init__(self, objects_list: list[GameObject]) -> None:
        self._objects_list = objects_list

    def check_for_collision(
        self, object_to_check: GameObject
    ) -> GameObject | None:
        position_check_list = []
        for i in object_to_check.occupied_space:
            position_check_list.append(i)

        for obj in self._objects_list:
            if obj is object_to_check or obj.is_alive is False:
                continue

            for i in obj.occupied_space:
                if i in position_check_list:
                    return obj
        return None


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

        from spielobjekte import CannonBall

        shot = CannonBall(
            x=x,
            y=y,
            collision_model=self.collision_model,
            objects_list=self.objects_list,
        )
        shot.set_velocity(20, aim)
