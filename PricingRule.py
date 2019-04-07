class PricingRule:
    def __init__(self, discountItem):
        self._discountItem = discountItem
        
    @property
    def discountItem(self):
        return self._discountItem

class XForY(PricingRule):
    def __init__(self, x, y, discountItem):
        super().__init__(discountItem)
        self._x = x
        self._y = y

class BulkDiscount(PricingRule):
    def __init__(self, threshold, newPrice, discountItem):
        super().__init__(discountItem)
        self._threshold = threshold
        self._newPrice = newPrice
    
    @property
    def threshold(self):
        return self._threshold
    
    @property
    def newPrice(self):
        return self._newPrice

class FreeGift(PricingRule):
    def __init__(self, freeItem, discountItem):
        super().__init__(discountItem)
        self._freeItem = freeItem
    
    @property
    def freeItem(self):
        return self._freeItem