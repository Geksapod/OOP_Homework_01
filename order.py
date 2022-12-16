from math import prod
import customer
import product


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

    def __init__(self, order_number: str, customer: customer.Customer):
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

    def add_product(self, product: product.Product, price: int):
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