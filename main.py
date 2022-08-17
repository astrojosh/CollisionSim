import numpy as np
from modules.shapes import Collider, Circle, Square
from modules.objects import Object
from modules.physics import Sim


def main() -> None:

    c = Circle(radius=1)

    s = Square(width=1.5)
    s.rotate_points(rot=np.pi / 6)
    s.set_origin(1, 1)

    col = Collider(c, s)

    obj = Object(pos=(0, 0))

    sim = Sim()
    sim.add_collider(col)
    sim.add_object(obj)
    sim.run_simulation()
    sim.show_simulation()


if __name__ == "__main__":
    main()
