from collections import deque

def potion_production(substances_quantities, energy_level):
    potions = {
        "Brew of Immortality": 110,
        "Essence of Resilience": 100,
        "Draught of Wisdom": 90,
        "Potion of Agility": 80,
        "Elixir of Strength": 70
    }

    crafted_potions = []
    crafted_levels = set()

    while substances_quantities and energy_level and len(crafted_potions) < 5:

        if not substances_quantities:
            break
        if not energy_level:
            break

        current_substance = substances_quantities.pop()
        current_crystal = energy_level.popleft()
        current_energy = current_substance + current_crystal

        if current_energy in potions.values() and current_energy not in crafted_levels:
            for potion, level in potions.items():
                if level == current_energy:
                    crafted_potions.append(potion)
                    crafted_levels.add(level)
        else:
            lower_potions = [level for level in potions.values()
                             if level < current_energy and level not in crafted_levels]
            if lower_potions:
                max_possible = max(lower_potions)
                for potion, level in potions.items():
                    if level == max_possible:
                        crafted_potions.append(potion)
                        crafted_levels.add(level)
                if current_crystal - 20 > 0:
                    energy_level.append(current_crystal - 20)
            else:
                current_crystal -= 5
                if current_crystal > 0:
                    energy_level.append(current_crystal)

    if len(crafted_potions) == 5:
        print("Success! The alchemist has forged all potions!")
    else:
        print("The alchemist failed to complete his quest.")

    if crafted_potions:
        print(f"Crafted potions: {', '.join(crafted_potions)}")

    if substances_quantities:
        print(f"Substances: {', '.join(map(str, substances_quantities[::-1]))}")
    if energy_level:
        print(f"Crystals: {', '.join(map(str, energy_level))}")


substances = [int(el) for el in input().split(', ')]  # stack
crystals = deque(int(x) for x in input().split(', '))
potion_production(substances, crystals)
