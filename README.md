# labirinto

    maze.py (inalterado).
    main_maze.py (alterado).
    labirinto1.txt (inalterado).

        Pilha (stack):

        deque é usado como pilha (LIFO) para armazenar posições a serem exploradas.

        a cada iteração, a última posição adicionada é removida (stack.pop()).

    Posições Adjacentes:

        para cada posição atual, geramos as 4 posições vizinhas (cima, baixo, esquerda, direita).

        é verificado se a posição é válida (dentro do labirinto, livre e não visitada).

    Condição de Parada:

        se maze.find_prize(current_pos) for True, o prêmio foi encontrado.

        se a pilha estiver vazia e o prêmio não for encontrado, retorna False.

    Visualização:

        maze.mov_player(current_pos) atualiza a posição do jogador no labirinto.

        time.sleep(0.1) adiciona um pequeno delay para visualização passo a passo.
