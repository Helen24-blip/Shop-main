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

store2 = Store("Магазин Дачный уголок", "Улица Кирова, дом 15")

store2.add_item("Лопаты", 700)
store2.add_item("Грабли", 850)
store2.add_item("Вилы", 790)
store2.add_item("Распылитель", 1200)
store2.add_item("Шланг", 500)
store2.add_item("Лейка", 250)

print("Товары в магазине Дачный уголок:")
print(store2.items)

store2.update_price("Вилы", 890)
print("Товары в магазине Дачный уголок после обновления цены:")
print(store2.items)

store2.remove_item("Шланг")
print("Товары в магазине Дачный уголок после удаления товара:")
print(store2.items)

print(f"Цена товара 'Вилы': {store2.get_price('Вилы')}")
print(f"Цена товара 'Шланг': {store2.get_price('Шланг')}")

