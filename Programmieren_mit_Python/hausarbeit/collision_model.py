from game_object import GameObject


class CollisionModel:
    # Arbeitet auf der zentralen Liste aller Spielobjekte.
    def __init__(self, objects_list: list[GameObject]) -> None:
        self._objects_list = objects_list

    # Bewusst ohne konkrete Typannotation:
    # Rückgabe und object_to_check hängen vom Aufrufer ab.
    def check_for_collision(
        self, object_to_check: GameObject
    ) -> GameObject | None:
        """Prüfe Kollisionen und gib das kollidierende Objekt zurück."""
        # Enthält alle Koordinaten, die das anfragende Objekt belegt.
        position_check_list = []
        for i in object_to_check.occupied_space:
            position_check_list.append(i)
        # Vergleiche mit allen anderen Objekten.
        for obj in self._objects_list:
            # Eigene Instanz und tote Objekte überspringen.
            if obj is object_to_check or obj.is_alive is False:
                continue

            for i in obj.occupied_space:
                if i in position_check_list:
                    return obj
