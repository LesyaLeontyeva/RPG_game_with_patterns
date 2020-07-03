from abc import ABC, abstractmethod
import random


class Weapon(ABC):
    strength = 0
    low_strength = 5
    high_strength = 10
    type = ''

    @abstractmethod
    def find_weapon(self, hero_type: str) -> None:
        pass


class Sword(Weapon):
    strength = 0
    type = 'sword'

    def find_weapon(self, hero_type: str) -> None:
        # print(Sword.strength)
        if hero_type == "Warrior":
            Sword.strength = random.randint(Weapon.low_strength, Weapon.high_strength + 10)
        else:
            Sword.strength = random.randint(Weapon.low_strength, Weapon.high_strength)
        print("вы нашли меч с силой равной {}".format(Sword.strength))


class Bow(Weapon):
    strength = 0
    type = 'bow'

    def find_weapon(self, hero_type: str) -> None:
        if hero_type == "Archer":
            Bow.strength = random.randint(Weapon.low_strength, Weapon.high_strength + 10)
        else:
            Bow.strength = random.randint(Weapon.low_strength, Weapon.high_strength)
        print("вы нашли лук с силой равной {}".format(Bow.strength))


class MagicBook(Weapon):
    strength = 0
    type = 'magic_book'

    def find_weapon(self, hero_type: str) -> None:
        if hero_type == "Wizard":
            MagicBook.strength = random.randint(Weapon.low_strength, Weapon.high_strength + 10)
        else:
            MagicBook.strength = random.randint(Weapon.low_strength, Weapon.high_strength)
        print("вы нашли магическую книгу с силой равной {}".format(MagicBook.strength))


class WeaponFactory(ABC):
    @abstractmethod
    def create_weapon(self) -> Weapon:
        pass


class SwordFactory(WeaponFactory):
    def create_weapon(self) -> Weapon:
        return Sword()


class BowFactory(WeaponFactory):
    def create_weapon(self) -> Weapon:
        return Bow()


class MagicBookFactory(WeaponFactory):
    def create_weapon(self) -> Weapon:
        return MagicBook()
