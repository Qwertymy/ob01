# Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Этот метод должен быть переопределен в подклассе")

    def eat(self):
        print(f"{self.name} ест.")

# Подкласс Bird (Птица)
class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span  # размах крыльев

    def make_sound(self):
        print(f"{self.name} чирикает.")

# Подкласс Mammal (Млекопитающее)
class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color  # цвет меха

    def make_sound(self):
        print(f"{self.name} рычит.")

# Подкласс Reptile (Рептилия)
class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type  # тип чешуи

    def make_sound(self):
        print(f"{self.name} шипит.")

# Полиморфизм - функция, принимающая список животных
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

# Класс сотрудника зоопарка ZooKeeper
class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"Смотритель {self.name} кормит животное {animal.name}.")

# Класс ветеринара Veterinarian
class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"Ветеринар {self.name} лечит животное {animal.name}.")

# Класс зоопарка, использующий композицию
class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []  # список животных в зоопарке
        self.staff = []    # список сотрудников

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal.name} добавлено в зоопарк {self.name}.")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"Сотрудник {staff_member.name} добавлен в зоопарк {self.name}.")

    def zoo_details(self):
        print(f"Зоопарк {self.name} содержит {len(self.animals)} животных и {len(self.staff)} сотрудников.")

# Пример использования

# Создание животных
eagle = Bird(name="Орел", age=5, wing_span=2.0)
lion = Mammal(name="Лев", age=8, fur_color="Золотой")
snake = Reptile(name="Змея", age=3, scale_type="Гладкая")

# Создание сотрудников
keeper = ZooKeeper(name="Андрей")
vet = Veterinarian(name="Марина")

# Создание зоопарка
zoo = Zoo(name="Городской зоопарк")

# Добавление животных в зоопарк
zoo.add_animal(eagle)
zoo.add_animal(lion)
zoo.add_animal(snake)

# Добавление сотрудников в зоопарк
zoo.add_staff(keeper)
zoo.add_staff(vet)

# Демонстрация полиморфизма
animal_sound([eagle, lion, snake])

# Использование методов сотрудников
keeper.feed_animal(lion)
vet.heal_animal(snake)

# Информация о зоопарке
zoo.zoo_details()
