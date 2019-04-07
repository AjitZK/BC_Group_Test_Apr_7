class PricingRule:
    def __init__(self, sku):
        self._sku = sku
        
    @property
    def sku(self):
        return self._sku

class XForY(PricingRule):
    def __init__(self, x, y, sku):
        super().__init__(sku)
        self._x = x
        self._y = y

class BulkDiscount(PricingRule):
    def __init__(self, threshold, newPrice, sku):
        super().__init__(sku)
        self._threshold = threshold
        self._newPrice = newPrice
    
    @property
    def threshold(self):
        return self._threshold
    
    @property
    def newPrice(self):
        return self._newPrice

class FreeGift(PricingRule):
    def __init__(self, freeItem, sku):
        super().__init__(sku)
        self._freeItem = freeItem
    
    @property
    def freeItem(self):
        return self._freeItem