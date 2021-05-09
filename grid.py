class Grid:
    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y
        self.board = [[-1 for j in range(size_x)] for i in range(size_y)]
        self.valid_pos = [self.size_y - 1 for _ in range(self.size_x)]
        self.current_player = 0

    def play(self, player, selection):
        self.board[self.valid_pos[selection]][selection] = player
        if self.winning_move(player, selection):
            print("Victory !")
            input()
        self.valid_pos[selection] -= 1

    def winning_column(self, player, selection):
        current_line = self.valid_pos[selection]
        if self.size_y - current_line >= 4:
            for i in range(1, 4):
                if self.board[current_line + i][selection] != player:
                    return False
            return True
        return False

    def winning_row(self, player, selection):
        line = self.valid_pos[selection]
        for c in range(max(0, selection - 3), min(self.size_x - 3, selection + 1)):
            if all(self.board[line][c + i] == player for i in range(4)):
                return True
        return False

    def winning_diagonal(self, player, selection):
        # Bottom left to top right
        line = self.valid_pos[selection]
        diagonale = [(line, selection)]
        for i in range(1, 4):
            if line + i < self.size_y and 0 <= selection - i:
                diagonale.append((line + i, selection - i))
            if 0 <= line - i and selection + i < self.size_x:
                diagonale.append((line - i, selection + i))
        diagonale.sort(key=lambda e: e[1])
        tot = 1
        for i, e in enumerate(diagonale[:-1]):
            suiv = diagonale[i+1]
            if self.board[e[0]][e[1]] == self.board[suiv[0]][suiv[1]]:
                tot += 1
                if tot == 4:
                    return True
            else:
                tot = 1

        # Top left to bottom right
        diagonale = [(line, selection)]
        for i in range(1, 4):
            if line + i < self.size_y and selection + i < self.size_x:
                diagonale.append((line + i, selection + i))
            if 0 <= line - i and 0 <= selection - i:
                diagonale.append((line - i, selection - i))
        diagonale.sort(key=lambda e: e[1])
        tot = 1
        for i, e in enumerate(diagonale[:-1]):
            suiv = diagonale[i+1]
            if self.board[e[0]][e[1]] == self.board[suiv[0]][suiv[1]]:
                tot += 1
                if tot == 4:
                    return True
            else:
                tot = 1
        return False

    def winning_move(self, player, selection):
        return self.winning_column(player, selection) or self.winning_row(player, selection) or self.winning_diagonal(player, selection)

    def possible_moves(self):
        for c in range(self.size_x):
            if self.available(c):
                yield c

    def available(self, column):
        return self.valid_pos[column] != -1
    
    def show(self):
        for i in range(self.size_x):
            print(i, end=" ")
        print()
        for l in self.board:
            for element in l:
                if element == -1:
                    print(" ", end=" ")
                elif element == 0:
                    print("o", end=" ")
                else:
                    print("x", end=" ")
            print()

    def score(self, player):
        # 4 = 10000
        # 3 = 100
        # 2 = 10
        score = 0

        """
        #Score per row 
        for l in self.board:
            combo = 0
            for c in l:
                if c == player:
                    combo += 1
                else:
                    if combo != 0:
                        if combo == 4:
                            combo += 1
                        score += 10 ** (combo - 1)
                        combo = 0
            if combo != 0:
                if combo == 4:
                    combo += 1
                score += 10 ** (combo - 1)

        #Score per column
        for col in range(self.size_x):
            combo = 0
            for line in self.board:
                if line[col] == player:
                    combo += 1
                else:
                    if combo != 0:
                        if combo == 4:
                            combo += 1
                        score += 10 ** (combo - 1) - 1
                        combo = 0
            if combo != 0:
                if combo == 4:
                    combo += 1
                score += 10 ** (combo - 1) - 1
                combo = 0

        #Score per diagonal bottom to top
        for diag in range(4, self.size_x + self.size_y - 3):
            beginning = max(0, diag - self.size_y)
            combo = 0
            for j in range(min(diag, self.size_x - beginning, self.size_y)):
                if self.board[min(self.size_y, diag) - j - 1][beginning + j] == player:
                    combo += 1
                else:
                    if combo != 0:
                        if combo == 4:
                            combo += 1
                        score += 10 ** (combo - 1) - 1
                        combo = 0
            if combo != 0:
                if combo == 4:
                    combo += 1
                score += 10 ** (combo - 1) - 1
                combo = 0

        """
        print(f"le score est {score}")
                

    def game_over(self):
        for c in self.valid_pos:
            if c != -1:
                return False
        return True
