from Item import Item
from PricingRule import PricingRule, XForY, BulkDiscount, FreeGift

class Checkout:
    """
    Takes in an array of PricingRule instances to determine the discounts applied\n
    Accepts instances of Item class to be considered for this checkout and would be able to tell you the total price to be charged for this checkout.
    """
    def __init__(self, pricingRules=None):
        if pricingRules is None:
            self._pricingRules = []
        else:
            onlyPricingRuleInstances = True
            for rule in pricingRules:
                if not isinstance(rule, PricingRule):
                    onlyPricingRuleInstances = False
                    print('The given array has other types of data apart from just instances of class PricingRule')
                    print('So, there will simply be no pricing rules applied to this checkout instance')
                    break
            if onlyPricingRuleInstances:
                self._pricingRules = pricingRules
            else:
                self._pricingRules = []
        self._listOfItems = []
        self._total = 0

    def scan(self, item):
        """
        Takes in Item instances and adds it to the list of items that will be charged for this checkout
        """
        if isinstance(item,Item):
            self._listOfItems.append(item)
    
    def totalPrice(self) -> float:
        """
        Returns a float value denoting the total cost for this checkout after applying all discounts as per the pricingRules
        """
        self._total = 0
        for item in self._listOfItems:
            self._total += item.price
        for rule in self._pricingRules:
            self._total += rule.applyDiscount(self._listOfItems)
        # return a rounded value to the nearest 0.00 value
        # because python doesn't represent decimals very well
        return round(self._total, 2)