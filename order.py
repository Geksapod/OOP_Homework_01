"""This module provides access to Order class"""


from math import prod
from customer import Customer
from product import Product

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

    def add_product(self, product: Product, price: int, quantity: int=1):
        """Add product to self.products dictionary

        Parameters
        ----------
        product: Product
            Product that is being added to an order.
        price: int
            Price of a product.
        quantity: int
            Quantity of a product.
        """

        self.products[product] = [price, quantity]


    def order_list(self):
        """Create list of added to an order products"""

        order_list = [f"{i} - {j[1]} pcs" for i, j in self.products.items()]
        return order_list

    def total_order_price(self):
        """Returns calculated total price of an order."""

        return sum(prod(self.products[i]) for i in self.products)

    def __getitem__(self, product: Product):
        """Get product and quantity of the product in the order

        Parameters
        ----------
        product: Product
            Product that is being added to an order.
        """

        if product in self.products.keys():
            return product, self.products[product][1]
        raise KeyError("There is not this product in the order")

    def __iter__(self):
        """Returns the OrderIter class iterator."""

        return OrderIter(self.products)


    def __str__(self):
        """Return formatted order's name."""

        return f"Order - {self.order_number}\n{'-' * 70}\n" \
               f"Customer - {self.customer}\n{'-' * 70}\n" +\
               '\n'.join(map(str, self.order_list())) + '\n' + '-' * 70 + '\n' + \
               'Total ' + str(self.total_order_price()) + ' UAH'


class OrderIter:
    """This class is used to make class order an iterable"""

    def __init__(self, products: dict):
        """Initialisation of orderiter's attributes.

        Parameters
        ----------
        products: dict
            Dictionary with product key and list of price and quantity values.

        """

        self.products = products
        self.product = iter(self.products.keys())
        self.index = 0

    def __next__(self):
        """Returns the next items from the products iterator. If default is given and the iterator is exhausted,
        it is returned instead of raising StopIteration.
        """

        if self.index < len(self.products.keys()):
            self.index += 1
            product = next(self.product)
            quantity = self.products[product][1]
            return product, quantity
        raise StopIteration




