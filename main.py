import os
import sys
from random import randint

import requests
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt, QPoint


# cities = ["Москва", "Париж", "Нью Йорк", "Берлин", "Рим", "Токио", "Сеул"]
# maps = {}
#
# for i, city in enumerate(cities):
#     geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
#     geocoder_params = {
#         "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
#         "geocode": city,
#         "format": "json",
#         "kind": "district",
#     }
#
#     response = requests.get(geocoder_api_server, params=geocoder_params)
#     # print(response.url)
#     if not response:
#         # обработка ошибочной ситуации
#         print("1Ошибка выполнения запроса:")
#         print(map_request)
#         print("Http статус:", response.status_code, "(", response.reason, ")")
#         sys.exit(1)
#
#     # Преобразуем ответ в json-объект
#     json_response = response.json()
#     # Получаем первый топоним из ответа геокодера.
#     toponym = json_response["response"]["GeoObjectCollection"][
#         "featureMember"][0]["GeoObject"]
#     # Координаты центра топонима:
#     toponym_coodrinates = toponym["Point"]["pos"]
#     toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
#
#
#     ll = f"{toponym_longitude},{toponym_lattitude}"
#
#
#     # locality = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][3]["name"]
#     # print(toponym_longitude, toponym_lattitude)
#
#     map_request = f"https://static-maps.yandex.ru/1.x/?ll={toponym_longitude},{toponym_lattitude}&spn=0.005,0.005&l=map"
#     response = requests.get(map_request)
#
#     if not response:
#         print("1Ошибка выполнения запроса:")
#         print(map_request)
#         print("Http статус:", response.status_code, "(", response.reason, ")")
#         sys.exit(1)

    # Запишем полученное изображение в файл.
    # map_file = f"map{i}.png"
    # with open(map_file, "wb") as file:
    #     file.write(response.content)
    # maps[city] = map_file


# # Инициализируем pygame
# pygame.init()
# screen = pygame.display.set_mode((600, 450))
# # Рисуем картинку, загружаемую из только что созданного файла.
# # Переключаем экран и ждем закрытия окна.
# player_1 = 1
# player_2 = 2
# run = True
#
# print(f"В игре можно загадать следующие города: {', '.join(list(maps.keys()))}.")
#
# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#
#     user_question = input(f"Игрок №{player_1} введите город, который надо отгадать: ")
#     while user_question not in maps:
#         print("Вы ввели город, которого нет в списке!")
#         print(f"В игре можно загадать следующие города: {', '.join(list(maps.keys()))}.")
#         user_question = input(f"Игрок №{player_1} введите город, который надо отгадать: ")
#     map_file = maps[user_question]
#     screen.blit(pygame.image.load(map_file), (0, 0))
#     pygame.display.flip()
#
#     user_answer = input(f"Игрок №{player_2}, часть какого города на картинке? ")
#     while user_answer not in maps:
#         print("Вы ввели город, которого нет в списке!")
#         print(f"В игре можно загадать следующие города: {', '.join(list(maps.keys()))}.")
#         user_answer = input(f"Игрок №{player_2}, часть какого города на картинке? ")
#
#     if user_question == user_answer:
#         print(f"Игрок {player_2} угадал!")
#     else:
#         print(f"Игрок {player_2} не угадал.")
#
#     player_1, player_2 = player_2, player_1





class MapsAPI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.setWindowTitle('Угадай город')
        self.setFixedSize(654, 600)

        self.cities = ["Москва", "Париж", "Нью Йорк", "Берлин", "Рим", "Токио", "Сеул"]
        self.maps = {}
        for i, city in enumerate(self.cities):
            geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
            geocoder_params = {
                "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
                "geocode": city,
                "format": "json",
                "kind": "district",
            }

            response = requests.get(geocoder_api_server, params=geocoder_params)
            # print(response.url)
            if not response:
                # обработка ошибочной ситуации
                print("1Ошибка выполнения запроса:")
                print(map_request)
                print("Http статус:", response.status_code, "(", response.reason, ")")
                sys.exit(1)

            # Преобразуем ответ в json-объект
            json_response = response.json()
            # Получаем первый топоним из ответа геокодера.
            toponym = json_response["response"]["GeoObjectCollection"][
                "featureMember"][0]["GeoObject"]
            # Координаты центра топонима:
            toponym_coodrinates = toponym["Point"]["pos"]
            toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

            ll = f"{toponym_longitude},{toponym_lattitude}"

            # locality = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][3]["name"]
            # print(toponym_longitude, toponym_lattitude)

            map_request = f"https://static-maps.yandex.ru/1.x/?ll={toponym_longitude},{toponym_lattitude}&spn=0.005,0.005&l=map"
            response = requests.get(map_request)
            if not response:
                print("1Ошибка выполнения запроса:")
                print(map_request)
                print("Http статус:", response.status_code, "(", response.reason, ")")
                sys.exit(1)
            # Запишем полученное изображение в файл.
            map_file = f"map{i}.png"
            with open(map_file, "wb") as file:
                file.write(response.content)
            self.maps[city] = [map_file]

            map_request = f"https://static-maps.yandex.ru/1.x/?ll={toponym_longitude},{toponym_lattitude}&spn=0.005,0.005&l=sat"
            response = requests.get(map_request)
            if not response:
                print("1Ошибка выполнения запроса:")
                print(map_request)
                print("Http статус:", response.status_code, "(", response.reason, ")")
                sys.exit(1)
            # Запишем полученное изображение в файл.
            map_file = f"map1{i}.png"
            with open(map_file, "wb") as file:
                file.write(response.content)
            self.maps[city].append(map_file)


        self.player1 = 1
        self.player2 = 2

        self.label.setText(f"Игрок №{self.player1} выберете город.")

        self.comboBox.addItem("")
        for city in self.cities:
            self.comboBox.addItem(city)

        self.curr_turn = "q"

        self.enterBtn.clicked.connect(self.turn)

    def loadImage(self):
        self.pixmap = QPixmap(self.curr_img)
        self.image.setPixmap(self.pixmap)

    def turn(self):
        if self.comboBox.currentText() == "":
            self.result.setText(f"Выберете город")
            return
        if self.curr_turn == "q":
            self.question()
            self.curr_turn = "a"
        else:
            self.answer()
            self.curr_turn = "q"
            self.player1, self.player2 = self.player2, self.player1
            self.label.setText(f"Игрок №{self.player1} выберете город.")
        # self.comboBox.setCurrentIndex(0)


    def question(self):
        self.user_question = self.comboBox.currentText()
        self.curr_img = self.maps[self.user_question][randint(0, 1)]
        self.comboBox.setCurrentIndex(0)
        self.loadImage()
        self.comboBox.setCurrentIndex(0)
        self.label.setText(f"Игрок №{self.player2} какой город на карте?")

    def answer(self):
        self.user_answer = self.comboBox.currentText()
        if self.user_question == self.user_answer:
            self.result.setText(f"Ура, игрок №{self.player2} угадал!")
        else:
            self.result.setText(f"Игрок №{self.player2} не угадал.")
        self.comboBox.setCurrentIndex(0)


    def closeEvent(self, event):
        # Удаляем за собой файлы с изображениями.
        for img in self.maps.values():
            os.remove(img[0])
            os.remove(img[1])


def except_hook(cls, exception, traceback):
    sys.excepthook(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MapsAPI()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())



pygame.quit()

