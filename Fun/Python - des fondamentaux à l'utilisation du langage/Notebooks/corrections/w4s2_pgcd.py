# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args

# @BEG@ name=pgcd
def pgcd(a, b):
    "le pgcd de a et b par l'algorithme d'Euclide"
    # l'algorithme suppose que a >= b
    # donc si ce n'est pas le cas 
    # il faut inverser les deux entrées
    if b > a : 
        a, b = b, a
    # boucle sans fin
    while True:
        # on calcule le reste 
        r = a % b
        # si le reste est nul, on a terminé
        if r == 0:
            return b
        # sinon on passe à l'itération suivante
        a, b = b, r
# @END@

# @BEG@ name=pgcd more=v2
# il se trouve qu'en fait la première inversion n'est
# pas nécessaire
# en effet si a <= b, la première itération de la boucle
# while va faire
# r = a % b = a
# et ensuite
# a, b = b, r = b, a
# ce qui provoque l'inversion
def pgcd_bis(a, b):
    while True:
        # on calcule le reste 
        r = a % b
        # si le reste est nul, on a terminé
        if r == 0:
            return b
        # sinon on passe à l'itération suivante
        a, b = b, r
# @END@

# xxx à publier ?
# le code proposé par un étudiant, et qui serait en mesure de gérer
# le cas b=0 qui semble-t-il provoque un ZeroDivisionError
# à voir aussi: l'inversion des deux entrées est probablement inutile
def pgcd_ter(a, b):
    if b > a : 
        a, b = b, a
    while b:
        a, b = b, a % b
    return a


def pgcd_ko(a, b):
    return a % b

inputs_pgcd = [
    Args(36 * 2**i * 3**j * 5**k,
         36 * 2**j * 3**k * 5**i)
 for i in range(3) for j in range(3) for k in range(2)
]

exo_pgcd = ExerciseFunction(pgcd, inputs_pgcd)
