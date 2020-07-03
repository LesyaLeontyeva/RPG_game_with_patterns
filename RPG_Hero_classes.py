from abc import ABC, abstractmethod


class Hero(ABC):
    health = 50
    strength = 0
    max_health = 0
    current_health = 0
    type = ''
    weapon = {'sword': ['active', '10'], 'bow': ['inactive', '20'],
              'magic_book': ['inactive', '30']}
    arrows = 50

    @abstractmethod
    def attack(self) -> None:
        pass


class Warrior(Hero):
    strength = 10
    type = "Warrior"

    def attack(self) -> None:
        pass


class Archer(Hero):
    strength = 10
    type = "Archer"

    def attack(self) -> None:
        pass


class Wizard(Hero):
    strength = 10
    type = "Wizard"

    def attack(self)->None:
        pass


class HeroFactory(ABC):
    @abstractmethod
    def create_hero(self) -> Hero:
        pass


class WarriorFactory(HeroFactory):
    def create_hero(self) -> Hero:
        return Warrior()


class ArcherFactory(HeroFactory):
    def create_hero(self) -> Hero:
        return Archer()


class WizardFactory(HeroFactory):
    def create_hero(self) -> Hero:
        return Wizard()
