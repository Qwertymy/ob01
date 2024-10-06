class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
        else:
            print(f"Товар '{item_name}' отсутствует в ассортименте.")

    def get_item_price(self, item_name):
        return self.items.get(item_name, None)

    def update_item_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
        else:
            print(f"Товар '{item_name}' отсутствует в ассортименте.")

    def __str__(self):
        return f"Магазин: {self.name}, Адрес: {self.address}, Ассортимент: {self.items}"

store1 = Store("Магазин Продукты 24", "ул. Ленина, 12")
store2 = Store("ТехноМаркет", "проспект Мира, 50")
store3 = Store("Книжный Мир", "ул. Пушкина, 34")

store1.add_item("молоко", 90)
store1.add_item("хлеб", 65)
store1.add_item("яйца", 150)
store1.add_item("сыр", 250)
store1.add_item("колбаса", 330)
store1.add_item("сок", 200)

store2.add_item("смартфон", 15600)
store2.add_item("ноутбук", 45000)
store2.add_item("наушники", 9600)
store2.add_item("телевизор", 75000)
store2.add_item("фотоаппарат", 96000)
store2.add_item("игровая консоль", 220000)

store3.add_item("роман", 1500)
store3.add_item("блокнот", 300)
store3.add_item("ручка", 45)
store3.add_item("энциклопедия", 680)
store3.add_item("учебник", 470)
store3.add_item("карта мира", 190)

print(store1)
print(store2)
print(store3)

# Проверка методов

print(store2)
print("Проверка цены:")
price = store2.get_item_price("ноутбук")
print(f"Цена на ноутбук: {price}")

price = store2.get_item_price("телевизор")
print(f"Цена на телевизор: {price}")

price = store2.get_item_price("планшет")
print(f"Цена на планшет: {price}")

print("Обновление цены:")
store2.update_item_price("смартфон", 23500)
print(store2.get_item_price("смартфон"))

print("Удаление товара:")
store2.remove_item("фотоаппарат")
print(store2)

store2.remove_item("планшет")
