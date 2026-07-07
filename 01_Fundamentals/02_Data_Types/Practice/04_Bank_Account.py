# Scenario:

# A bank stores information about a customer account.

# The following information is already known and stored in the program.

# • Customer Name
# • Account Number
# • Current Balance
# • Account Is Active

# The program should display each value along with its data type.

# Assume all values are valid.


customer_name = "Alex"
account_Number = "34567823"
current_balance = 2000.14
account_active_status = True


print(f"The Customers name is {customer_name} and has the data type of {type(customer_name)}")
print(f"The Customers account number is {account_Number} and has the data type of {type(account_Number)}")
print(f"The Customers current balance is {current_balance} and has the data type of {type(current_balance)}")
print(f"The Customers account status of still active is {account_active_status} and has the data type of {type(account_active_status)}")