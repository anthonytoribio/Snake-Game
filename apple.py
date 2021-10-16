#apple.py
#Creator: Anthony Toribio
#Date: 7/07/2021

"""
This py file holds the class Apple which will be implemented in the snake_model
.py file.
"""

class Apple:
    def __init__(self):
        self.col = None
        self.row = None
        
    def change_apple(self,col,row):
        self.col = col
        self.row = row


    def get_col(self):
        return self.col


    def get_row(self):
        return self.row


    def repre(self):
        return 3
