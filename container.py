class CloudTags:
    def __init__(self, s3_bucket_name):
        self.__s3_bucket_name = s3_bucket_name


class Product:
    def __init__(self, product_id, product_name, price, tags):
        self.__product_id = product_id
        self.__product_name = product_name
        self.price = price
        self.__tags = tags

    def __str__(self):
        return f'Product: {self.__product_name}'

    def get_product_id(self):
        return self.__product_id

    def get_product_name(self):
        return self.__product_name

    def get_tags(self):
        return self.__tags

    def set_tags(self, tags):
        self.__tags = tags

    # def get_price(self):
    #     return self.__price

    # def set_price(self, price):
    #     if price < 0:
    #         raise ValueError('Price cannot be negative')
    #     self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('Price cannot be negative')

        self.__price = value
