"""RPG игра с применений паттернов проектирования."""

import os
import pickle
import random

import sys
import time

import RPG_Hero_classes
import RPG_monster_classes
import RPG_weapon_abstract_fabric_class

delay = 2
hero_player: RPG_Hero_classes.Hero
enemy: RPG_monster_classes.Monster
weapon_type: RPG_weapon_abstract_fabric_class.Weapon


def main() -> None:
    """Главное меню."""
    print('Вы начинаете опасное путешествие!')
    print("1. Начать игру")
    print("2. Загрузить")
    print("3. Выйти из игры")
    option = input("->")
    if option == "1":
        start()
    elif option == "2":
        load()
    elif option == "3":
        sys.exit()
    else:
        main()


def load() -> None:
    """Фукнция для загрузки сохраненного файла с прогрессом игры."""
    if os.path.exists("save_file"):
        os.system('cls')
        with open('save_file', 'rb') as f:
            hero_p = pickle.load(f)
        global hero_player
        hero_player = hero_p
        print("Игра загружена")
        start1()
    else:
        print("Нет сохраненных игр")
        time.sleep(delay)
        main()


def start() -> None:
    """Старт игры."""
    print('\n' * 2)
    print("Выберите класс за который вы хотели бы играть?")
    print("1. Воин")
    print("2. Лучник")
    print("3. Маг")
    option = input("-->")
    global hero_player
    if option == "1":
        hero_player = RPG_Hero_classes.WarriorFactory().create_hero()
        start1()
    elif option == "2":
        hero_player = RPG_Hero_classes.ArcherFactory().create_hero()
        start1()
    elif option == "3":
        hero_player = RPG_Hero_classes.WizardFactory().create_hero()
        start1()
    else:
        start()


def events_generation() -> None:
    """Функиция для генерации события."""
    time.sleep(delay)
    print('\n' * 2)
    print("Начался новый день")
    event_gen = random.randint(1, 4)
    if event_gen == 1:
        weapon_generation()
    elif event_gen == 2:
        apple()
    elif event_gen == 3:
        choose_action(5, 0)
    elif event_gen == 4:
        pre_fight()
        # print("Вы столкнулись с врагом!")


def apple() -> None:
    """Функция для увеличения здоровья."""
    print('\n' * 2)
    apple_health = random.randint(5, 20)
    print('Вы нашли яблоко, которое увеличивает ваше здоровье на %s'
          % apple_health)
    hero_player.health = hero_player.health + apple_health
    print('Ваше текущее здоровье равно %s' % hero_player.health)

    events_generation()


def totem() -> None:
    """Фукнция, описывающая работу тотема."""
    print('\n' * 2)
    with open('save_file', 'wb') as f:
        pickle.dump(hero_player, f)
    print("Игра была сохранена")
    events_generation()


def weapon_generation() -> None:
    """Фукнция для генерации оружия."""
    print('\n' * 2)
    weapon_gen = random.randint(1, 4)
    global weapon_type
    if weapon_gen == 1:
        weapon_type = RPG_weapon_abstract_fabric_class.SwordFactory().create_weapon()
        weapon_type.find_weapon(hero_player.type)
        choose_action(1, weapon_type.strength)
    elif weapon_gen == 2:
        print("Вы нашли лук!")
        weapon_type = RPG_weapon_abstract_fabric_class.BowFactory().create_weapon()
        weapon_type.find_weapon(hero_player.type)
        choose_action(2, weapon_type.strength)
    elif weapon_gen == 3:
        amount = random.randint(2, 10)
        print("Вы нашли стрелы в количестве {} штук!".format(amount))
        hero_player.arrows += amount
        events_generation()
    elif weapon_gen == 4:
        weapon_type = RPG_weapon_abstract_fabric_class.MagicBookFactory().create_weapon()
        weapon_type.find_weapon(hero_player.type)
        print("Вы нашли магическую книгу!")
        choose_action(4, weapon_type.strength)


def choose_action(found: int, new: int) -> None:
    """Фукнция для выбора действия."""
    print('\n' * 2)
    found_name1 = ''
    if found == 1:
        found_name = "меч"
        found_name1 = 'sword'
    elif found == 2:
        found_name = "лук"
        found_name1 = 'bow'
    elif found == 3:
        found_name = "стрелы"
    elif found == 4:
        found_name = "магическую книгу"
        found_name1 = 'magic_book'
    elif found == 5:
        found_name = "тотем"
    else:
        found_name = " "
    print("Нажмите 1, чтобы подобрать {}, нажмите 2, чтобы пройти мимо".format(found_name))
    action = input()
    if action == "1" and found != 5:
        hero_player.weapon[found_name1][1] = str(new)
        print('Вы подобрали {} с силой {}'.format(found_name, new))
        events_generation()
    elif action == "1" and found == 5:
        print('Вы подобрали тотем')
        totem()
    elif action == "2":
        print('Вы прошли мимо')
        events_generation()
    else:
        choose_action(found, new)


def start1() -> None:
    """Загрузка сохраненной игры."""
    print('\n' * 2)
    print("Ваш класс: ", hero_player.type)
    print("Ваша атака равна ", hero_player.strength)
    print("Ваше здоровье равно : ", hero_player.health)
    print("В Вашем рюкзаке находится: ")
    for i in hero_player.weapon:
        if int(hero_player.weapon[i][1]) != 0:
            print('>', i)
    events_generation()


def pre_fight() -> None:
    """Генерация пртивников."""
    enemynum = random.randint(1, 3)
    global enemy
    if enemynum == 1:
        enemy = RPG_monster_classes.GoblinFactory().create_monster()
        enemy.attack()
    elif enemynum == 2:
        enemy = RPG_monster_classes.OrcFactory().create_monster()
        enemy.attack()
    else:
        enemy = RPG_monster_classes.UndeadFactory().create_monster()
        enemy.attack()
    fight()


def fight() -> None:
    """Выбор действия связанного с противником."""
    print('\n' * 2)
    print("Нажмите 1, чтобы сражаться, нажмите 2, чтобы убежать")
    option = input()
    if option == "1":
        combat()
    elif option == "2":
        print("Вы убежали от монстра")
        events_generation()
    else:
        fight()


def combat() -> None:
    """Фукнция, реализующая логику боя с противником."""
    i = 0
    while True:
        i += 1
        print('\n' * 2)
        print("Раунд {} начался!".format(i))
        check_bow()
        print('Ваше текущее здоровье равно {}'.format(hero_player.health))
        print('Текущее здоровье монстра равно {}'.format(enemy.health))
        choose_or_fight()
        if hero_player.weapon['bow'][0] == 'active':
            hero_player.arrows -= 1
        if hero_player.health <= enemy.strength:
            if miss(hero_player.type, enemy.attack_type) == 1:
                print('Вы нанесли {} урона по врагу'.format(hero_player.strength))
                print("Вам удалось уклониться от атаки врага")
                continue
            else:
                print("Потрачено")
                sys.exit()
        elif hero_player.strength >= enemy.health:
            print('Вы нанесли {} урона по врагу'.format(hero_player.strength))
            if miss(hero_player.type, enemy.attack_type) == 1:
                print("Вам удалось уклониться от атаки врага")
            else:
                print('Вы получили {} урона'.format(enemy.strength))
                hero_player.health -= enemy.strength
            print('Чудище побеждено!')
            events_generation()
        elif hero_player.strength < enemy.health and \
                enemy.strength < hero_player.health:
            print('Вы нанесли {} урона по врагу'.format(hero_player.strength))
            enemy.health -= hero_player.strength
            if miss(hero_player.type, enemy.attack_type) == 1:
                print("Вам удалось уклониться от атаки врага")
            else:
                print('Вы получили {} урона'.format(enemy.strength))
                hero_player.health -= enemy.strength


def check_bow() -> None:
    """Фукнция для проверки наличия стрел."""
    if hero_player.weapon['bow'][0] == 'active' and hero_player.arrows == 0:
        print('У вас отсутствуют стрелы, оружие изменено на меч')
        hero_player.weapon['bow'][0] = 'inactive'
        hero_player.weapon['sword'][0] = 'active'
        hero_player.strength = int(hero_player.weapon['sword'][1])


def choose_or_fight() -> None:
    """Фукнция для смены оружия и вступления в бой."""
    print('\n' * 2)
    print("Нажмите 1, чтобы сменить оружие, нажмите 2, чтобы сражаться")
    option = input()
    if option == "1":
        choose_weapon_for_attack()
    elif option == "2":
        print('Бой начался!')
    else:
        choose_or_fight()


def miss(hero_type: str, enemy_type: str) -> int:
    """Фукнция реализации промаха, если тип атаки героя и противника совпадают."""
    if hero_type == enemy_type:
        miss = random.randint(0, 1)
    else:
        miss = 0
    return miss


def choose_weapon_for_attack() -> None:
    """Фукнция выбора оружия для атаки."""
    print('\n' * 2)
    print("Выберите оружие для атаки")
    temp_list = []
    index_list = []
    j = 0
    for i in hero_player.weapon:
        if int(hero_player.weapon[i][1]) != 0:
            if i == 'bow':
                if hero_player.arrows == 0:
                    continue
            temp_list.append(i)
            j += 1
            index_list.append(j)
            print("{}.{}".format(j, i))
    option = input()
    if int(option) in index_list:
        hero_player.weapon[temp_list[int(option) - 1]][0] = 'active'
        for i in hero_player.weapon:
            if i != temp_list[int(option) - 1]:
                hero_player.weapon[i][0] = 'inactive'
        hero_player.strength = int(hero_player.weapon[temp_list[int(option) - 1]][1])
        print("Для атаки выбрано оружие {}".format(temp_list[int(option) - 1]))
    else:
        choose_weapon_for_attack()


main()
