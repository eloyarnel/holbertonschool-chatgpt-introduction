#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.flagged = [[False for _ in range(width)] for _ in range(height)]

    def in_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def print_board(self, reveal=False):
        clear_screen()
        print('   ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(f"{y:2} ", end='')
            for x in range(self.width):
                idx = y * self.width + x
                if reveal or self.revealed[y][x]:
                    if idx in self.mines:
                        ch = '*'
                    else:
                        count = self.count_mines_nearby(x, y)
                        ch = str(count) if count > 0 else ' '
                    print(ch, end=' ')
                else:
                    print('F' if self.flagged[y][x] else '.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if self.in_bounds(nx, ny) and (ny * self.width + nx) in self.mines:
                    count += 1
        return count

    def reveal(self, x, y):
        if not self.in_bounds(x, y) or self.flagged[y][x]:
            return True  # ignore invalid/flagged move

        idx = y * self.width + x
        if idx in self.mines:
            return False

        if self.revealed[y][x]:
            return True

        self.revealed[y][x] = True

        if self.count_mines_nearby(x, y) == 0:
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    nx, ny = x + dx, y + dy
                    if self.in_bounds(nx, ny) and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
        return True

    def toggle_flag(self, x, y):
        if self.in_bounds(x, y) and not self.revealed[y][x]:
            self.flagged[y][x] = not self.flagged[y][x]

    def won(self):
        # Win when all non-mine cells are revealed
        total_cells = self.width * self.height
        revealed_count = sum(sum(1 for c in row if c) for row in self.revealed)
        return revealed_count == total_cells - len(self.mines)

    def play(self):
        while True:
            self.print_board()
            move = input("Move: 'x y' to reveal, or 'f x y' to flag: ").strip().lower().split()

            try:
                if len(move) == 2:
                    x, y = map(int, move)
                    ok = self.reveal(x, y)
                elif len(move) == 3 and move[0] == 'f':
                    x, y = int(move[1]), int(move[2])
                    self.toggle_flag(x, y)
                    ok = True
                else:
                    print("Invalid format. Use: x y  OR  f x y")
                    continue

                if not ok:
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break

                if self.won():
                    self.print_board(reveal=True)
                    print("You win! 🎉")
                    break

            except ValueError:
                print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
