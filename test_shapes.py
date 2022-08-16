from modules.shapes import Circle, Square


def main() -> None:
    c = Circle(1)
    c.gen_points()
    c.plot_shape()

    s = Square(1)
    s.gen_points()
    s.plot_shape()


if __name__ == "__main__":
    main()
