# Определение класса Store
class Store:
    def __init__(self, name, address):
        """
        Конструктор, который инициализирует название и адрес магазина,
        а также пустой словарь для ассортимента товаров.
        """
        self.name = name  # Название магазина
        self.address = address  # Адрес магазина
        self.items = {}  # Ассортимент товаров (словарь)

    def add_item(self, item_name, price):
        """
        Метод для добавления товара в ассортимент магазина.
        """
        self.items[item_name] = price

    def remove_item(self, item_name):
        """
        Метод для удаления товара из ассортимента магазина.
        """
        if item_name in self.items:
            del self.items[item_name]
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")

    def get_price(self, item_name):
        """
        Метод для получения цены товара по его названию.
        Возвращает None, если товар отсутствует.
        """
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        """
        Метод для обновления цены товара.
        """
        if item_name in self.items:
            self.items[item_name] = new_price
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")

store3 = Store("Магазин Спортивный мир", "Улица Южная, дом 24")

store3.add_item("Велосипед", 7800)
store3.add_item("Самокат", 5300)
store3.add_item("Лыжи", 4800)
store3.add_item("Гантели", 2200)
store3.add_item("Бодибар", 1900)
store3.add_item("Гиря", 2500)

print("Товары в магазине Спортивный мир:")
print(store3.items)

store3.update_price("Лыжи", 4100)
store3.update_price("Велосипед", 8500)
print("Товары в магазине Спортивный мир после обновления цены:")
print(store3.items)

store3.remove_item("Гиря")
print("Товары в магазине Дачный уголок после удаления товара:")
print(store3.items)

print(f"Цена товара 'Лыжи': {store3.get_price('Лыжи')}")
print(f"Цена товара 'Гиря': {store3.get_price('Гиря')}")

