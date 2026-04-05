from game_object import GameObject


class SandBank(GameObject):
    def __init__(self, ID: int, x: int, y: int, width: int, height: int):
        # Wie Rock: statisch.
        super().__init__(
            ID=ID, x=x, y=y, movable=False, width=width, height=height
        )

    def update(self) -> None:
        pass
