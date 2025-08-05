# -*- coding: utf-8 -*-
import time
from maze import Maze
from collections import deque

def solve_maze_backtracking(maze):
    '''
    Implementação do algoritmo de backtracking usando uma pilha para resolver o labirinto.
    Retorna True se o prêmio for encontrado, False caso contrário.
    '''
    stack = deque()  
    start_pos = maze.get_init_pos_player()
    stack.append(start_pos)  

    visited = set()  # evita loops

    while stack:
        current_pos = stack.pop()  #LIFO

        if maze.find_prize(current_pos):
            print("Prêmio encontrado na posição:", current_pos)
            return True

        if current_pos not in visited:
            visited.add(current_pos)
            maze.mov_player(current_pos)  
            time.sleep(0.1)  

            x, y = current_pos
            adjacent_positions = [
                (x-1, y),  # Cima
                (x+1, y),  # Baixo
                (x, y-1),  # Esquerda
                (x, y+1)   # Direita
            ]

            for pos in adjacent_positions:
                if (0 <= pos[0] < maze.M.shape[0] and 
                    0 <= pos[1] < maze.M.shape[1] and 
                    maze.is_free(pos) and 
                    pos not in visited):
                    stack.append(pos)  

    print("Prêmio não encontrado.")
    return False

maze_csv_path = "labirinto1.txt"
maze = Maze() 
maze.load_from_csv(maze_csv_path)
maze.run()  
maze.init_player()  

solve_maze_backtracking(maze)