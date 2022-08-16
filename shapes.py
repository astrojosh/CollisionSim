import numpy as np
import matplotlib.pyplot as plt


class Shape:
    """
    This is a class for creating shapes.

    Attributes:
        points (list[tuple[float, float]]): List of points of the surface of the shape in the form (x, y)
    """

    def __init__(self, points: None = None) -> None:
        """
        The constructor for Shape class.

        Parameters:
            points (list[tuple[float, float]]): List of points of the surface of the shape in the form (x, y)
        """

        if points:
            self.points: list[tuple[float, float]] = points
        else:
            self.points: list[tuple[float, float]] = []

    def add_points(self, new_points: list[tuple[float, float]]) -> None:
        """
        The function to add points to the shape.

        Parameters:
            new_points (list[tuple[float, float]]): The list of points to be added to the shape in the form (x, y)

        # Returns:
        #     ComplexNumber: A complex number which contains the sum.
        """

        self.points += new_points

    def plot_shape(self) -> None:
        """The function to plot the shape."""

        plt.figure(figsize=(15, 15))
        plt.scatter([x for x, _ in self.points], [y for _, y in self.points])
        plt.show()


class Circle(Shape):
    """
    This is a class for creating the Circle class, which is a subclass of the Shape class.

    Attributes:
        radius (float): The radius of the circle.
    """

    def __init__(self, radius: float) -> None:
        """
        The constructor for Circle class, which is a subclass of the Shape class.

        Parameters:
            radius (float): The radius of the circle.
        """

        super().__init__()
        self.radius = radius

    def gen_points(self, point_density: float = 100) -> None:
        """
        The function to generate the points for the Circle object.

        Parameters:
            point_density (float): The density of the points generated for the surface of the shape.
        """

        self.point_density = point_density

        # Generate points equally spaced around the surface of the circle
        t = np.linspace(0, 2 * np.pi, int(self.point_density * self.radius))
        x = self.radius * np.cos(t)
        y = self.radius * np.sin(t)

        super().add_points(list(zip(x, y)))
        super().add_points(list(zip(x, -y)))


class Square(Shape):
    """
    This is a class for creating the Square class, which is a subclass of the Shape class.

    Attributes:
        width (float): The width of the square.
    """

    def __init__(self, width: float) -> None:
        """
        The constructor for Square class, which is a subclass of the Shape class.

        Parameters:
            width (float): The width of the circle.
        """

        super().__init__()
        self.width = width

    def gen_points(self, point_density: float = 100) -> None:
        """
        The function to generate the points for the Square object.

        Parameters:
            point_density (float): The density of the points generated for the surface of the shape.
        """

        self.point_density = point_density

        x = np.linspace(
            -self.width / 2, self.width / 2, int(self.point_density * self.width)
        )
        y = (self.width / 2) * np.ones_like(x)

        super().add_points(list(zip(x, y)))
        super().add_points(list(zip(x, -y)))
        super().add_points(list(zip(y, x)))
        super().add_points(list(zip(-y, x)))
