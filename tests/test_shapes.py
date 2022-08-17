import numpy as np
from modules.shapes import Collider, Circle, Square


def main() -> None:

    c = Circle(radius=1)

    s = Square(width=1.5)
    s.rotate_points(rot=np.pi / 6)
    s.set_origin(1, 1)

    col = Collider(c, s)
    col.show_shape_plot()


if __name__ == "__main__":
    main()
