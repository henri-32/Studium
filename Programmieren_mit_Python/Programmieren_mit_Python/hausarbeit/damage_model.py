from abc import ABC, abstractmethod
from enum import Enum


# Basisklasse
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

        # Auch hier kooperative Vererbung ermöglichen.
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
