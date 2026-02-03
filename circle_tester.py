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

    

origin = Point()
print(origin)
p1 = Point(-4.2, 7.1)
print(p1)