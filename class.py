class ShoppingCart:
    '''
    Shooping Class
    '''

    def __init__(self):
        self.__items = []

    @property
    def item(self):
        '''
        returns item from the shopping cart class
        '''
        return self.__items.pop()

    @item.setter
    def item(self, item):
        self.__items.append(item)

    def __len__(self):
        return len(self.__items)

    def __contains__(self, item):
        return item in self.__items

    def __getitem__(self, index):
        return self.__items[index]

    def __iter__(self):
        return iter(self.__items)

    def __str__(self):
        return 'Shopping Cart: {}'.format(self.__items)


cart = ShoppingCart()

cart.item = 'Orange'

SIZE = len(cart)
print(SIZE)

GOTTEN = cart.item
print(GOTTEN)

# size = len(cart)
# print(size)
