def pyramid(string, height):
    for i in range(1, height + 1):
        spaces = " " * (i - 1)
        layer = string[:i * 2 - 1][::-1]
        print(spaces + layer.center(height * 2 - 1))

base_string = "abcdefghijklmnopqrstuvwxyz"
pyramid_height = 10
pyramid(base_string, pyramid_height)