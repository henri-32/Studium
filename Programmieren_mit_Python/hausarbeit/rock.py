from game_object import GameObject


class Rock(GameObject):
    def __init__(self, ID: int, x: int, y: int, width: int, height: int):
        # Rocks sind statische Objekte.
        super().__init__(
            ID=ID, x=x, y=y, movable=False, width=width, height=height
        )

    # Keine Bewegung; Methode nur wegen abstrakter Basisklasse.
    def update(self) -> None:
        pass
