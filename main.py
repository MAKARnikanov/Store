import utils

item1 = utils.Item("Смартфон", 10000, 20)
item2 = utils.Item("Ноутбук", 20000, 5)

print(item1.calculate_total_price())
print(item2.calculate_total_price())

utils.Item.pay_rate = 0.8
item1.apply_discount()
print(item1.price)
print(item2.price)

print(utils.Item.all)