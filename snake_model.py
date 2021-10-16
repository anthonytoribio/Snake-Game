#snake_model.py
#Creator: Anthony Toribio
#Date: 7/04/2021

"""
This py file holds the code that is responsible for the logic of the
snake game, although some modules are seperated for cleanliness of the code.
"""

from snake_body import SnakeBody, SnakePart
from apple import Apple
import random


class SnakeBoard():
    def __init__(self):
        '''
        Initializes the board where the board is 17 length(cols) x 15 height(rows).
        '''
        #self.board = [[0 for i in range(15)] for i in range(17)] #Let 0 reper a empty space
        self.snake = SnakeBody()
        self.apple = Apple()
        #for part in self.snake.get_body():
            #self.board[part.get_col()][part.get_row()] = part.repre()
        #self.board[self.snake.get_head_col()][self.snake.get_head_row()] = self.snake.repre()
        self.add_apple()

    def _update_board(self):
        self.board = [[0 for i in range(15)] for i in range(17)]
        for part in self.snake.get_body():
            self.board[part.get_col()][part.get_row()] = part.repre()
        self.board[self.snake.get_head_col()][self.snake.get_head_row()] = self.snake.repre()

    def add_apple(self):
        added = False
        coords = []
        for part in self.snake.get_body():
            coords.append((part.get_col(),part.get_row()))
        coords.append((self.snake.get_head_col(), self.snake.get_head_row()))
        while not added:
            col = random.randint(0,16)
            row = random.randint(0,14)
            if (col,row) not in coords:
                self.apple.change_apple(col,row)
                added = True
        

    def move_snake(self,direction = None):
        inside = self.snake.move(direction)
        if self._check_snake_eats_apple():
            self.snake.add_snake_part()
            self.add_apple()
        game_over = self._check_snake_bound()
        if game_over or inside:
            return game_over or inside
        #self._update_board()
        return game_over


    def _check_snake_eats_apple(self) -> bool:
        s = self.get_snake()
        a = self.apple
        s_c = s.get_head_col()
        s_r = s.get_head_row()
        a_c = a.get_col()
        a_r = a.get_row()
        return s_c == a_c and s_r == a_r


    def _check_snake_bound(self) -> bool:
        a = self._check_snake_head()
        b = self._check_in_bounds()
        return a or b  #changed from and
    

    def _check_snake_head(self) -> bool:
        s = self.get_snake()
        col, row = s.get_head_col(), s.get_head_row()
        for part in s.get_body():
            c,r = part.get_col(), part.get_row()
            if col == c and row == r: #changed from or
                return True
        return False


    def _check_in_bounds(self) -> bool:
        s = self.get_snake()
        if -1 < s.get_head_col() < 17 and -1 < s.get_head_row() < 15:
            return False
        return True
        

    def game_over(self):
        bl = self.get_snake().get_body_len()
        print('|--------------------------|')
        print('|-------GAME OVER----------|')
        print(f'|-------SCORE: {bl if bl > 10 else str(bl) + "-" }----------|')
        print('|--------------------------|')
        print()


    def game_won(self):
        print(f'|--------------------------|')
        print(f'|-------GAME WON!----------|')
        print(f'|--------------------------|')
        print()

    def get_board(self):
        return self.board


    def get_snake(self):
        return self.snake

    def get_apple(self):
        return self.apple


    def _check_board(self):
        print(self.board)

















if __name__ == '__main__':
    s = SnakeBoard()
    s._check_board()
        
