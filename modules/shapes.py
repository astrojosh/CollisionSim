from __future__ import annotations
import numpy as np
import matplotlib.pyplot as plt


class Collider:
    """
    This is a class for creating colliders, made up of multiple shapes.

    Attributes:
        shapes (tuple[Shape]): List of Shape objects that make up the container.
        points (list[tuple[float, float]]): List of points of the surface of the collider in the form (x, y).
    """

    def __init__(self, *shapes: Shape) -> None:
        """
        The constructor for Collider class.

        Parameters:
            shapes (tuple[Shape]): List of Shape objects that make up the container.
        """
        self.shapes = shapes

        self.points: list[tuple[float, float]] = []
        for shape in self.shapes:
            self.points += shape.points

    def plot_shape(self) -> None:
        """The function to plot the shape."""

        plt.scatter([x for x, _ in self.points], [y for _, y in self.points])

    def show_shape_plot(self) -> None:
        """The function to show the plot of the shape."""

        plt.figure(figsize=(15, 15))
        self.plot_shape()
        plt.show()


class Shape(Collider):
    """
    This is a class for creating shapes.

    Attributes:
        points (list[tuple[float, float]]): List of points of the surface of the shape in the form (x, y).
        rot (float): The angle, in radians, to rotate the shape.
        x_origin (float): The x position of the origin of the shape.
        y_origin (float): The y position of the origin of the shape.
    """

    def __init__(self, points: list[tuple[float, float]] | None = None) -> None:
        """
        The constructor for Shape class.

        Parameters:
            points (list[tuple[float, float]]): List of points of the surface of the shape in the form (x, y).
        """

        super().__init__()

        if points:
            self.points = points
        else:
            self.points = []

    def add_points(self, new_points: list[tuple[float, float]]) -> None:
        """
        The function to add points to the shape.

        Parameters:
            new_points (list[tuple[float, float]]): The list of points to be added to the shape in the form (x, y).

        # Returns:
        #     ComplexNumber: A complex number which contains the sum.
        """

        self.points += new_points

    def rotate_points(self, rot: float) -> None:
        """
        The function to rotate the points of the shape.

        Parameters:
            rot (float): The angle, in radians, to rotate the shape.
        """

        self.rot = rot

        for i, (x, y) in enumerate(self.points):
            x_rot: float = x * np.cos(self.rot) - y * np.sin(self.rot)
            y_rot: float = x * np.sin(self.rot) + y * np.cos(self.rot)
            self.points[i] = (x_rot, y_rot)

    def set_origin(self, x_origin: float, y_origin: float) -> None:
        """
        The function to set the origin shape.

        Parameters:
            x_origin (float): The x position of the origin of the shape.
            y_origin (float): The y position of the origin of the shape.
        """

        self.x_origin = x_origin
        self.y_origin = y_origin

        self.points = list(
            zip(
                [x + self.x_origin for x, _ in self.points],
                [y + self.y_origin for _, y in self.points],
            )
        )


class Circle(Shape):
    """
    This is a class for creating the Circle class, which is a subclass of the Shape class.

    Attributes:
        radius (float): The radius of the circle.
        point_density (float): The density of the points generated for the surface of the shape. Default = 100.
    """

    def __init__(
        self, radius: float, gen_points: bool = True, point_density: float = 100
    ) -> None:
        """
        The constructor for Circle class, which is a subclass of the Shape class.

        Parameters:
            radius (float): The radius of the circle.
            gen_points (bool): The condition whether the initialiser should auto-generate the shape points. Default = True.
            point_density (float): The density of the points generated for the surface of the shape. Default = 100.
        """

        super().__init__()
        self.radius = radius

        if gen_points:
            self.gen_points(point_density)

    def gen_points(self, point_density: float = 100) -> None:
        """
        The function to generate the points for the Circle object.

        Parameters:
            point_density (float): The density of the points generated for the surface of the shape. Default = 100.
        """

        self.point_density = point_density

        # Generate points equally spaced around the surface of the circle
        t = np.linspace(0, 2 * np.pi, int(np.pi * self.point_density * self.radius))
        x = self.radius * np.cos(t)
        y = self.radius * np.sin(t)

        super().add_points(list(zip(x, y)))
        super().add_points(list(zip(x, -y)))


class Square(Shape):
    """
    This is a class for creating the Square class, which is a subclass of the Shape class.

    Attributes:
        width (float): The width of the square.
        point_density (float): The density of the points generated for the surface of the shape. Default = 100.
    """

    def __init__(
        self, width: float, gen_points: bool = True, point_density: float = 100
    ) -> None:
        """
        The constructor for Square class, which is a subclass of the Shape class.

        Parameters:
            width (float): The width of the square.
            gen_points (bool): The condition whether the initialiser should auto-generate the shape points. Default = True.
            point_density (float): The density of the points generated for the surface of the shape. Default = 100.
        """

        super().__init__()
        self.width = width

        if gen_points:
            self.gen_points(point_density)

    def gen_points(self, point_density: float = 100) -> None:
        """
        The function to generate the points for the Square object.

        Parameters:
            point_density (float): The density of the points generated for the surface of the shape. Default = 100.
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
