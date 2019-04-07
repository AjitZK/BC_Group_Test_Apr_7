from Item import Item

class PricingRule:
    """
    Abstract class for defining how to apply discounts for a particular item\n
    Takes in the item that will be given discounts
    """
    def __init__(self, discountItem):
        if not isinstance(discountItem, Item):
            print('Cannot accept a value for discountItem that is not of class Item, so discountItem is automatically set to Item(\'\',\'\',0.00)')
            discountItem = Item()
        self._discountItem = discountItem
    
    def applyDiscount(self, listOfItems):
        raise NotImplementedError

class XForY(PricingRule):
    """
    Enforces a deal where X items will be charged for the price of Y, for a particular item\n
    Takes in x (int), y (int) and the item (Item) to be discounted
    """
    def __init__(self, x, y, discountItem):
        super().__init__(discountItem)
        if not isinstance(x, int):
            print('Cannot accept a value for x that is not an integer, so x is automatically set to 1')
            x = 1
        if not isinstance(y, int):
            print('Cannot accept a value for y that is not an integer, so y is automatically set to 1')
            y = 1
        if x < 1:
            print('Cannot accept a value for x that is less than 1, so x is automatically set to 1')
            x = 1
        if y < 1:
            print('Cannot accept a value for y that is less than 1, so y is automatically set to 1')
            y = 1
        self._x = x
        self._y = y
    
    def applyDiscount(self, listOfItems=None):
        count = 0
        total = 0
        if listOfItems is not None: 
            # Finds all items that need to be discounted
            # subtracts all costs for items that should be given for free
            for item in listOfItems:
                if item.sku == self._discountItem.sku:
                    if (count % (self._x)) > (self._y - 1):
                        total -= item.price
                    count += 1
        return total

class BulkDiscount(PricingRule):
    """
    Enforces a deal where all items, given that there are more than the threshold, cost a new price for a particular item\n
    Takes in threshold (this discount only applies if there are n items such that n > threshold), 
    the new price of the item and the item to be discounted
    """
    def __init__(self, threshold, newPrice, discountItem):
        super().__init__(discountItem)
        if not isinstance(threshold, int):
            print('Cannot accept a value for threshold that is not an integer, so threshold is automatically set to 1')
            threshold = 1
        if not isinstance(newPrice, float):
            print('Cannot accept a value for newPrice that is not a float, so newPrice is automatically set to the current price of the item')
            newPrice = discountItem.price 
        if threshold < 1:
            print('Cannot accept a value for threshold that is less than 1, so threshold is automatically set to 1')
            threshold = 1
        if newPrice < 0.00:
            print('Cannot accept a value for newPrice that is less than $0.00, so newPrice is automatically set to the price of the item')
            newPrice = discountItem.price
        self._threshold = threshold
        self._newPrice = newPrice

    def applyDiscount(self, listOfItems=None):
        count = 0
        total = 0
        if listOfItems is not None:
            # Finds all items that need to be discounted
            # subtracts the supposed cost
            # and instead adds the cost with the new price in mind
            for item in listOfItems:
                if item.sku == self._discountItem.sku:
                    count += 1
            if count > self._threshold:
                total += self._newPrice * count
                total -= self._discountItem.price * count
        return total

class FreeGift(PricingRule):
    """
    Enforces a deal where n items are given for free if a particular item is purchased\n
    Takes in the number of free items that will be given, the item that needs to be free and the item to be discounted
    """
    def __init__(self, numberOfFreeItems, freeItem, discountItem):
        super().__init__(discountItem)
        if not isinstance(numberOfFreeItems, int):
            print('Cannot accept a value for numberOfFreeItems that is not an integer, so numberOfFreeItems is automatically set to 1')
            numberOfFreeItems = 1
        if numberOfFreeItems < 1:
            print('Cannot accept a value for numberOfFreeItems that is less than 1, so numberOfFreeItems is automatically set to 1')
            numberOfFreeItems = 1
        if not isinstance(freeItem, Item):
            print('Cannot accept a value for freeItem that is not of class Item, so freeItem is automatically set to Item(\'\',\'\',0.00)')
            freeItem = Item()
        self._numberOfFreeItems = numberOfFreeItems
        self._freeItem = freeItem
    
    def applyDiscount(self, listOfItems=None):
        freeItemCount = 0
        mainItemCount = 0
        total = 0
        if listOfItems is not None:
            # Finds all items that need to be discounted
            # subtracts all costs for items that should be given for free
            for item in listOfItems:
                if item.sku == self._discountItem.sku:
                    mainItemCount += 1
                if item.sku == self._freeItem.sku:
                    freeItemCount += 1
            if mainItemCount >= freeItemCount:
                total -= self._freeItem.price * freeItemCount
            else:
                total -= self._freeItem.price * mainItemCount
        return total