class PricingRule:
    def __init__(self, discountItem):
        self._discountItem = discountItem
    
    def applyDiscount(self, listOfItems):
        raise NotImplementedError

class XForY(PricingRule):
    def __init__(self, x, y, discountItem):
        super().__init__(discountItem)
        self._x = x
        self._y = y
    
    def applyDiscount(self, listOfItems):
        count = 0
        total = 0
        for item in listOfItems:
            if item.sku == self._discountItem.sku:
                count += 1
                if count % 3 == 0:
                    total -= item.price
        return total

class BulkDiscount(PricingRule):
    def __init__(self, threshold, newPrice, discountItem):
        super().__init__(discountItem)
        self._threshold = threshold
        self._newPrice = newPrice

    def applyDiscount(self, listOfItems):
        count = 0
        total = 0
        for item in listOfItems:
            if item.sku == self._discountItem.sku:
                count += 1
        if count > self._threshold:
            total += self._newPrice * count
            total -= self._discountItem.price * count
        return total

class FreeGift(PricingRule):
    def __init__(self, freeItem, discountItem):
        super().__init__(discountItem)
        self._freeItem = freeItem
    
    def applyDiscount(self, listOfItems):
        freeItemCount = 0
        mainItemCount = 0
        total = 0
        for item in listOfItems:
            if item.sku == self._discountItem.sku:
                mainItemCount += 1
            if item.sku == self._freeItem.sku:
                freeItemCount += 1
        if mainItemCount > freeItemCount:
            total -= self._freeItem.price * freeItemCount
        else:
            total -= self._freeItem.price * mainItemCount
        return total