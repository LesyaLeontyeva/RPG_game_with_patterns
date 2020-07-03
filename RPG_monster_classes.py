import random
from abc import ABC, abstractmethod


class Monster(ABC):
    low_health = 5
    high_health = 15
    low_attack = 2
    high_attack = 15
    health = 0
    strength = 0
    max_health = 0
    current_health = 0
    type = ''
    attack_type = ''

    @abstractmethod
    def attack(self) -> None:
        pass


class Goblin(Monster):
    health = random.randint(Monster.low_health, Monster.high_health)
    strength = random.randint(Monster.low_attack, Monster.high_attack)
    type = "Goblin"
    attack_type = "Archer"

    def attack(self) -> None:
        print("Вы встретили гоблина с атакой равной {} и здоровьем равным {}".format(Goblin.strength, Goblin.health))


class Orc(Monster):
    health = random.randint(Monster.low_health, Monster.high_health)
    strength = random.randint(Monster.low_attack, Monster.high_attack)
    type = "Orc"
    attack_type = "Warrior"

    def attack(self) -> None:
        print("Вы встретили орка с атакой равной {} и здоровьем равным {}".format(Orc.strength, Orc.health))


class Undead(Monster):
    health = random.randint(Monster.low_health, Monster.high_health)
    strength = random.randint(Monster.low_attack, Monster.high_attack)
    type = "Undead"
    attack_type = "Wizard"

    def attack(self) -> None:
        print("Вы встретили нежить с атакой равной {} и здоровьем равным {}".format(Undead.strength, Undead.health))


class MonsterFactory(ABC):
    @abstractmethod
    def create_monster(self) -> Monster:
        pass


class GoblinFactory(MonsterFactory):
    def create_monster(self) -> Monster:
        return Goblin()


class OrcFactory(MonsterFactory):
    def create_monster(self) -> Monster:
        return Orc()


class UndeadFactory(MonsterFactory):
    def create_monster(self) -> Monster:
        return Undead()
