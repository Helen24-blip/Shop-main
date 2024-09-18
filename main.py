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
