import pyfiglet


def print_text(text: str, font: str = "slant"):
    ascii_text = pyfiglet.figlet_format(text, font=font)
    print(ascii_text)


if __name__ == "__main__":
    print_text("Hello, World!")
