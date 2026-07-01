# Scenario:

# A veterinarian's office wants a simple program that stores
# information about a pet during a visit.

# The program should store:

# • Pet Name
# • Species
# • Age
# • Weight (lbs)
# • Microchip Number
# • Vaccinations Up To Date
# • Body Temperature

# The program should display every value and its data type.

# Assume all values are valid.




pet_name = "Ares"
species = "Dog"
age_in_years = 5
weight = 32.6
micro_chip_num = "234657"
up_to_date_vacc = False
body_temp = 99.8




print(f"Pet Name: {pet_name}")
print(f"Data Type for name: {type(pet_name)}")

print()

print(f"Pet Species: {species}")
print(f"Data Type for name: {type(species)}")

print()

print(f"Pet Age(in Human Years): {age_in_years}")
print(f"Data Type for age: {type(age_in_years)}")

print()

print(f"Pets Weight(LBS): {weight}")
print(f"Data Type for weight: {type(weight)}")

print()

print(f"Pets Micro Chip Number: {micro_chip_num}")
print(f"Data Type for Micro Chip Number: {type(micro_chip_num)}")

print()

print(f"Pet Vaccinatins Up-To-Date status: {up_to_date_vacc}")
print(f"Data Type for vaccinations status: {type(up_to_date_vacc)}")

print()

print(f"Pets body temp: {body_temp}")
print(f"Data Type for body temp: {type(body_temp)}")

print()
