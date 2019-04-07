from PricingRule import PricingRule, XForY, BulkDiscount, FreeGift
from Item import Item, IPad, AppleTV, MacBookPro, VGAAdapter
from Checkout import Checkout

ipd1 = IPad()
mbp1 = MacBookPro()
atv1 = AppleTV()
vga1 = VGAAdapter()
atv2 = AppleTV()
atv3 = AppleTV()

atvDiscount = XForY(3,2,'atv')
ipdDiscount = BulkDiscount(5, 499.99, 'ipd')
mbpDiscount = FreeGift(VGAAdapter(), 'mbp')

pricingRules = [atvDiscount, ipdDiscount, mbpDiscount]

co = Checkout(pricingRules)
# co.scan(ipd1)
co.scan(mbp1)
co.scan(atv1)
co.scan(vga1)
co.scan(atv2)
co.scan(atv3)

totalPrice = co.totalPrice()

print(totalPrice)
