
name = "pikachu"
age_human = 27
power_level = 47.9
pokemon = True
moves = ["Thunderbolt", "Quick Attack", "Surf", "Iron Tail"]

age_pokemon = age_human / 7
age_rounded = round(age_pokemon)
capitalised_name = name.capitalize()
power_level_rounded = round(power_level)
name_length = len(name)
age_name_nonsense = name_length * age_human

if pokemon == True:
    print("My name is " + capitalised_name + " I am " + str(age_rounded) + " years old. I have a power level of " + str(power_level_rounded) + " and these are my moves: " + str(moves))
else:
    print("This isn't a pokemon!")