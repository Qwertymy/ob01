import json

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Этот метод должен быть переопределен в подклассе")

    def eat(self):
        print(f"{self.name} ест.")

    def to_dict(self):
        return {
            'type': self.__class__.__name__,
            'name': self.name,
            'age': self.age
        }

    @staticmethod
    def from_dict(data):
        animal_type = data['type']
        if animal_type == 'Bird':
            return Bird(data['name'], data['age'], data['wing_span'])
        elif animal_type == 'Mammal':
            return Mammal(data['name'], data['age'], data['fur_color'])
        elif animal_type == 'Reptile':
            return Reptile(data['name'], data['age'], data['scale_type'])
        else:
            raise ValueError("Неизвестный тип животного")

class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span  # размах крыльев

    def make_sound(self):
        print(f"{self.name} чирикает.")

    def to_dict(self):
        data = super().to_dict()
        data['wing_span'] = self.wing_span
        return data

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color  # цвет меха

    def make_sound(self):
        print(f"{self.name} рычит.")

    def to_dict(self):
        data = super().to_dict()
        data['fur_color'] = self.fur_color
        return data

class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type  # тип чешуи

    def make_sound(self):
        print(f"{self.name} шипит.")

    def to_dict(self):
        data = super().to_dict()
        data['scale_type'] = self.scale_type
        return data

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"Смотритель {self.name} кормит животное {animal.name}.")

    def to_dict(self):
        return {'name': self.name, 'role': 'ZooKeeper'}

class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"Ветеринар {self.name} лечит животное {animal.name}.")

    def to_dict(self):
        return {'name': self.name, 'role': 'Veterinarian'}

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

    def to_dict(self):
        return {
            'name': self.name,
            'animals': [animal.to_dict() for animal in self.animals],
            'staff': [staff_member.to_dict() for staff_member in self.staff]
        }

    @staticmethod
    def from_dict(data):
        zoo = Zoo(data['name'])
        for animal_data in data['animals']:
            zoo.add_animal(Animal.from_dict(animal_data))
        for staff_data in data['staff']:
            if staff_data['role'] == 'ZooKeeper':
                zoo.add_staff(ZooKeeper(staff_data['name']))
            elif staff_data['role'] == 'Veterinarian':
                zoo.add_staff(Veterinarian(staff_data['name']))
        return zoo

    def save_zoo(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.to_dict(), f, ensure_ascii=False, indent=4)
        print(f"Данные зоопарка сохранены в файл {filename}.")

    @staticmethod
    def load_zoo(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"Данные зоопарка загружены из файла {filename}.")
        return Zoo.from_dict(data)

# Пример

eagle = Bird(name="Орел", age=5, wing_span=2.0)
lion = Mammal(name="Лев", age=8, fur_color="Золотой")
snake = Reptile(name="Змея", age=3, scale_type="Гладкая")

keeper = ZooKeeper(name="Андрей")
vet = Veterinarian(name="Марина")

zoo = Zoo(name="Городской зоопарк")

zoo.add_animal(eagle)
zoo.add_animal(lion)
zoo.add_animal(snake)

zoo.add_staff(keeper)
zoo.add_staff(vet)

zoo.save_zoo('zoo_data.json')

loaded_zoo = Zoo.load_zoo('zoo_data.json')
loaded_zoo.zoo_details()

animal_sound(loaded_zoo.animals)

keeper.feed_animal(lion)
vet.heal_animal(snake)
