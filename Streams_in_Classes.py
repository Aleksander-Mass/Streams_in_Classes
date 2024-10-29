import threading
import time

# Общее количество врагов для всех рыцарей
TOTAL_ENEMIES = 100
# Блокировка для синхронизации доступа к общему количеству врагов
lock = threading.Lock()

###   Пункты задачи:

#  1. Создайте класс Knight с соответствующими описанию свойствами.
class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0  # Счетчик дней, в течение которых рыцарь сражается

    # Создание метода run, в котором рыцарь будет сражаться с врагами:

    def run(self):
        global TOTAL_ENEMIES
        print(f"{self.name}, на нас напали!")

        while True:
            with lock:  # Защищаем общий ресурс (количество врагов) с помощью блокировки
                if TOTAL_ENEMIES <= 0:
                    break

                TOTAL_ENEMIES -= self.power
                if TOTAL_ENEMIES < 0:
                    TOTAL_ENEMIES = 0

            self.days += 1
            print(f"{self.name} сражается {self.days} день(дня)..., осталось {TOTAL_ENEMIES} воинов.")
            time.sleep(1)

        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


# Создание рыцарей
###  2. Создайте и запустите 2 потока на основе класса Knight.
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание завершения всех сражений
first_knight.join()
second_knight.join()

###   3. Выведите на экран строку об окончании битв.
print("Все битвы закончились!")

###   Вывод на консоль:
"""
Sir Lancelot, на нас напали!
Sir Lancelot сражается 1 день(дня)..., осталось 90 воинов.
Sir Galahad, на нас напали!
Sir Galahad сражается 1 день(дня)..., осталось 70 воинов.
Sir Lancelot сражается 2 день(дня)..., осталось 60 воинов.
Sir Galahad сражается 2 день(дня)..., осталось 40 воинов.
Sir Lancelot сражается 3 день(дня)..., осталось 30 воинов.
Sir Galahad сражается 3 день(дня)..., осталось 10 воинов.
Sir Lancelot сражается 4 день(дня)..., осталось 0 воинов.
Sir Galahad одержал победу спустя 3 дней(дня)!
Sir Lancelot одержал победу спустя 4 дней(дня)!
Все битвы закончились!
"""