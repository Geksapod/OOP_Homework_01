from math import prod
class Product:
    def __init__(self, name, price, description, size):
        self.name = name
        self.price = price
        self.description = description
        self.size = size

    def __str__(self):
        return f'{self.name} - {self.price} UAH\n{self.description}\n{self.size}'


class Customer:
    def __init__(self, surname, name, phone_number, location):
        self.surname = surname
        self.name = name
        self.phone_number = phone_number
        self.location = location

    def __str__(self):
        return f'{self.surname} {self.name[0]}., phone number - {self.phone_number}, {self.location}'


class Order:
    def __init__(self, order_number, customer):
        self.order_number = order_number
        self.customer = customer
        self.products = {}

    def add_product(self, product, price):
        if product not in self.products:
            self.products[product] = [1, price]
        else:
            self.products[product][0] += 1

    def order_list(self):
        order_list = [f'{i} - {j[0]} pcs' for i, j in self.products.items()]
        return order_list

    def total_order_price(self):
        return sum([prod(self.products[i]) for i in self.products])

    def __str__(self):
        return f"Order - {self.order_number}\n{'-' * 70}\n" \
               f"Customer - {self.customer}\n{'-' * 70}\n" +\
               '\n'.join(map(str, self.order_list())) + '\n' + '-' * 70 + '\n' + \
               'Total ' + str(self.total_order_price()) + ' UAH'

if __name__ == '__main__':
    battery_1 = Product('battery ABP7-12L', 776, '12v 7Ah AGM', '156 x 94 x 65')
    battery_2 = Product('battery AGM LPM 6V - 12 Ah', 658, '6v 12Ah AGM', '151 x 96 x 50')
    battery_3 = Product('battery LP1212', 1798, '12v 12Ah gel', '151 x 98 x 95')
    battery_4 = Product('battery GEL 12-12A-BS', 1290, '12v 10Ah gel', '150 x 87 x 106')


    customer_1 = Customer('Petrenko', 'Petro', '+380123123123', 'Kyiv')
    order_1 = Order('No 0001', customer_1)
    order_1.add_product(battery_1.name, battery_1.price)
    order_1.add_product(battery_4.name, battery_4.price)
    order_1.add_product(battery_1.name, battery_1.price)
    order_1.add_product(battery_2.name, battery_2.price)


    print(order_1)






