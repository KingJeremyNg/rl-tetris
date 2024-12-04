class Piece(object):
    rows = 20
    columns = 10

    def __init__(self, column, row, shape, shapeColor):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = shapeColor
        self.rotation = 0  # number from 0-3
