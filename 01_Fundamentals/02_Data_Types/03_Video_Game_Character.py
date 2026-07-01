# Scenario:

# A video game stores information about a player.

# The following information is already known and stored in the program.

# • Character Name
# • Character Level
# • Health Points
# • Is Alive

# The program should display each value along with its data type.

# Assume all values are valid.

character_name = "The Silver Surfer"
character_level = 7
current_health_points = 67.83
is_alive = True

print(f"The Characters name is {character_name} and has a data type of {type(character_name)}")
print(f"The Character is currentely on level {character_level} and has a data type of {type(character_level)}")
print(f"The Characters current health points out of 100 are {current_health_points} and has a data type of {type(current_health_points)}")
print(f"The Characters is alive status is {is_alive} and has a data type of {type(is_alive)}")