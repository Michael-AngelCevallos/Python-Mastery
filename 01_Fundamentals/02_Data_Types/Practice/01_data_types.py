# Algorithm

# Something like:

# 1. Create variables for each data type.
# 2. Store an example value in each.
# 3. Ask Python what type each variable is.
# 4. Display the results.
# Here's Your Challenge

# I am NOT going to give you the code.

# You already know how to:

# create variables
# assign values
# print values

# The only new thing you need is this function:

# type()

# Think of it exactly like print().

# Except instead of displaying a value...

# It returns the type of that value.
#==========================================================================================================

name = "Michael"
age = 30
gpa = 3.33
is_passing = True

name_type = type(name)
age_type = type(age)
gpa_type = type(gpa)
is_passing_type = type(is_passing)


print(f"The Data type for {name} is: {name_type}")
print(f"The Data type for {age} is: {age_type}")
print(f"The Data type for {gpa} is: {gpa_type}")
print(f"The Data type for {is_passing} is: {is_passing_type}")