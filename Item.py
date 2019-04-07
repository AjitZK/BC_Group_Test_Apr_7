class Item:
    """
    A class that helps store information about Shopping-R-Us items\n
    Takes in the item's sku value (string), name (string) and price (float)
    """
    def __init__(self, sku = '', name = '', price = 0.00):
        if not isinstance(sku, str):
            print('The value of sku must be a string, so it is set to an empty string by default')
            sku = ''
        if not isinstance(name, str):
            print('The value of name must be a string, so it is set to an empty string by default')
            name = ''
        if not isinstance(price, float):
            print('Cannot accept a value for price that is not a float, so price is automatically set to $0.00')
            price = 0.00
        if price < 0.00:
            print('Cannot accept a value for price that is less than $0.00, so newPrice is automatically set to $0.00')
            newPrice = discountItem.price
        self._sku = sku
        self._name = name
        self._price = price
    
    # Getter for the sku value
    # Helps enforce that the values can't be tampered with once defined
    @property
    def sku(self):
        return self._sku

    # Getter for the price value
    # Helps enforce that the values can't be tampered with once defined
    @property
    def price(self):
        return self._price

# Subclasses for predefined items for an easier to use interface
# Completely optional and these classes only exist to help save time
class IPad(Item):
    """
    A Super iPad (sku: ipd) that costs $549.99
    """
    def __init__(self):
        super().__init__('ipd', 'Super iPad', 549.99)

class MacBookPro(Item):
    """
    A Macbook Pro (sku: mbp) that costs $1399.99
    """
    def __init__(self):
        super().__init__('mbp', 'Macbook Pro', 1399.99)

class AppleTV(Item):
    """
    An Apple TV (sku: atv) that costs $109.50
    """
    def __init__(self):
        super().__init__('atv', 'Apple TV', 109.50)

class VGAAdapter(Item):
    """
    A VGA adapter (sku: vga) that costs $30.00
    """
    def __init__(self):
        super().__init__('vga', 'VGA adapter', 30.00)