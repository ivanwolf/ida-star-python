import argparse
from ida2 import ida
from pdb import Pdb
from slider import AbstractBoard, Board

parser = argparse.ArgumentParser(description="IDA* para el problema de sliders, ingresar dos enteros")
parser.add_argument('L', type=int, nargs=1,
                    help='Estimacion del largo de los problemas a resolver, un buen valor puede ser 8 o 9')
parser.add_argument('N', type=int, nargs=1,
                    help='Cantidad de problemas a resolver')

args = parser.parse_args()
largo = args.L[0]
cantidad = args.N[0]

print("Cantidad de pasos random: %2d" % largo)
print("Cantidad de ejemplos    : %2d" % cantidad)
print("\n")

## PDB4: 4 patrones con 4 piezas distinguibles
t0 = AbstractBoard(0, 1)
t1 = AbstractBoard(1, 1)
t2 = AbstractBoard(2, 1)
t3 = AbstractBoard(3, 1)

t0.make_target_pattern()
t1.make_target_pattern()
t2.make_target_pattern()
t3.make_target_pattern()

pdb40 = Pdb(t0)
pdb41 = Pdb(t1)
pdb42 = Pdb(t2)
pdb43 = Pdb(t3)

pdb40.setup_pdb(1)
pdb41.setup_pdb(1)
pdb42.setup_pdb(1)
pdb43.setup_pdb(1)

Board.pdbs4.append(pdb40)
Board.pdbs4.append(pdb41)
Board.pdbs4.append(pdb42)
Board.pdbs4.append(pdb43)
## PDB2: 2 Patrones con 6 piezas distinguibles
## Creamos la partición de 2 con 6 distinguibles cada una
## Atención estas líneas de código pueden hacer que el programa se demore ya
## que las bases de datos quedan de 450MB. Sin embargo genera mejoras considerables
## si tomamos en cuenta la cantidad de nodos expandidos usando esta heurística.

"""
target0 = AbstractBoard(0, 0)
target1 = AbstractBoard(1, 0)

target0.make_target_pattern()
target1.make_target_pattern()

pdb0 = Pdb(target0)
pdb1 = Pdb(target1)

pdb0.setup_pdb(0)
pdb1.setup_pdb(0)

Board.pdbs2.append(pdb0)
Board.pdbs2.append(pdb1)"""

print("\n")
for i in range(cantidad):
    s = Board()
    s = s.random_state(largo)
    print("Experimento %2d: \n" % i)
    print(s)
    # ida(s, 0) #PDB con 6 distinguibles
    ida(s, 2) #PDB con 4 distinguibles
    ida(s, 1) #manhattan
