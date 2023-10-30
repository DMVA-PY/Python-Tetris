from grid import Grid
from blocks import *
import random

# Variables: grid, blocks, current_block, next_block, game_over
# Metodos: get_random_block, move_left, move_right, move_down, lock_block, rotate, block_fits, block_inside, reset, draw

class Game:
    # Declara variables iniciales de la clase Game
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(),LBlock(),OBlock(),SBlock(),TBlock(),ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0

    # Retorna un block aleatorio, requiere todos los blocks y el metodo random.
    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(),LBlock(),OBlock(),SBlock(),TBlock(),ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    # Actualiza el tablero de puntos del juego
    def update_scores(self, lines_cleared, move_down_points):
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500
        self.score += move_down_points

    # Mueve el block a al izquierda, requiere la funcion block_inside y current_block.move
    def move_left(self):
        self.current_block.move(0, -1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, 1)

    # Mueve el block a al derecha, requiere la funcion block_inside y current_block.move
    def move_right(self):
        self.current_block.move(0, 1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, -1)

    # Mueve el block abajo, requiere la funcion block_inside y current_block.move
    def move_down(self):
        self.current_block.move(1, 0)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(-1, 0)
            self.lock_block()
    
    # Lockea el block cuando colisiona con el fondo del tablero
    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_full_rows()
        self.update_scores(rows_cleared, 0)
        if self.block_fits() == False:
            self.game_over = True

    # Rota el block a la siguiente posicion del diccionario, si no esta dentro del tablero, cancela la rotacion
    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() == False or self.block_fits() == False:    
           self.current_block.undo_rotation()
    
    # CORRECCION: ultimo return debe ser TRUE
    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False
        return True
        
    # Determina si el block esta dentro del tablero, requiere el block actual 
    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True 
    
    # Resetea el juego
    def reset(self):
        self.grid.reset()
        self.blocks = [IBlock(), JBlock(),LBlock(),OBlock(),SBlock(),TBlock(),ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0
    
    # Dibuja el tablero, requiere las variables grid y current_block
    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11)
        

        if self.next_block.id == 2:
            self.next_block.draw(screen, 255, 300)
        elif self.next_block.id == 3:
            self.next_block.draw(screen, 255, 270)
        elif self.next_block.id == 1:
            self.next_block.draw(screen, 240, 270)
        else:
            self.next_block.draw(screen, 270, 270)