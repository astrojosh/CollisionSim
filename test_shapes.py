import numpy as np
from matplotlib import pyplot as plt
from modules.shapes import Circle, Square


def main() -> None:
    c = Circle(radius=1)
    c.gen_points()
    # c.show_shape_plot()

    s = Square(width=1)
    s.gen_points()
    # s.show_shape_plot()

    c1 = Circle(radius=1)
    c1.gen_points()
    c1.rotate_points(rot=np.pi / 4)

    s1 = Square(width=1)
    s1.gen_points()
    s1.rotate_points(rot=np.pi / 4)

    plt.figure(figsize=(15, 15))
    c1.plot_shape()
    c.plot_shape()
    plt.show()


if __name__ == "__main__":
    main()
