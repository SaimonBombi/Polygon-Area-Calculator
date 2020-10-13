class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        #print(self.width + self.height)

    def __str__(self):
        return "Rectangle" + "(width=" + str(self.width) + ", height=" + str(self.height) + ")"

    def set_width(self, width):
        self.width = width
        return self.width

    def set_height(self, height):
        self.height = height
        return self.height

    def get_area(self):
        area = (self.width * self.height)
        return area

    def get_perimeter(self):
        perimeter = (2 * self.width) + (2 * self.height)
        return perimeter

    def get_diagonal(self):
        diagonal = ((self.width ** 2) + (self.height ** 2)) ** .5
        return diagonal

    def get_picture(self):
        if (self.height > 50) or (self.width > 50):
            return "Too big for picture."
        else:
            picwidth = self.width
            picheight = self.height
            countdown = picheight
            line = ""
            while countdown > 0:
                line += "*"* picwidth + "\n"
                countdown-=1
        return line

    def get_amount_inside(self, anothershape):
        numinside = self.get_area() / anothershape.get_area()
        return int(numinside)


class Square(Rectangle):

    def __init__(self, side):
        self.width = side
        self.height = side
        self.side = side

    def __str__(self):
        return "Square(side=" + str(self.side) + ")"

    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side
        return self.side

    def set_width(self, side):
        self.width = side
        self.side = side
        return self.side

    def set_height(self, side):
        self.height = side
        self.side = side
        return self.side
