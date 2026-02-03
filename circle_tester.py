class Point:
    def __init__(self, x = 0.0, y = 0.0) -> None:
        self._x = x
        self._y = y

    def __str__(self) -> str:
        return f"({self._x}, {self._y})"
    
    def get_x(self) -> float:
        """
        getter
        """
        return self._x
    
    def set_x(self, new_x: float) -> None:
        """Setter for X
        """
        self._x = new_x

class Circle:
    """Represents a simple circle.
    """
    def __init__(self, radius: float = 1.0, center: Point = None) -> None:
        self._radius = radius
        if center is None:
            center = Point()
            self._center = center
        self._center = center
        pass

    def __str__(self) -> str:
        """
        Docstring for __str__
        
        :param self: Description
        """
        return f"Radius: {self._radius} \nCenter: {self._center}"

origin = Point()
print(origin)
p1 = Point(-4.2, 7.1)
print(p1)

unit_circle = Circle()
print(unit_circle)
c1 = Circle(5.0, p1)
print(c1)