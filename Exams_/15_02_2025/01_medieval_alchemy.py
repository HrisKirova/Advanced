from collections import deque

substances_quantities = [int(el) for el in input().split(', ')] # stack
energy_levels = deque(int(x) for x in input().split(', '))
crafted_potions = []

while substances_quantities and energy_levels:
    current_substance = substances_quantities.pop()
    current_energy = energy_levels.popleft()
    current_cum = current_substance + current_energy
    if current_cum == 70:
        crafted_potions.append("Elixir of Strength")
    elif current_cum == 80:
        crafted_potions.append("Potion of Agility")
    elif current_cum == 90:
        crafted_potions.append("Draught of Wisdom")
    elif current_cum == 100:
        crafted_potions.append("Essence of Resilience")
    elif current_cum == 110:
        crafted_potions.append("Brew of Immortality")
    else:
        
