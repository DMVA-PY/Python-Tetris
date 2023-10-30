from colors import Colors
import pygame
from position import Position

# the Class Block has 4 methods.
class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0
        self.column_offset = 0
        self.rotation_state = 0
        self.colors = Colors.get_cell_colors()

    # Mueve al tetromino, sumando las nuevas coordenadas a las viejas.
    def move(self, rows, columns):
        self.row_offset += rows
        self.column_offset += columns
        
    # Otorga las nuevas 4 posiciones del tetromino.
    def get_cell_positions(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = [] 
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles
    
    # Rota al tetromino una posicion y si se encuentra en la posicion 3, vuelve a la 0, para asi poder seguir sumando posiciones.
    def rotate(self):
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    # Resta una posicion a las rotaciones, si las rotaciones llegan a -1,
    def undo_rotation(self):
        self.rotation_state -= 1
        if self.rotation_state == -1:
            self.rotation_state = len(self.cells) - 1

    # Dibuja el tetromino
    def draw(self, screen, offset_x, offset_y): 
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size , offset_y + tile.row * self.cell_size, self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)