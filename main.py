from PricingRule import PricingRule, XForY, BulkDiscount, FreeGift
from Item import Item, IPad, AppleTV, MacBookPro, VGAAdapter
from Checkout import Checkout

ipd1 = IPad()
ipd2 = IPad()
ipd3 = IPad()
ipd4 = IPad()
ipd5 = IPad()
ipd6 = IPad()
mbp1 = MacBookPro()
vga1 = VGAAdapter()
atv1 = AppleTV()
atv2 = AppleTV()
atv3 = AppleTV()
atv4 = AppleTV()

pricingRules = []

pricingRules.append(XForY(3,2,AppleTV()))
pricingRules.append(BulkDiscount(4, 499.99, IPad()))
pricingRules.append(FreeGift(1, VGAAdapter(), MacBookPro()))

co = Checkout(pricingRules)
co.scan(atv1)
co.scan(mbp1)
co.scan(vga1)
co.scan(atv2)
co.scan(ipd1)
co.scan(ipd2)
co.scan(ipd3)
co.scan(ipd4)
co.scan(ipd5)
co.scan(atv3)
co.scan(atv4)

totalPrice = co.totalPrice()

print(totalPrice)
