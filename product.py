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

        return f"{self.name}, {self.description}, {self.size}mm - {self.price} UAH"