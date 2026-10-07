import sys
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


# 🪟 КЛАСС ГЛАВНОГО ОКНА ПРИЛОЖЕНИЯ
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Инициализация родительского класса

        # 🖼️ Настройки окна
        self.setWindowTitle("Моё приложение")    # Заголовок окна
        self.setFixedSize(QSize(400, 300))       # Фиксированный размер

        # 🔘 СОЗДАЁМ КНОПКУ
        self.button = QPushButton("Привет, мир!") # Кнопка с начальной надписью
        self.button.setCheckable(True)       # Делает кнопку "переключаемой"

        # 📌 Устанавливаем начальное состояние кнопки (нажата)
        self.button_is_checked = True
        self.button.setChecked(self.button_is_checked)

        # 📡 ПОДКЛЮЧАЕМ СИГНАЛЫ К СЛОТАМ
        self.button.clicked.connect(self.the_button_was_clicked)   # При клике вызывается метод 1
        self.button.clicked.connect(self.the_button_was_toggled)   # Тот же сигнал передаёт состояние (True/False)

        # 🧩 Размещаем кнопку по центру окна
        self.setCentralWidget(self.button)


    # 🎯 СЛОТ 1: Обработка клика по кнопке
    def the_button_was_clicked(self):
        print("Кнопка нажата!")                      # Печать в консоль
        self.button.setText("До свидания!")          # Меняем текст на кнопке
        self.button.setEnabled(False)                # Отключаем кнопку (делаем неактивной)

    # 🎯 СЛОТ 2: Обработка изменения состояния кнопки (включена/выключена)
    def the_button_was_toggled(self, checked):
        if checked:
            print("Состояние: Нажата")               # Если кнопка нажата
        else:
            print("Состояние: Отжата")               # Если кнопка отжата



# 🚀 ЗАПУСК ПРИЛОЖЕНИЯ
app = QApplication(sys.argv)     # Создаём объект приложения
window = MainWindow()            # Создаём главное окно
window.show()                    # Показываем окно
app.exec()                       # Запускаем цикл обработки событий
