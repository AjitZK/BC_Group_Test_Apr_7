class Item:
    def __init__(self, sku, name, price):
        self._sku = sku
        self._name = name
        self._price = price
    
    @property
    def sku(self):
        return self._sku

    @property
    def price(self):
        return self._price

class IPad(Item):
    def __init__(self):
        super().__init__('ipd', 'Super iPad', 549.99)

class MacBookPro(Item):
    def __init__(self):
        super().__init__('mbp', 'Macbook Pro', 1399.99)

class AppleTV(Item):
    def __init__(self):
        super().__init__('atv', 'Apple TV', 109.50)

class VGAAdapter(Item):
    def __init__(self):
        super().__init__('vga', 'VGA adapter', 30.00)