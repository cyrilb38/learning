# python3
import sys


def compute_min_refills(distance, tank, stops, position=0, current_count=0):
    # write your code here
    
    # si le véhicule peut accéder directement au point d'arrivée, alors il n'a pas besoin de refill
    if (position + tank) >= distance:
        return current_count
    else:
        # si il n'y a pas de stops, on ne peut donc pas atteindre le bout
        if not stops :
            return -1
        # si le prochain stop est trop loin, idem
        elif stops[0] > (position + tank):
            return -1
        else:
            # Si il y a des stops, on prends le dernier que l'on peut atteindre avec notre tank
            while stops and (stops[0] <= (position + tank)): 
                last_stop = stops.pop(0)
            
            # on rappelle la fonction sur la suite du parcours
            position = last_stop
            current_count += 1
            return compute_min_refills(distance, tank, stops, position, current_count)
    

# print(compute_min_refills(950, 400, [200, 375, 550, 750]))
# print(compute_min_refills(700, 200, [100, 200, 300, 400]))
# print(compute_min_refills(250, 250, [20, 50, 90, 140, 200]))
# print(compute_min_refills(10, 3, [1, 2, 5, 9]))

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
