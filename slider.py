import random

SIZE = 4
PATTERNS = [[0, 3, 12, 13, 14, 15],
            [1, 2, 4, 7, 8, 11]]

PATTERNS_2 = [[0, 1, 4, 8],
              [2, 3, 7, 11],
              [5, 9 , 12, 13],
              [6, 10, 14, 15]]


class Board:

    pdbs2 = []
    pdbs4 = []
    def __init__(self):
        self.board = [[None for j in range(SIZE)] for i in range(SIZE)]
        self.parent = None

    def __repr__(self):
        rep = ''
        for i in range(SIZE):
            for j in range(SIZE):
                rep += ' %2s ' % self.board[i][j]
            rep += '\n'
        return rep


    def random_succ(self):
        i = random.uniform(0, 4 * SIZE - 1)
        return self.succ(int(i))

    def random_walk(self, steps):
        self.make_goal()
        b = self.clone_board()
        for i in range(steps):
            b = b.random_succ()
        return b

    def heuristic(self, h):
        if h == 0:
            if self.pdbs2:
                lista = []
                for pdb in self.pdbs2:
                    lista.append(pdb.get_heuristic(self))
                return max(lista)
        elif h == 1:
            return self.manhattan()

        elif h == 2:
            if self.pdbs4:
                lista = []
                for pdb in self.pdbs4:
                    lista.append(pdb.get_heuristic(self))
                return max(lista)
        else:
            return 0

    def random_state(self, steps):
        self.make_goal()
        b = self.clone_board()
        for j in range(steps):
            i = int(random.uniform(0, 4 * SIZE - 1))
            b = b.succ(i)
        return b

    def manhattan(self):
        suma = 0
        def min_dist(num, i, j):
            x = abs(num / SIZE - i)
            y = abs(num % SIZE - j)
            return min(x, SIZE - x) + min(y, SIZE - y)

        for i in range(SIZE):
            for j in range(SIZE):
                suma += min_dist(self.board[i][j], i , j)
        return int(suma / 4)


    def to_string(self):
        # Retorna el arreglo que representa el arreglo para poder reemplazar
        array = []
        for i in range(SIZE):
            for j in range(SIZE):
                array.append(self.board[i][j])
        return repr(array)


    def solution_length(self):
        if self.parent is not None:
            return 1 + self.parent.solution_length()
        return 0

    def print_solution(self):
        print(self)
        if self.parent:
            self.parent.print_solution()


    def make_goal(self):
        num = 0
        for i in range(SIZE):
            for j in range(SIZE):
                self.board[i][j] = num
                num += 1

    def check_goal(self):
        num = 0
        for i in range(SIZE):
            for j in range(SIZE):
                if self.board[i][j] != num:
                    return False
                num += 1
        return True

    def clone_board(self):
        b = self.__class__()
        for i in range(SIZE):
            b.board[i] = self.board[i][:]
        return b

    def succ(self, n): # 0 <= n <= 4*SIZE
        b = self.clone_board()
        b.parent = self

        if n >= 0 and n < SIZE:
            i = n
            aux = b.board[i][0]
            for j in range(SIZE - 1):
                b.board[i][j] = b.board[i][j + 1]
            b.board[i][SIZE - 1] = aux

        elif SIZE <= n < 2 * SIZE:
            i = n - SIZE
            aux = b.board[i][SIZE - 1]
            for j in range(SIZE - 1):
                b.board[i][SIZE - 1 - j] = b.board[i][SIZE - j - 2]
            b.board[i][0] = aux

        elif 2 * SIZE <= n < 3 * SIZE:
            j = n - 2 * SIZE
            aux = b.board[0][j]
            for i in range(SIZE - 1):
                b.board[i][j] = b.board[i + 1][j]
            b.board[SIZE-1][j] = aux

        elif 3 * SIZE <= n < 4 * SIZE:
            j = n - 3 * SIZE
            aux = b.board[SIZE - 1][j]
            for i in range(SIZE - 1):
                b.board[SIZE - 1 - i][j] = b.board[SIZE - i - 2][j]
            b.board[0][j] = aux


        return b

    def get_children(self):
        children = []
        for i in range(4 * SIZE):
            children.append(self.succ(i))
        return children


class AbstractBoard(Board):

    def __init__(self, n, l):
        Board.__init__(self)
        self.board = [[None for j in range(SIZE)] for i in range(SIZE)]
        self.parent = None
        self.distancia = 0
        self.n = n
        self.l = l

        if l == 0:
            self.distinguibles = PATTERNS[n]
        if l == 1:
            self.distinguibles = PATTERNS_2[n]


    def clone_board(self):
        b = AbstractBoard(self.n, self.l)
        for i in range(SIZE):
            b.board[i] = self.board[i][:]
        return b


    def make_target_pattern(self):
        num = 0
        for i in range(SIZE):
            for j in range(SIZE):
                if num not in self.distinguibles:
                    self.board[i][j] = 'X'
                else:
                    self.board[i][j] = num
                num += 1

    def check_goal(self):
        num = 0
        for i in range(SIZE):
            for j in range(SIZE):
                if num in self.distinguibles and self.board[i][j] != num:
                    return False
                num += 1
        return True
