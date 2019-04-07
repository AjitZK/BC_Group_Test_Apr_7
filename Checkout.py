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
            self._total += rule.applyDiscount(self._listOfItems)
        for item in self._listOfItems:
            self._total += item.price
        return self._total