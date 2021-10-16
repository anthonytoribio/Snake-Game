#snake_body.py
#Creator: Anthony Toribio
#Date: 7/04/2021

#Let the int 1 be representative of the snake head and let int 2
#represent the snake part that is not the head



#To-DO: Figure out SnakeBody and how update and move will work
#when using self.direction. Is self.direction needed? How will it change? etc.
#Edit figured it out now have to test it with the game

class SnakeBody():
    def __init__(self):
        self.head_col = 3
        self.head_row = 7
        self.body = [SnakePart(2,7), SnakePart(1,7)]
        self.dir = []
        self.direction = 'R'


    def _change_dir(self,direction:str):
        self.dir = [self.head_col,self.head_row,direction]


    def update_h(self,direction = None):
        if direction == None:
            direction = self.direction
        changed = False
        if self.direction != direction:
            correct = False
            if self.direction == 'R' and direction != 'L':
                correct = True
            elif self.direction == 'L' and direction != 'R':
                correct = True
            elif self.direction == 'U' and direction != 'D':
                correct = True
            elif self.direction == 'D' and direction != 'U':
                correct = True
            if correct:
                self._change_dir(direction)
                self.direction = direction
                changed = True
            else:
                direction = self.direction
        if direction == 'L':
            self.head_col -= 1
        elif direction == 'R':
            self.head_col += 1
        elif direction == 'U':
            self.head_row -= 1
        elif direction == 'D':
            self.head_row += 1
        else:
            raise ValueError(f'SnakeBody: Error direction invalid: {direction}')
        return changed
        

    def move(self,direction = None):   #Add a way so that it detects if head is 'on' another body part
        if direction == None:
            changed = self.update_h()
        else:
            changed = self.update_h(direction)
        for part in self.body:
            if changed:
                part.add_turn(self.get_dir())
            part.move()
        return self._check_head_and_body()
        #print(self.body)


    def _check_head_and_body(self) -> bool:
        for part in self.body:
            c,r = part.get_col(), part.get_row()
            if self.head_col == c and self.head_row == r:
                return True
        return False


    def add_snake_part(self):
        lsp = self.body[-1]
        c = lsp.get_col()
        r = lsp.get_row()
        turns = lsp.get_turns()
        direction = lsp.get_direction()
        if direction == 'L':
            c += 1
        elif direction == 'R':
            c -= 1
        elif direction == 'U':
            r += 1
        elif direction == 'D':
            r -= 1
        self.body.append(SnakePart(c,r,turns,direction))


    def get_direction(self):
        return self.direction


    def get_dir(self):
        return self.dir
        

    def get_head_col(self):
        return self.head_col


    def get_head_row(self):
        return self.head_row


    def get_body_len(self):
        return len(self.body) + 1

    def get_body(self):
        return self.body


    def repre(self):
        return 1


class SnakePart():
    def __init__(self,col:int,row:int,turns = [], direction = 'R'):
        self.col = col
        self.row = row
        self.turns = list(turns)
        self.direction = direction


    def update_p(self):
        if self.direction == 'L':
            self.col -= 1
        elif self.direction == 'R':
            self.col += 1
        elif self.direction == 'U':
            self.row -= 1
        elif self.direction == 'D':
            self.row += 1
        else:
            raise ValueError(f'SnakePart.update_p: Error direction invalid: {direction}')


    def add_turn(self,li_di:list):
        if li_di not in self.turns:
            self.turns.append(li_di)


    def check_turn(self):
        if len(self.turns) != 0:
            x,y = self.turns[0][0], self.turns[0][1]
            if x == self.col and y == self.row:
                self.direction = self.turns[0][2]
                #print(self,'TURNED')
                del self.turns[0]


    def move(self):
        self.check_turn()
        self.update_p()
        

    def get_col(self):
        return self.col


    def get_row(self):
        return self.row


    def get_direction(self):
        return self.direction

    def get_turns(self):
        return self.turns


    def repre(self):
        return 2

    def __repr__(self):
        return f'SnakePart({self.col}, {self.row}, {self.turns})'
