from Item import Item
from PricingRule import PricingRule, XForY, BulkDiscount, FreeGift

class Checkout:
    def __init__(self, pricingRules=None):
        if pricingRules is None:
            self._pricingRules = []
        else:
            ok = True
            for rule in pricingRules:
                if not isinstance(rule, PricingRule):
                    ok = False
                    print('pricing rules is not an array of only instances of class PricingRule')
                    break
            if ok:
                self._pricingRules = pricingRules
            else:
                self._pricingRules = []
        self._listOfItems = []
        self._total = 0

    def scan(self, item):
        if isinstance(item,Item):
            self._listOfItems.append(item)
    
    def totalPrice(self):
        self._total = 0
        for rule in self._pricingRules:
            if isinstance(rule, XForY):
                count = 1
                for item in self._listOfItems:
                    if item.sku == rule.sku:
                        count += 1
                        if count % 3 == 0:
                            self._total -= item.price
            elif isinstance(rule, BulkDiscount):
                count = 0
                for item in self._listOfItems:
                    if item.sku == rule.sku:
                        count += 1
                if count >= rule.threshold:
                    self._total += rule.newPrice * count
                    self.total -= item.price * count
            elif isinstance(rule, FreeGift):
                freeItemCount = 0
                mainItemCount = 0
                for item in self._listOfItems:
                    if item.sku == rule.sku:
                        mainItemCount += 1
                    if item.sku == rule.freeItem.sku:
                        freeItemCount += 1
                if mainItemCount > freeItemCount:
                    self._total -= rule.freeItem.price * freeItemCount
                else:
                    self._total -= rule.freeItem.price * mainItemCount
        for item in self._listOfItems:
            self._total += item.price
        return self._total