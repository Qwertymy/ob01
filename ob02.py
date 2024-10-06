class User:
    def __init__(self, user_id: int, name: str):
        # Приватные атрибуты
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'

    # Методы для получения информации
    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    # Методы для изменения данных
    def set_name(self, name: str):
        self._name = name

    def set_access_level(self, level: str):
        if level in ['user', 'admin']:
            self._access_level = level
        else:
            raise ValueError("Недопустимый уровень доступа")


class Admin(User):
    def __init__(self, user_id: int, name: str):
        # Наследуем инициализацию от User, но устанавливаем доступ для администратора
        super().__init__(user_id, name)
        self._access_level = 'admin'

    # Метод добавления нового пользователя
    def add_user(self, user_list: list, user: User):
        if not isinstance(user, User):
            raise TypeError("Добавлять можно только экземпляры класса User")
        user_list.append(user)
        print(f"Пользователь {user.get_name()} успешно добавлен.")

    # Метод удаления пользователя по ID
    def remove_user(self, user_list: list, user_id: int):
        user_to_remove = None
        for user in user_list:
            if user.get_user_id() == user_id:
                user_to_remove = user
                break

        if user_to_remove:
            user_list.remove(user_to_remove)
            print(f"Пользователь {user_to_remove.get_name()} успешно удален.")
        else:
            print(f"Пользователь с ID {user_id} не найден.")


# Пример использования системы

# Создаем список пользователей
user_list = []

# Создаем пользователей
user1 = User(1, "Иван Иванов")
user2 = User(2, "Ольга Смирнова")
admin = Admin(99, "Администратор")

# Администратор добавляет пользователей
admin.add_user(user_list, user1)
admin.add_user(user_list, user2)

# Администратор удаляет пользователя
admin.remove_user(user_list, 1)

# Проверка информации о пользователях
for user in user_list:
    print(f"ID: {user.get_user_id()}, Имя: {user.get
