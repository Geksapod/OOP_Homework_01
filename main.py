from math import prod


class Product:
    """Class describes a product."""

    def __init__(self, name: str, price: int, description: str, size: str):
        """Initialisation of product's attributes.

        Parameters
        ----------
        name: str
            Name of a product.
        price: int
            Price of a product.
        description: str
            Description of a product.
        size: str
            Size (length x width x height) of a product.

        Raises
        ------
        TypeError
            If price is not integer.
        ValueError
            If price is negative or equal to zero.
        """

        self.name = name
        self.price = price
        self.description = description
        self.size = size
        if not isinstance(price, int):
            raise TypeError("The product price must be an integer")
        if price <= 0:
            raise ValueError("The product price can not be negative or equal to zero")

    def __str__(self):
        """Return formatted product's name."""

        return f"{self.name} - {self.price} UAH\n{self.description}\n{self.size}"


class Customer:
    """Class describes a customer."""

    def __init__(self, surname: str, name: str, phone_number: str, location: str):
        """Initialisation of customer's attributes.

        Parameters
        ----------
        surname: str
            Name of a customer.
        name: str
            Name of a customer.
        phone_number: str
            Phone number of a customer.
        location: str
            Location of a customer.
        """

        self.surname = surname
        self.name = name
        self.phone_number = phone_number
        self.location = location

    def __str__(self):
        """Return formatted customer's name."""

        return f"{self.surname} {self.name[0]}., phone number - {self.phone_number}, {self.location}"


class Order:
    """Class describes an order.

    Methods
    _______
    add_product(self, product, price)
        Add product to self.products dictionary.
    order_list(self)
        Create list of added to an order products.
    total_order_price(self)
        Returns calculated total price of an order.
    """

    def __init__(self, order_number: str, customer: Customer):
        """Initialisation of order's attributes.

        Parameters
        ----------
        order_number: str
            Order number.
        customer: Customer
            Customer is person who make an order.
        self.products: dict
            self.products dictionary contains products from order as keys,
            lists of products quantities from order and price as value.
        """
        self.order_number = order_number
        self.customer = customer
        self.products = {}

    def add_product(self, product: Product, price: int):
        """Add product to self.products dictionary

        Parameters
        ----------
        product: Product
            Product that is being added to an order.
        price: int
            Price of a product.
        """

        if product not in self.products:
            self.products[product] = [1, price]
        else:
            self.products[product][0] += 1

    def order_list(self):
        """Create list of added to an order products"""

        order_list = [f"{i} - {j[0]} pcs" for i, j in self.products.items()]
        return order_list

    def total_order_price(self):
        """Returns calculated total price of an order."""

        return sum(prod(self.products[i]) for i in self.products)

    def __str__(self):
        return f"Order - {self.order_number}\n{'-' * 70}\n" \
               f"Customer - {self.customer}\n{'-' * 70}\n" +\
               '\n'.join(map(str, self.order_list())) + '\n' + '-' * 70 + '\n' + \
               'Total ' + str(self.total_order_price()) + ' UAH'


if __name__ == '__main__':
    try:
        battery_1 = Product('battery ABP7-12L', -776, '12v 7Ah AGM', '156 x 94 x 65')
        battery_2 = Product('battery AGM LPM 6V - 12 Ah', 658, '6v 12Ah AGM', '151 x 96 x 50')
        battery_3 = Product('battery LP1212', 1798, '12v 12Ah gel', '151 x 98 x 95')
        battery_4 = Product('battery GEL 12-12A-BS', 1290, '12v 10Ah gel', '150 x 87 x 106')

        customer_1 = Customer('Petrenko', 'Petro', '+380123123123', 'Kyiv')
        order_1 = Order('No 0001', customer_1)
        order_1.add_product(battery_1.name, battery_1.price)
        order_1.add_product(battery_4.name, battery_4.price)
        order_1.add_product(battery_1.name, battery_1.price)
        order_1.add_product(battery_2.name, battery_2.price)

    except (TypeError, ValueError) as error:
        print(error)








