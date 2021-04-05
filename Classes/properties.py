# to have control over attribute of class

class Product:
    def __init__(self, price):
        self.price = price
        # to make an attribute private we should pre-fix it with "__"

    # a decorator coverts a instance method into a class method

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price Cannot be negative.")
        self.__price = value

    #price = property(price, set_price)


product = Product(-50)
print(product.price)
# how to ensure product don't have a negative value
