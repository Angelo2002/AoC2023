from enum import Enum


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Cell:
    x = 0
    y = 0
    extraSize = 0
    value = None

    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        if isinstance(value, str):
            self.extraSize = len(value) - 1
        else:
            self.extraSize = 0


class Grid:
    matrix = None
    posx = 0
    posy = 0

    def __init__(self, data):
        self.posx = 0
        self.posy = 0
        matrix = []
        if isinstance(data, str):
            for row in str.split("\n"):
                new_row = []
                matrix.append(new_row)
                for element in row:
                    new_row.append(Cell(len(matrix), len(new_row), element))
        else:
            for row in data:
                new_row = []
                matrix.append(new_row)
                for element in row:
                    new_row.append(Cell(len(matrix), len(new_row), element))
        self.matrix = matrix

    def get_cell(self, x, y):
        return self.matrix[x][y]

    def get_neighbors(self, x=None, y=None, get_values=True):
        if x is None:
            x = self.posx
        if y is None:
            y = self.posy
        neighbors = []
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if 0 <= i < len(self.matrix) and 0 <= j < len(self.matrix[i]):
                    neighbors.append(self.matrix[i][j].value if get_values else self.matrix[i][j])
        return neighbors

    def get_neighbours_values(self, x=None, y=None):
        if x is None:
            x = self.posx
        if y is None:
            y = self.posy

        neighbors = self.get_neighbors(x, y)
        values = []
        for neighbor in neighbors:
            values.append(neighbor.value)
        return values

    def get_current_cell(self):
        return self.matrix[self.posx][self.posy]

    def move(self, direction):
        if direction == Direction.UP and self.posx > 0:
            self.posx -= 1
        elif direction == Direction.DOWN and self.posx < len(self.matrix) - 1:
            self.posx += 1
        elif direction == Direction.LEFT and self.posy > 0:
            self.posy -= 1
        elif direction == Direction.RIGHT and self.posy < len(self.matrix[self.posx]) - 1:
            self.posy += 1
        else:
            return False
        return True

    def move_until(self, direction, value):
        while self.get_current_cell().value != value:
            if not self.move(direction):
                return False
        return True

    def move_until_not(self, direction, value):
        while self.get_current_cell().value == value:
            if not self.move(direction):
                return False
        return True

    def has_neighbour(self, value, x=None, y=None):
        if x is None:
            x = self.posx
        if y is None:
            y = self.posy

        neighbors = self.get_neighbors(x, y)
        for neighbor in neighbors:
            if neighbor.value == value:
                return True
        return False

    def goRight(self):
        return self.move(Direction.RIGHT)

    def goLeft(self):
        return self.move(Direction.LEFT)

    def goUp(self):
        return self.move(Direction.UP)

    def goDown(self):
        return self.move(Direction.DOWN)

    def get_line_neighbours(self, x=None, y=None, get_values=True):
        if x is None:
            x = self.posx
        if y is None:
            y = self.posy

        neighbors = self.get_neighbors(x, y,False)
        values = []
        for neighbor in neighbors:
            if neighbor.y == y or neighbor.x == x:
                values.append(neighbor.value if get_values else neighbor)
        return values

    def get_diagonal_neighbours(self, x=None, y=None, get_values=True):
        if x is None:
            x = self.posx
        if y is None:
            y = self.posy
        neighbors = self.get_neighbors(x, y)
        values = []
        for neighbor in neighbors:
            if neighbor.y != y and neighbor.x != x:
                values.append(neighbor.value if get_values else neighbor)
        return values

