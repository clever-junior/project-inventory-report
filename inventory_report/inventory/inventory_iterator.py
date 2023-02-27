from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, dados):
        self.dados = dados
        self.contador = 0

    def __next__(self):
        elemento = self.dados[self.contador]

        if not elemento:
            raise StopIteration

        self.contador += 1
        return elemento
