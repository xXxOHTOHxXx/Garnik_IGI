import abc

class FigureColour:
    

class GeometricFigure(abc.ABC):
    @abc.abstractmethod 
    def area (self): pass       # площадь фигуры
		
class Rectangle(GeometricFigure):
    def __init__(self, width:float, height:float):
        self.width = width
        self.height = height

class Hexagon(GeometricFigure):
        def __init__(self, side:float):
            self.side = side