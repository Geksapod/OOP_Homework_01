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