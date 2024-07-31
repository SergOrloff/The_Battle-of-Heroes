import random

class Hero:
    def __init__(self, name):
        # Инициализация героя с заданным именем
        self.name = name
        self.health = 100  # Здоровье героя
        self.attack_power = 20  # Сила атаки героя

    def attack(self, other):
        # Наносим урон другому герою
        damage = self.attack_power
        other.health -= damage  # Уменьшаем здоровье другого героя
        print(f"{self.name} атаковал {other.name} и нанес {damage} урона.")

    def is_alive(self):
        # Проверяем, жив ли герой (здоровье больше нуля)
        return self.health > 0

class Game:
    def __init__(self, player_name):
        # Создаем игроков: одного с именем игрока и одного с именем "Компьютер"
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print("Игра началась!")
        # Пока оба героя живы, продолжаем игру
        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока: игрок атакует компьютерного героя
            self.player.attack(self.computer)
            self.display_health()
            if not self.computer.is_alive():
                print(f"{self.player.name} победил!")  # Объявляем победу игрока
                break

            # Ход компьютера: компьютерный герой атакует игрока
            self.computer.attack(self.player)
            self.display_health()
            if not self.player.is_alive():
                print(f"{self.computer.name} победил!")  # Объявляем победу компьютера
                break

    def display_health(self):
        # Выводим здоровье обоих героев
        print(f"{self.player.name} здоровье: {self.player.health}")
        print(f"{self.computer.name} здоровье: {self.computer.health}")

if __name__ == "__main__":
    # Запрашиваем имя игрока
    player_name = input("Введите имя вашего героя: ")
    # Создаем и запускаем игру
    game = Game(player_name)
    game.start()