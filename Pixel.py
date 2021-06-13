def picture():
    class Pixel:

        def __init__(self, x=0, y=0, red=0, blue=0, green=0):
            self._x, self._y, self._red, self._blue, self._green = x, y, red, blue, green
            self.gray = 0

        def set_coords(self, num_x, num_y):
            self._x = num_x
            self._y = num_y
            print(self._x, self._y)

        def set_gray(self):
            self.gray = self._blue + self._green + self._red
            self.gray = int(self.gray/3)
            self._blue = self._green = self._red = self.gray

        def print_pixel_info(self):
            al = [self._blue, self._green, self._red]
            if al.count(0) == 2:
                for num in [self._blue, self._green, self._red]:
                    for b in "Blue", "Green", "Red":
                        if num > 50:
                            big = b
                        else:
                            big = ""
            else:
                    big = ""
            print(f"X: {self._x}, Y: {self._y}, Color: {self._blue , self._green , self._red} {big}")

    def main():
        col = Pixel(5, 6, 250, 40)
        col.print_pixel_info()
        col.set_gray()
        col.print_pixel_info()

    main()


if __name__ == '__main__':
    picture()