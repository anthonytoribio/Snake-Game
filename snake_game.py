#snake_game.py
#Creator: Anthony Toribio
#Date: 7/04/2021

"""
This py file holds the code that is responsible for snake game that the
user interact with. The game will use the PyGame Library.
"""

import pygame
from snake_model import SnakeBoard

_Black = (0,0,12)
_Blue = (0,91,183)
_Green = (55,194,43)
_Red = (192,18,34)

class Snake_Game:

    def __init__(self):
        self.board = SnakeBoard()
        self._running = True

    def run(self):
        pygame.init()

        self._resize_surface((600,600))

        clock = pygame.time.Clock()
        self._redraw()


        while self._running:
            clock.tick(10)
            changed = self._handle_events()
            if not changed:
                game_over = self.board.move_snake()
                if game_over:
                    self._running = False
                    self.board.game_over()
                elif self.board.get_snake().get_body_len() == 255:
                    self.board.game_won()
            self._redraw()
            

        pygame.quit()


    def _handle_events(self) -> bool:
        '''
        Handles events such as movements and quiting the game.
        '''
        moved = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.board.move_snake('L')
                elif event.key == pygame.K_RIGHT:
                    self.board.move_snake('R')
                elif event.key == pygame.K_UP:
                    self.board.move_snake('U')
                elif event.key == pygame.K_DOWN:
                    self.board.move_snake('D')
                moved = True
        return moved


    def _redraw(self) -> None:
        '''
        Draws the board and pieces/snake/apple
        '''
        surface = pygame.display.get_surface()

        surface.fill(pygame.Color(_Green))
        self._draw_snake()
        self._draw_apple()
        pygame.display.flip()
        

    def _draw_snake(self):
        '''
        Draws the snake.
        '''
        width, height = pygame.display.get_surface().get_size()
        width = width/17
        height = height/15
        surface = pygame.display.get_surface()
        s = self.board.get_snake()
        for part in s.get_body():
            rectangle = pygame.Rect(part.get_col() * width, part.get_row() * height, width, height)
            pygame.draw.rect(surface, _Blue, rectangle)
        rectangle = pygame.Rect(s.get_head_col() * width, s.get_head_row() * height, width,height)
        pygame.draw.rect(surface, _Black, rectangle)
        #print(s.get_head_col(), s.get_head_row())


    def _draw_apple(self):
        '''
        Draws apple.
        '''
        width, height = pygame.display.get_surface().get_size()
        width = width/17
        height = height/15
        surface = pygame.display.get_surface()
        a = self.board.get_apple()
        rectangle = pygame.Rect(a.get_col() * width, a.get_row() * height, width, height)
        pygame.draw.rect(surface, _Red, rectangle)
    

    
    def _resize_surface(self, size: (int,int)) -> None:
        '''
        Resizes the screen.
        '''
        pygame.display.set_mode(size, pygame.RESIZABLE)



if __name__ == '__main__':
    Snake_Game().run()
