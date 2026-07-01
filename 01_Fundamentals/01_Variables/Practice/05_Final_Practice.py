# ======================================================
# Practice Range
# Phase 1 - Python Fundamentals
# Mission 1.1 - Variables
#
# Practice 05 - Paint Estimator
#
# Scenario:
#
# A painter is preparing to paint a rectangular wall.
#
# The height and width of the wall are already known and
# stored in the program.
#
# One gallon of paint covers 350 square feet.
#
# The program should:
#
# 1. Calculate the wall's area.
# 2. Calculate approximately how many gallons of paint
#    are needed.
# 3. Display both results.
#
# Assume all values are valid.
#
# ======================================================




# ! Start of Code ============================================================================================================================


# Wall Dementions
height_of_wall = 20
width_of_wall = 13


# Calculation - To Find the Area of the Wall
area_of_wall = height_of_wall * width_of_wall

# 1 gallon of paint sq ft coverage
paint_coverage_per_gallon = 350

# Calulation - Finds the Number Of Gallons Needed For Wall 
gallons_of_paint = area_of_wall / paint_coverage_per_gallon



print(area_of_wall)
print(gallons_of_paint)