from collections import deque
import os.path
import json


class Pdb:

    def __init__(self, target_pattern):
        self.target = target_pattern #AbstractBoard object
        self.n = target_pattern.n
        self.data = {}

    def __repr__(self):
        rep = ''
        for k, v in self.data.items():
            rep += '%s : %3d' % (k, v) + '\n'
        return rep

    def setup_pdb(self, l, new=False):
        if l == 1:
            if not os.path.isfile('pdb4-{}.txt'.format(self.n)) or new:
                self.bfs()
                with open('pdb4-{}.txt'.format(self.n), 'w') as file:
                    json.dump(self.data, file, indent=2)
            else:
                with open('pdb4-{}.txt'.format(self.n), 'r') as file:
                    self.data = json.load(file)
            print("PDB cargada")

        if l == 0:
            if not os.path.isfile('pdb{}.txt'.format(self.n)) or new:
                self.bfs()
                with open('pdb{}.txt'.format(self.n), 'w') as file:
                    json.dump(self.data, file, indent=2)
            else:
                with open('pdb{}.txt'.format(self.n), 'r') as file:
                    self.data = json.load(file)
            print("PDB cargada")


    def get_heuristic(self, state):

        SIZE = len(state.board)
        distinguibles = self.target.distinguibles
        lista = []
        for i in range(SIZE):
            for j in range(SIZE):
                if state.board[i][j] in distinguibles:
                    lista.append(state.board[i][j])
                else:
                    lista.append('X')
        return self.data[repr(lista)]


    def bfs(self):
        print("Preparando la PDB...")
        cola = deque()
        self.target.distancia = 0
        self.data[self.target.to_string()] = 0
        cola.append(self.target)

        while cola:
            current = cola.popleft()
            for child in current.get_children():
                if not child.to_string() in self.data:
                    child.distancia = current.distancia + 1
                    self.data[child.to_string()] = child.distancia
                    cola.append(child)
