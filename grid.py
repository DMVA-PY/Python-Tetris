import pygame
from colors import Colors

# Variables: num_rows, num_cols, cell_size, grid, colors 
# Metodos: print_grid, is_inside, is_empty, is_row_full, clear_row, move_row_down, clear_full_rows, reset, draw

class Grid:
    # Declara variables iniciales de la clase grid
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = Colors.get_cell_colors()
    
    # Imprime el tablero mediante una iteracion, requiere numero de filas y columnas y un array bidimensional.
    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols): 
                print(self.grid[row][column], end = ' ')
            print()

    # Determina si el tetromino esta dentro del tablero, requiere numero de filas y columnas.
    def is_inside(self, row, column):
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        return False 
    
    # Chequea si el tablero se encuentra vacio en dicha posicion, requiere row y column 
    def is_empty(self, row, column):
	    if self.grid[row][column] == 0:
	        return True
	    return False
    
    # Chequea si la fila del tablero esta vacia en dicha posicion, requiere de row
    def is_row_full(self, row):
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True 
    
    # Limpia la fila, requiere de row
    def clear_row(self, row):
        for column in range(self.num_cols):
            self.grid[row][column] = 0

    # Mueve la fila hacia abajo un numero especifico de celdas, 
    def move_row_down(self, row, num_rows):
        for column in range(self.num_cols):
            self.grid[row+num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0

    # Limpia las filas del tablero que esten llenas y luego
    def clear_full_rows(self):
        completed = 0
        for row in range(self.num_rows-1, 0, -1):
            if self.is_row_full(row): 
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)
        return completed

    # Resetea el juego
    def reset(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0

    # Imprime cada celda del tablero mediante una iteracion y le asigna un color y tamano, 
    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column*self.cell_size + 11, row*self.cell_size + 11, self.cell_size -1 , self.cell_size -1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)

    