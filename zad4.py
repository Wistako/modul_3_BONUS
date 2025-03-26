dice = {}

for first in range(1,7):
    for second in range(1,7):
        if dice.get(str(first+second)):
            pass
        else: 
            dice[str(first+second)] = []
            
        dice[str(first+second)].append((first, second))

print(dice)