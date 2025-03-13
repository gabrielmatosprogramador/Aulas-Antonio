class Order:
    def __init__(self, total_price, status, client):
        self._total_price = total_price
        self._status = status
        self._client = client
        self._items = []

    def add_item(self, order_item):
        self._items.append(order_item)

    def verifica_total(self):
        result = sum(item.verifica_total() for item in self._items)
        if result == self._total_price:
            return "O valor está correto!"
        else:
            return "O valor está errado"
        