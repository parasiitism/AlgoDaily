from collections import *

"""
    1st approach: orderdict
    - every thing is straight forward, actually it can be done with a hashtable and a linked list

    be careful of this corner case:
    0HX
    0TX
    000

    H: head
    T: tail
    X: body

    it allows the snake move from (0,1) to (1,1)

    Time of move()  O(1)
    Time of init()  O(RC)
    Space           O(RC)
    1100 ms, faster than 5.16%
"""


class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        # create matrix
        grid = []
        for _ in range(height):
            grid.append(width*[0])
        # create snake
        od = OrderedDict()
        od[(0, 0)] = True

        self.grid = grid
        self.food = food
        self.od = od

        # add food
        self.addFood()

    def addFood(self):
        if len(self.food) > 0:
            popI, popJ = self.food.pop(0)
            if 0 <= popI < len(self.grid) and 0 <= popJ < len(self.grid[0]):
                self.grid[popI][popJ] = 1

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        coor, b = self.od.popitem()
        i, j = coor
        nextI, nextJ = i, j
        if direction == 'U':
            nextI -= 1
        elif direction == 'D':
            nextI += 1
        elif direction == 'L':
            nextJ -= 1
        else:
            nextJ += 1

        # collides the wall
        if nextI < 0 or nextI+1 > len(self.grid) or nextJ < 0 or nextJ+1 > len(self.grid[0]):
            return -1

        # collide with itself
        if (nextI, nextJ) in self.od:
            tail, b = self.od.popitem(False)
            tailI, tailJ = tail[0], tail[1]
            self.od[tail] = True
            # python3 because of this new method, move_to_end()
            self.od.move_to_end(tail, last=False)
            if nextI == tailI and nextJ == tailJ:
                pass
            else:
                return -1

        # eat food
        if self.grid[nextI][nextJ] == 1:
            # add back the head
            self.od[(i, j)] = True
            # grow the head
            self.od[(nextI, nextJ)] = True
            # remove food
            self.grid[nextI][nextJ] = 0
            # add new food
            self.addFood()

            return len(self.od)-1

        # just move
        self.od[(i, j)] = True
        self.od.popitem(False)
        self.od[(nextI, nextJ)] = True
        return len(self.od)-1
