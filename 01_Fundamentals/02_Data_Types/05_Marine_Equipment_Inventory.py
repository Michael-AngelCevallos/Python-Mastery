# Scenario:

# A logistics system stores information about a piece of equipment.

# The following information is already known and stored in the program.

# • Equipment Name
# • Serial Number
# • Weight (lbs)
# • Is Operational

# The program should display each value along with its data type.

# Assume all values are valid.


equipment_name = "M-4 Rifle"
serial_number = "5643321"
equipment_weight = 6.36
is_operational = True

print(f"The Current equipment name is {equipment_name} which has a data type of {type(equipment_name)}, \n the Serial Number for this equipment is {serial_number} which has a data type of {type(serial_number)}, \n the weight of the equipment is {equipment_weight} which has a data type of {type(equipment_weight)}, \n and the operational status of the equipment is determined to be {is_operational} which has a data type of {type(is_operational)}")