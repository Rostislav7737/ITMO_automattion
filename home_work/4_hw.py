# Задание 1: Прямоугольник
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


rect1 = Rectangle(5, 3)
rect2 = Rectangle(10, 4)
rect3 = Rectangle(7, 2)

print("Прямоугольник 1: площадь =", rect1.area(), "периметр =", rect1.perimeter())
print("Прямоугольник 2: площадь =", rect2.area(), "периметр =", rect2.perimeter())
print("Прямоугольник 3: площадь =", rect3.area(), "периметр =", rect3.perimeter())


# Задание 2: Класс Math
class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print(self.a + self.b)

    def multiplication(self):
        print(self.a * self.b)

    def division(self):
        print(self.a / self.b)

    def subtraction(self):
        print(self.a - self.b)


math1 = Math(10, 2)
math1.addition()
math1.multiplication()
math1.division()
math1.subtraction()


# Задание 3: Кнопки на странице
class Button:
    def __init__(self, text):
        self.text = text
        self.type = "Кнопка"
        self.locator = ""

    def click(self):
        return f"Клик по кнопке {self.text}"


text_box = Button("Text Box")
check_box = Button("Check Box")
radio_button = Button("Radio Button")
web_tables = Button("Web Tables")
buttons = Button("Buttons")
links = Button("Links")
broken_links = Button("Broken Links")
upload_download = Button("Upload and Download")
dynamic_properties = Button("Dynamic Properties")

buttons_list = [text_box, check_box, radio_button, web_tables, buttons,
                links, broken_links, upload_download, dynamic_properties]

# Выводим текст для каждой кнопки
for btn in buttons_list:
    print(btn.text)

# Вызываем клик для каждой кнопки
for btn in buttons_list:
    print(btn.click())


# Задание 4 (Доп): Класс Car (отдельный файл)
class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print("Автомобиль заведен")

    def stop(self):
        print("Автомобиль заглушен")

    def set_year(self, year):
        self.year = year

    def set_type(self, type):
        self.type = type

    def set_color(self, color):
        self.color = color


# Пример использования
my_car = Car("Красный", "Седан", 2020)
my_car.start()
my_car.stop()
my_car.set_year(2022)
my_car.set_type("Хэтчбек")
my_car.set_color("Синий")
