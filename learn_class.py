class Point:
    '''
    A simple point class with x and y coordinates.
    '''
    # class attribute
    default_color = 'red'  # Color(255,255,255)


# class constructor

    def __init__(self, x, y):
        '''
        Initialize the point with x and y coordinates.
        '''

        # instance attributes
        self.x = x
        self.y = y

    # class methods
    @classmethod
    def create_point(cls, color=None):
        '''
        Create a point with x and y coordinates.
        '''
        new_point = cls(0, 0)
        new_point.default_color = color
        return new_point

# class method
    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
point.draw()
