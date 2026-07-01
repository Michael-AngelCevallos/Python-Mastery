# Scenario:

# A company needs a simple employee record.

# The following information is already known and stored in the program.

# • Employee Name
# • Employee ID
# • Years Worked
# • Full-Time Status

# The program should display each value along with its data type.

# Assume all values are valid.

employee_name = "John"
employee_ID = "324657"
years_worked = 8
full_time_status = True

print(f"the employee's name is {employee_name} and has a data type of {type(employee_name)}")
print(f"the employee's ID is {employee_ID} and has a data type of {type(employee_ID)}")
print(f"the employee has worked for the company for {years_worked} years and has a data type of {type(years_worked)}")
print(f"the employee's full time status is {full_time_status} and has a data type of {type(full_time_status)}")