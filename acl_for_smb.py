class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self, new_name):
        self._name = new_name


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'
        self._user_list = []

    def add_user(self, user):
        if user not in self._user_list:
            self._user_list.append(user)

    def remove_user(self, user):
        if user in self._user_list:
            self._user_list.remove(user)

    def get_user_list(self):
        return self._user_list

    def display_admins(self):
     #   admin_list[]
        for user in self._user_list:
            if user.get_access_level() == 'admin':
                print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")


# Пример использования:
admin1 = Admin('001', 'Александр')
admin2 = Admin('002', 'Антон')
user1 = User('003', 'Иван')
user2 = User('004', 'Ирина')
user3 = User('005', 'Николай')

admin1.add_user(user1)
admin1.add_user(user2)
admin1.add_user(user3)
admin2.add_user(admin1)
admin1.add_user(admin2)

# Вывод списка пользователей
for user in admin1.get_user_list():
    print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")

# Удаление пользователя
admin1.remove_user(user1)

# Вывод списка пользователей после удаления
for user in admin2.get_user_list():
    print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")

print("Информация о другом администраторе:")
admin2.display_admins()

# Вывод информации о пользователе и его уровне доступа - сам про себя
print("Информация о ceбe:")
print (f"ID: {user3.get_user_id()}, Имя: {user3.get_name()}, Уровень доступа: {user3.get_access_level()}")